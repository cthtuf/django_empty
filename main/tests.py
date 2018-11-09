from django.test import TestCase
from main.models import SomeModel

class SomeModelTestCase(TestCase):
	INSTANCE1_VALUE = 'SomeData'

	def setUp(self):
		SomeModel.objects.create(somefield=self.INSTANCE1_VALUE)

	def test_lower(self):
		instance1 = SomeModel.objects.get(somefield=self.INSTANCE1_VALUE)

		self.assertEqual(self.INSTANCE1_VALUE.lower(), instance1.to_lowercase())
