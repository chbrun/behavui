from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from django.views import generic

from .models import Campaign

# Create your views here.
class IndexView(generic.ListView):
    model = Campaign
    template_name = 'campaign/campaigns_list.html'
    paginate_by = 10

    def get_queryset(self):
        return Campaign.objects.order_by('name')

class DetailView(generic.DetailView):
    model = Campaign
    template_name = 'campaign/campaign_detail.html'
