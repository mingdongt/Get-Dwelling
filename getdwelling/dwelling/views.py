
from django.views.generic import TemplateView

#FIXME
from django.http import HttpResponse


class IndexView(TemplateView):
    """ Index View for the website. """

    template_name = 'dwelling/index.html'


class DataSourceView(TemplateView):
    template_name = 'dwelling/data_source.html'


def DataAnalyzeView(request):
    return HttpResponse("data analyze")
