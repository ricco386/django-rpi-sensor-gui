from django.test import TestCase
from gui.models import Unit


class UnitTestCase(TestCase):
    def setUp(self):
        Unit.objects.create(name="temperature", variable="*C")

    def test_model_print(self):
        temp = Unit.objects.get(name="temperature")
        self.assertEqual(temp.name, 'temperature')
        self.assertEqual(temp.variable, '*C')
