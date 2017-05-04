
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """ Index View for the website. """

    template_name = 'dwelling/index.html'



