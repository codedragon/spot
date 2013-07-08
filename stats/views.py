from django.shortcuts import redirect, render
from stats.models import Owner, Dog

#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
#from django.views import generic

#from stats.models import Owner,Dog

def home_page(request):
    #if request.method == 'POST':
    #    owner = Owner.objects.create(first_name=request.POST['first_name'], 
    #                                 last_name=request.POST['last_name'])
    #    dog = Dog.objects.create(dog_name=request.POST['dog_name'], owner=owner)
    #    return redirect('/')
    return render(request, 'home.html')
    
    #owner = Owner.objects.create()
    #owner.first_name = request.POST.get('first_name', '')
    #owner.last_name = request.POST.get('last_name', '')
    #owner.save()

    #dog = Dog.objects.create(owner=owner)
    #dog.dog_name = request.POST.get('dog_name', '')
    #print owner.first_name
    #print owner.last_name
    #print dog.dog_name

    #dog.save()
    

def view_owners(request):
    owners = Owner.objects.all()
    dogs = Dog.objects.all()
    return render(request, 'index.html', {'owner': owners,
                                          'dog': dogs})

    #return render(request, 'home.html', {'new_first_name': owners.first_name,
    #                                     'new_last_name': owners.last_name,
    #                                     'new_dog_name': dogs.dog_name
    #                                     })
                                 

def new_owner(request):
    #owner = Owner.objects.create()
    owner = Owner.objects.create(first_name=request.POST['first_name'], 
                                 last_name=request.POST['last_name'])
    dog = Dog.objects.create(dog_name=request.POST['dog_name'], owner=owner)
    
    #return render(request, 'new_owner.html', {'new_first_name': owner.first_name,
    #                                          'new_last_name': owner.last_name,
    #                                          'new_dog_name': dog.dog_name,})
    
    return redirect('/stats/%d/' % (owner.id,))
    #return render(request, 'home.html', {
    #        'new_first_name': owner.first_name,
    #        'new_last_name': owner.last_name,
    #        'new_dog_name': dog.dog_name,
    #        })

def temp_owner(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    dog = Dog.objects.get(owner=owner)

    #return render(request, 'new_owner.html',{'first_name':owner_names.first_name,
    #                                         'last_name':owner_names.last_name,
    #                                         'dog_name':dog.dog_name,})

    return render(request, 'new_owner.html', {'owner': owner,
                                              'dog': dog})


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




