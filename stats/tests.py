"""

Stuff to test (edge cases) what if first, last or dogs name are the same? 
what if blanks for a name or blanks in name? esp. when used for urls.
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
        
class OwnerModelTest(TestCase):
    def test_saving_and_rerieving_first_names(self):
        first_f_name = Owner()
        first_f_name.first_name = 'first first name'
        first_f_name.save()

        second_f_name = Owner()
        second_f_name.first_name = 'second first name'
        second_f_name.save()
        
        saved_names = Owner.objects.all()
        self.assertEqual(saved_names.count(), 2)
        
        first_saved_f_name = saved_names[0]
        second_saved_f_name = saved_names[1]
        self.assertEqual(first_saved_f_name.first_name, 'first first name')
        self.assertEqual(second_saved_f_name.first_name, 'second first name')

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

        new_name = Owner.objects.all()[0]
        print new_name
        self.assertEqual(new_name.last_name, 'last name')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/stats/the-only-owner/')
    
    def test_stats_view_displays_only_new_owner(self):
        owner = Owner.objects.create(first_name='name 1a',last_name='name 1b')
        Dog.objects.create(dog_name='name 1c', owner=owner)
        
        other_owner = Owner.objects.create(first_name='name 2a',last_name='name 2b')
        Dog.objects.create(dog_name='name 2c', owner=other_owner)

        client = Client()
        response = client.get('/stats/%d/' % (owner.id,))
        response.content()
       
        self.assertIn('name 1a', response.content)
        self.assertIn('name 1b', response.content)
        self.assertIn('name 1c', response.content)
        self.assertInNotIn('name 2a', response.content)
        self.assertInNotIn('name 2b', response.content)
        self.assertInNotIn('name 2c', response.content)
        self.assertTemplateUsed(response, 'new_owner.html')
        

#class StatsTestCase(TestCase):
#    def setUp(self):
#        Stats.objects.create(first_name="Susie", last_name="Doe", dog_name="rover")
#        Stats.ojbects.create(first_name="John", last_name="Roe", dog_name="spot")
#    
#    def test_

