"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

Stuff to test (edge cases) what if first, last or dogs name are the same? 

"""

from django.test import TestCase
from django.core.urlresolvers import resolve
from stats.views import home_page

class HomePageTest(TestCase):
    def test_root_rul_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

#class StatsTestCase(TestCase):
#    def setUp(self):
#        Stats.objects.create(first_name="Susie", last_name="Doe", dog_name="rover")
#        Stats.ojbects.create(first_name="John", last_name="Roe", dog_name="spot")
#    
#    def test_

