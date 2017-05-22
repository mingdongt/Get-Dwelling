import os
import functools
import numpy as np

import pandas

from django.conf import settings
from django.views.generic import (
    TemplateView,
    FormView,
)
from django.shortcuts import render

from .forms import AnalyzeInputForm

DATA_FILE_NAME = 'data.h5'

LARGE_FIELD_MAP = {
    'Dwelling number': 'Dwelling number class',
}


class IndexView(TemplateView):
    """ Home page view for the website. """

    template_name = 'dwelling/index.html'


class DataSourceView(TemplateView):
    """ Data source view for the website. """

    template_name = 'dwelling/data_source.html'


class DataAnalyzeView(FormView):

    form_class = AnalyzeInputForm
    template_name = 'dwelling/data_analyze.html'
    graph_template = 'dwelling/graph.html'


    def post(self, request, *args, **kwargs):
        self.request = request
        return super(DataAnalyzeView, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        """ Extract form data and plot table if valid """

        filter_conditions = self.get_filter_conditions(form)

        filtered_data = self.get_filtered_data(filter_conditions)

        agg_func_rep = self.return_agg_func_rep(
            form,
            form.cleaned_data['aggregation_function']
        )
        return self.plot_pivot_table(
            filtered_data,
            form.cleaned_data['row'],
            form.cleaned_data['column'],
            form.cleaned_data['aggregation_field'],
            form.cleaned_data['aggregation_function'],
            agg_func_rep,
        )

    def return_agg_func_rep(self, form, field):

        """Return human readable label for aggregation method. """

        field_header_dict = dict(form.fields['aggregation_function'].choices)
        return field_header_dict[field]

    def plot_pivot_table(self, filtered_data, row, column,
                         agg_field, agg_func, agg_func_rep):

        """ Render template with pivot table parameters. """

        table_kwargs = {
            'data': filtered_data,
            'aggfunc': agg_func,
            'values': [agg_field],
        }

        base_title = '{} of {}'.format(agg_func_rep, agg_field)

        context_kwargs = {}
        response_kwargs = {
            'request': self.request,
            'template_name': self.graph_template,
        }
        if row == 'None' and column == "None":
            pass

        else:
            row, column = self.transfer_large_fields(row, column)

            if row == 'None':
                table_kwargs['columns'] = [column]
                pivot_table = pandas.pivot_table(**table_kwargs)

                table_title = self.get_table_title(base_title, column)
                table_rows = ['']
                table_columns = self.get_table_column_fields(pivot_table)

            elif column == "None":
                table_kwargs['index'] = [row]
                pivot_table = pandas.pivot_table(**table_kwargs)

                table_title = self.get_table_title(base_title, row)
                table_rows = self.get_table_row_fields(pivot_table)
                table_columns = ['']


            else:
                table_kwargs['columns'], table_kwargs['index'] = [column], [row]
                pivot_table = pandas.pivot_table(**table_kwargs)

                table_rows = self.get_table_row_fields(pivot_table)
                table_columns = self.get_table_column_fields(pivot_table)
                table_title = self.get_table_title(base_title, row, column)

            context_kwargs['spots'] = self.get_table_spots(pivot_table)
            context_kwargs['title'] = table_title
            context_kwargs['rows'] = table_rows
            context_kwargs['columns'] = table_columns

            response_kwargs['context'] = context_kwargs

        return render(**response_kwargs)

    def get_table_title(self, title, *args):
        """ Return title for the pivot table. """

        for arg in args:
            title = '{} per {}'.format(title, arg)
        return title

    def get_table_row_fields(self, pivot_table):
        return map(str, pivot_table.index)

    def get_table_column_fields(self, pivot_table):

        return [column_field[1:] if isinstance(column_field, set) else column_field
                for column_field in list(pivot_table)]

    def transfer_large_fields(self, *fields):
        """ Filter and transfer field with large amount of unique values. """

        return [LARGE_FIELD_MAP[field]
                if field in LARGE_FIELD_MAP.keys() else field
                for field in fields]

    def get_table_spots(self, pivot_table):
        """ Generate and return spots for the pivot table. """

        row = 0
        spots = []
        for index, row_data in pivot_table.iterrows():
            column = 0
            for unit in row_data:
                if pandas.isnull(unit):
                    spots.append([row, column, 0])
                else:
                    spots.append([row, column, unit])
                column += 1
            row += 1
        return spots

    def get_filter_conditions(self, form):
        """ Return filter conditions for all filter fields. """

        filter_conditions = {}
        form_data = form.cleaned_data

        for field in form.filter_fields:

            # Get rid of the filter if condition is not given.
            if form_data[field.field]:

                # Get distinct value for census years.
                if field.field == 'census_year_range':
                    condition = self.get_distinct_years(form_data[field.field])
                else:
                    condition = form_data[field.field]

                filter_conditions[field] = condition

                if field.field == 'search_street_address':
                    filter_conditions[field] = [condition]

        return filter_conditions

    def get_distinct_years(self, year_ranges):
        """ Process and return distinct census years from received form 
        data. """

        distinct_years = []

        for year_range in year_ranges:
            years = map(int, year_range.split('-'))

            # A range of year
            if len(years) > 1:
                start_year, end_year = years
                years = range(start_year, end_year + 1)

            distinct_years.extend(years)

        # Get distinct values
        return list(set(distinct_years))

    def get_filtered_data(self, filter_conditions):
        """ Return filtered Dataframe. """

        # Read HDF5 table
        file_ = os.path.join(str(settings.APPS_DIR), DATA_FILE_NAME)
        df = pandas.read_hdf(file_, 'table')

        # Generate logical conditions for the filter conditions.
        logical_conditions = [self.get_logical_condition(df, field, value)
                              for field, value in filter_conditions.items()]

        if logical_conditions:
            return df[self.conjunction(logical_conditions)]
        else:
            return df

    def get_logical_condition(self, df, field, value):
        """ Distributor which returns a logical condition for this filter 
        condition sent to pandas. """

        if field.type == 'choices':
            condition = self.get_choices_logical_condition(
                df, field, value)

        elif field.type == 'min_number':
            condition = self.get_minimum_number_logical_condition(
                df, field, int(value))

        elif field.type == 'max_number':
            condition = self.get_maximum_number_logical_condition(
                df, field, int(value))

        return condition

    def get_maximum_number_logical_condition(self, df, field, number):
        """ Return logical condition for maximum number case. """

        return df[field.data_file_field] <= number

    def get_minimum_number_logical_condition(self, df, field, number):
        """ Return logical condition for minimum number case. """

        return df[field.data_file_field] >= number

    def get_choices_logical_condition(self, df, field, choices):
        """ Return logical condition for choices case. """

        return df[field.data_file_field].isin(choices)

    def conjunction(self, conditions):
        """ Return conjunct logical conditions. """

        return functools.reduce(np.logical_and, conditions)



