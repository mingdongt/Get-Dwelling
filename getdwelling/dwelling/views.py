
from django.views.generic import TemplateView

#FIXME
from django.http import HttpResponse


class IndexView(TemplateView):
    """ Index View for the website. """

    template_name = 'dwelling/index.html'


def DataSourceView(request):
    return HttpResponse("data source")


def DataAnalyzeView(request):
    return HttpResponse("data analyze")
