from django.contrib import admin
from django.forms import ModelForm
from suit.admin import SortableTabularInline
from editarea.editarea import EditArea

from .models import Feature, Scenario, Step

# Register your models here.


class StepInlineForm(ModelForm):
    class Meta:
        widgets = {
                'action': EditArea,
                'result': EditArea,
                }


class StepInline(SortableTabularInline):
    model = Step
    sortable = 'order'
    form = StepInlineForm
    extra = 0
    min_num = 1
    max_num = 20


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ScenarioAdmin(admin.ModelAdmin):
    inlines = [
            StepInline,
            ]

    class Media:
        js = ('/static/editarea/edit_area_loader.js', )


admin.site.register(Feature, FeatureAdmin)
admin.site.register(Scenario, ScenarioAdmin)
