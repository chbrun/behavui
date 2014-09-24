from django.conf.urls import patterns, url, include
from tastypie.api import Api

from . import views
#from .api import ProjectResource

v1_api = Api(api_name="v1")
#v1_api.register(ProjectResource())

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='campaigns_list'),
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='campaign_detail'),
        url(r'^api/', include(v1_api.urls)),
        )
