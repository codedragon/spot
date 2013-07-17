from django.shortcuts import redirect, render
from stats.models import Owner, Dog
from .forms import UploadFileImage

#from django.shortcuts import get_object_or_404, render
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
#from django.views import generic

#from stats.models import Owner,Dog

def home_page(request):
    return render(request, 'home.html')

def view_owners(request):
    owners = Owner.objects.all()
    dogs = Dog.objects.all()
    return render(request, 'index.html', {'owner': owners,
                                          'dog': dogs})

def post_owner(request):
    owner = Owner.objects.create(first_name=request.POST['first_name'], 
                                 last_name=request.POST['last_name'])
    dog = Dog.objects.create(dog_name=request.POST['dog_name'], owner=owner)
    
    return redirect('/stats/%d/new_photo' % (owner.id,))
    #return redirect('/stats/%d/' % (owner.id,))

def update_owner(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    dog = Dog.objects.get(owner=owner)

    return render(request, 'update_owner.html', {'owner': owner,
                                                 'dog': dog,
                                                 })

def add_photo(request, owner_id):
    owner = Owner.objects.get(id=owner_id)
    dog = Dog.objects.get(owner=owner) 

    if request.method == 'POST':
        form = UploadFileImage(request.POST, request.FILES)
        if form.is_valid():
            dog.photo = form.cleaned_data['photo']
            #dog.photo = request.FILES['photo']
            dog.save()
            #dog.photo.save(request.FILES['photo'])
            #dog.photo = request.FILES['photo']
            return redirect('/stats/%d/' % (owner.id,))

    return render(request, 'update_owner.html', {'owner': owner,
                                                     'dog': dog,
                                                     })
    
    #dog.photo = request.POST.get('photo')
    #dog.photo.save()
    #dog.photo=request.POST['photo']
    #except (KeyError, Dog.DoesNotExist):
    #    return render(request, 'home.html', {
    #                  'error_message': "You need to enter your dog's name."})

    #return redirect('/stats/%d/' % (owner.id,))

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




