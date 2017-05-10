
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """ Index View for the website. """

    template_name = 'dwelling/index.html'

#FIXME
from django.http import HttpResponse


def DataSourceView(request):
    return HttpResponse("data source")

def DataAnalyzeView(request):
    return HttpResponse("data analyze")
