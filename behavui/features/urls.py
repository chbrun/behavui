from django.conf.urls import patterns, url, include
from tastypie.api import Api

from . import views
from .api import FeatureResource, ScenarioResource

v1_api = Api(api_name="v1")
v1_api.register(FeatureResource())
v1_api.register(ScenarioResource())

urlpatterns = patterns('',
        url(r'^$', views.IndexView.as_view(), name='features_list'),
        url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='feature_detail'),
        url(r'^api/', include(v1_api.urls)),
        )
