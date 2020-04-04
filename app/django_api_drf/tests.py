from django.test import TestCase
from django_api_drf.calc import add, substract


class CalcTests(TestCase):
    def test_add_numbers(self):
        """Test that two numbers that are added together"""
        self.assertEqual(add(3,8),11)

    def test_substract_numbers(self):
        """ Test that values that are substracted and returned """
        self.assertEqual(substract(5, 11),6)
