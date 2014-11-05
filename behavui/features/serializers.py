from .models import Feature, Scenario
from rest_framework import serializers

class FeatureSerializer(serializers.ModelSerializer):
    script = serializers.SerializerMethodField('get_script')

    class Meta:
        model = Feature

    def get_script(self, obj):
        return obj.get_script() 

class ScenarioSerializer(serializers.ModelSerializer):
    script = serializers.SerializerMethodField('get_script')

    class Meta:
        model = Scenario

    def get_script(self, obj):
        return obj.get_script() 
