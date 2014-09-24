from tastypie.resources import ModelResource

from .models import Feature, Scenario

class FeatureResource(ModelResource):
    class Meta:
        queryset = Feature.objects.all()
        resource_name = 'feature'

    def dehydrate(self, bundle):
        bundle.data['script'] = bundle.obj.get_script()
        return bundle

class ScenarioResource(ModelResource):
    class Meta:
        queryset = Scenario.objects.all()
        resource_name = 'scenario'

    def dehydrate(self, bundle):
        bundle.data['script'] = bundle.obj.get_script()
        return bundle


