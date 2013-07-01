"""

Stuff to test (edge cases) what if first, last or dogs name are the same? 

"""

from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from stats.views import home_page

class HomePageTest(TestCase):

    def test_root_rul_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith('<html>'))
        self.assertIn('<title>Spot Database</title>', response.content)
        self.assertTrue(response.content.endswith('</html>'))

#class StatsTestCase(TestCase):
#    def setUp(self):
#        Stats.objects.create(first_name="Susie", last_name="Doe", dog_name="rover")
#        Stats.ojbects.create(first_name="John", last_name="Roe", dog_name="spot")
#    
#    def test_

