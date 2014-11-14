from django.conf.urls import patterns, url, include
from .views import FeatureViewSet, ScenarioViewSet
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'feature', FeatureViewSet)
router.register(r'scenario', ScenarioViewSet)

urlpatterns = patterns(
    '',
    url(r'^$', views.IndexView.as_view(), name='features_list'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='feature_detail'),
    url(r'^api/', include(router.urls)),
)
