from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^source', views.DataSourceView.as_view(), name='data_source'),
    url(r'^analyze$', views.DataAnalyzeView.as_view(), name='data_analyze'),
    url(r'^insights/(?P<order>[1-5]{1})$', views.InsightsView.as_view(), name='data_analyze'),
]
