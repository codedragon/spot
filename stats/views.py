from django.shortcuts import render
#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
#from django.views import generic

#from stats.models import Owner,Dog

def home_page(request):
    return render(request, 'home.html', {
            'new_first_text': request.POST.get('first_text', ''),
            'new_last_text': request.POST.get('last_text', ''),
            'new_dog_text': request.POST.get('dog_text', ''),
            })

#class ListView(generic.ListView):
#    template_name = 'stats/index.html'
#    context_ojbect_name = 'latest_stats_list'
#        
#    def get_queryset(self):
#        """Return the all owners and dogs."""
#        return Stats.objects.order_by('owner')
#
#class DetailView(generic.DetailView):
#    model = Owner
#    template_name = 'stats/detail.html'

