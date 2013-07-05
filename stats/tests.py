"""

Stuff to test (edge cases) what if first, last or dogs name are the same? 

"""

from django.test import TestCase
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

    def test_home_page_can_save_a_POST_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['first_text','last_text','dog_text'] = ['first name',
                                                             'last name',
                                                             'dog name']
        
        #request.POST['first_name'] = 'first name'        
        
        response = home_page(request)

        #self.assertEqual(Owner.objects.all().count(), 1)
        new_name = Owner.objects.all()[0]
        print new_name.first_name
        #self. assertEqual(new_name.first_name, 'first name')

        self.assertIn('first name', response.content)

        self.assertIn('last_name', response.content)

        expected_html = render_to_string(
            'home.html',
            {'new_first_name': 'first name',
             'new_last_name': 'last name',
             'new_dog_name': 'dog name',
             })

        self.assertEqual(response.content, expected_html)
        #
        #self.assertIn('dog_name', response.content)
        #expected_html = render_to_string(
        #    'home.html',
        #    {'new_first_text': 'first_name',
        #     'new_last_text': 'last_name',
        #     'new_dog_text': 'dog_name'}
        #    )
        #self.assertEqual(response.content, expected_html)

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

#class StatsTestCase(TestCase):
#    def setUp(self):
#        Stats.objects.create(first_name="Susie", last_name="Doe", dog_name="rover")
#        Stats.ojbects.create(first_name="John", last_name="Roe", dog_name="spot")
#    
#    def test_

