from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from stats.models import Owner,Dog

class ListView(generic.ListView):
    template_name = 'stats/index.html'
    context_ojbect_name = 'latest_stats_list'
        
    def get_queryset(self):
        """Return the all owners and dogs."""
        return Stats.objects.order_by('owner')

class DetailView(generic.DetailView):
    model = Owner
    template_name = 'stats/detail.html'

