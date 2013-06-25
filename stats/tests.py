"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.

Stuff to test (edge cases) what if first, last or dogs name are the same? 

"""

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

class StatsTestCase(TestCase):
    def setUp(self):
        Stats.objects.create(first_name="Susie", last_name="Doe", dog_name="rover")
        Stats.ojbects.create(first_name="John", last_name="Roe", dog_name="spot")
    
    def test_

