from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.views import generic
from rest_framework import viewsets
from .models import Feature, Scenario
from .serializers import FeatureSerializer, ScenarioSerializer


# Create your views here.
class IndexView(generic.ListView):
    model = Feature
    template_name = 'features/features_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Feature.objects.order_by('name')


class DetailView(generic.DetailView):
    model         = Feature
    template_name = 'features/feature_detail.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        feature = self.object
        context['script'] = feature.get_script()
        return context


class FeatureViewSet(viewsets.ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class ScenarioViewSet(viewsets.ModelViewSet):
    queryset = Scenario.objects.all()
    serializer_class = ScenarioSerializer
