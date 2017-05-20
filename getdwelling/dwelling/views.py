
from django.views.generic import (
    TemplateView,
    FormView,
)

from .forms import AnalyzeInputForm

#FIXME
from django.http import HttpResponse


class IndexView(TemplateView):
    """ Home page view for the website. """

    template_name = 'dwelling/index.html'


class DataSourceView(TemplateView):
    """ Data source view for the website. """

    template_name = 'dwelling/data_source.html'


class DataAnalyzeView(FormView):
    form_class = AnalyzeInputForm
    template_name = 'dwelling/data_analyze.html'


