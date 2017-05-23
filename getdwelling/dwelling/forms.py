from django import forms
from collections import namedtuple

CENSUS_YEAR_CHOICES = (
    (
        '2002-2006',
        (
            ('2002-2006', '2002-2006'),
            (2002, '2002'),
            (2003, '2003'),
            (2004, '2004'),
            (2005, '2005'),
            (2006, '2006'),
        ),
    ),
    (
        '2007-2011',
        (
            ('2007-2011', '2007-2011'),
            (2007, '2007'),
            (2008, '2008'),
            (2009, '2009'),
            (2010, '2010'),
            (2011, '2011'),
        ),
    ),
    (
        '2012-2016',
        (
            ('2012-2016', '2012-2016'),
            (2012, '2012'),
            (2013, '2013'),
            (2014, '2014'),
            (2015, '2015'),
            (2016, '2016'),
        ),
    ),
)

CLUE_SMALL_AREA_CHOICES = (
    ('Carlton', 'Carlton'),
    ('Docklands', 'Docklands'),
    ('East Melbourne', 'East Melbourne'),
    ('Kensington', 'Kensington'),
    ('Melbourne (CBD)', 'Melbourne (CBD)'),
    ('Melbourne (Remainder)', 'Melbourne (Remainder)'),
    ('North Melbourne', 'North Melbourne'),
    ('Parkville', 'Parkville'),
    ('Port Melbourne', 'Port Melbourne'),
    ('South Yarra', 'South Yarra'),
    ('Southbank', 'Southbank'),
    ('West Melbourne (Industrial)', 'West Melbourne (Industrial)'),
    ('West Melbourne (Residential)', 'West Melbourne (Residential)'),
)

DWELLING_TYPE_CHOICES = (
        ('House/Townhouse', 'House/Townhouse'),
        ('Residential Apartments', 'Residential Apartments'),
        ('Student Apartments', 'Student Apartments'),
)

DIMENSION_CHOICES = (
    ('None', 'None'),
    ('Census year', 'Census Year'),
    ('CLUE small area', 'CLUE Small Area'),
    ('Dwelling type', 'Dwelling Type'),
    ('Street address', 'Street Address'),
    ('Dwelling number', 'Dwelling Number'),
)

AGG_CHOICES = (
    ('', 'Required'),
    ('Census year', 'Census Year'),
    ('Dwelling number', 'Dwelling Number'),
)


Filter_field = namedtuple('Filter_field', ['field', 'type', 'data_file_field'])


class AnalyzeInputForm(forms.Form):

    # Filter conditions
    census_year_range = forms.MultipleChoiceField(
        label="Census Year:",
        choices=CENSUS_YEAR_CHOICES,
        required=False,
    )
    clue_small_area = forms.MultipleChoiceField(
        label="CLUE Small Area:",
        choices=CLUE_SMALL_AREA_CHOICES,
        required=False,
    )
    dwelling_type = forms.MultipleChoiceField(
        label="Dwelling Type:",
        choices=DWELLING_TYPE_CHOICES,
        required=False,
    )
    dwelling_number_min = forms.IntegerField(
        min_value=1,
        required=False,
    )
    dwelling_number_max = forms.IntegerField(
        max_value=1000,
        required=False,
    )
    search_street_address = forms.CharField(
        required=False,
        label="Street Address Keyword:",
    )

    # Graph information.
    row = forms.ChoiceField(
        required=True,
        choices=DIMENSION_CHOICES,
    )
    column = forms.ChoiceField(
        required=True,
        choices=DIMENSION_CHOICES,
    )
    aggregation_field = forms.ChoiceField(
        required=True,
        choices=AGG_CHOICES,
        label="Aggregation Field",
    )

    aggregation_function = forms.ChoiceField(
        required=True,
        choices=(
            ('count', 'Count of Records'),
            ('sum', 'Sum'),
            ('max', 'Maximum'),
            ('min', 'Minimum'),
            ('mean', 'Average'),
            ('median', 'Median'),
            ('var', 'Variance'),
        ),
        label="Aggregation Method"
    )

    def __init__(self, *args, **kwargs):
        super(AnalyzeInputForm, self).__init__(*args, **kwargs)

        # NOTE: Define here if new filter fields get added.
        self.filter_fields = (
            Filter_field('census_year_range', 'choices', 'Census year'),
            Filter_field('clue_small_area', 'choices', 'CLUE small area'),
            Filter_field('dwelling_type', 'choices', 'Dwelling type'),
            Filter_field('dwelling_number_min', 'min_number', 'Dwelling number'),
            Filter_field('dwelling_number_max', 'max_number', 'Dwelling number'),
            Filter_field('search_street_address', 'contain', 'Street address')
        )
