"""

Stuff to test (edge cases) what if first, last or dogs name are the same? 
what if blanks for a name or blanks in name? esp. when used for urls.
more than one dog?
"""

from django.test import TestCase, Client
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string

from stats.views import home_page
from stats.models import Owner
from stats.models import Dog

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        self.assertEqual(response.content, expected_html)

    def test_home_page_only_saves_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Owner.objects.all().count(), 0)
        self.assertEqual(Dog.objects.all().count(), 0)
        
class OwnerAndDogModelsTest(TestCase):
    def test_saving_and_rerieving_first_names(self):
        first_owner = Owner()
        first_owner.first_name = 'first owner'
        first_owner.save()
        
        first_dog = Dog()
        first_dog.dog_name = 'first dog'
        first_dog.owner = first_owner
        first_dog.save()

        second_owner = Owner()
        second_owner.first_name = 'second owner'
        second_owner.save()
        
        second_dog = Dog()
        second_dog.dog_name = 'second dog'
        second_dog.owner = second_owner
        second_dog.save()

        saved_owners = Owner.objects.all()
        self.assertEqual(saved_owners.count(), 2)
        self.assertEqual(saved_owners[0], first_owner)
        saved_dogs = Dog.objects.all()
        self.assertEqual(saved_dogs.count(), 2)
        
        first_saved_owner = saved_owners[0]
        second_saved_owner = saved_owners[1]
        first_saved_dog = saved_dogs[0]
        second_saved_dog = saved_dogs[1]

        self.assertEqual(first_saved_owner.first_name, 'first owner')
        self.assertEqual(second_saved_owner.first_name, 'second owner')
        self.assertEqual(first_saved_dog.dog_name, 'first dog')
        self.assertEqual(second_saved_dog.dog_name, 'second dog')

    def test_saving_photo_to_Dog(self):
        owner = Owner()
        owner.first_name = 'jane'
        owner.last_name = 'doe'
        owner.save()
        dog = Dog()
        dog.dog_name = 'fido'
        dog.owner = owner
        dog.save()
        self.assertEqual(bool(dog.photo), False)
        f = open('/Users/maria/Desktop/sebastian.JPG')
        try:
            dog.photo = f
        finally:
            f.close()
            
        self.assertEqual(bool(dog.photo), True)

    def test_thumbnail_created_in_Dog(self):
        pass

# Don't care about this class yet, just get new stats working for next bit of FT
#class StatsIndexTest(TestCase):
#
#    def test_stats_view_displays_all_owners(self):
#        owner = Owner.objects.create(first_name='name 1',last_name='name 2')
#        Dog.objects.create(dog_name='name 3', owner=owner)
#        
#        client = Client()
#        response = client.get('/stats/the-only-owner/')
#
#        self.assertIn('name 1', response.content)
#        self.assertIn('name 2', response.content)
#        self.assertIn('name 3', response.content)
#        self.assertTemplateUsed(response, 'index.html')

class NewStatsTest(TestCase):
    
    def test_saving_a_POST_request(self):
        client = Client()
        response = client.post(
            '/stats/new',
            data = {'first_name': 'first name',
                    'last_name': 'last name',
                    'dog_name': 'dog name'}
            )

        self.assertEqual(Owner.objects.all().count(), 1)
        new_owner = Owner.objects.all()[0]
        self.assertEqual(Dog.objects.all().count(), 1)
        new_dog = Dog.objects.all()[0]
        self.assertEqual(new_owner.last_name, 'last name')
        self.assertEqual(new_dog.dog_name, 'dog name')

        self.assertRedirects(response,'/stats/%d/' % (new_owner.id,))
    
    def test_stats_view_displays_only_new_owner(self):
        owner = Owner.objects.create(first_name='name 1a',last_name='name 1b')
        dog = Dog.objects.create(dog_name='name 1c', owner=owner)

        self.assertEqual(owner.last_name, 'name 1b')
        self.assertEqual(dog.dog_name, 'name 1c')

        other_owner = Owner.objects.create(first_name='name 2a',last_name='name 2b')
        Dog.objects.create(dog_name='name 2c', owner=other_owner)

        client = Client()
        print owner.id
        response = client.get('/stats/%d/' % (owner.id,))
        
        self.assertTemplateUsed(response, 'new_owner.html')       
        
        self.assertIn('name 1a', response.content)
        self.assertIn('name 1b', response.content)
        self.assertIn('name 1c', response.content)
        self.assertNotIn('name 2a', response.content)
        self.assertNotIn('name 2b', response.content)
        self.assertNotIn('name 2c', response.content)

    def test_stats_view_uploads_a_file(self):
        try:
            f = open('/Users/maria/Desktop/sebastian.JPG')
            postdata = {'datatype': 'photo','datafile':f}
        
            client = Client()
            response= client.post('/stats/%d/', postdata)
            self.failUnlessEqual(response.status_code, 200)
        finally:
            f.close()

#class StatsTestCase(TestCase):
#    def setUp(self):
#        Stats.objects.create(first_name="Susie", last_name="Doe", dog_name="rover")
#        Stats.ojbects.create(first_name="John", last_name="Roe", dog_name="spot")
#    
#    def test_

