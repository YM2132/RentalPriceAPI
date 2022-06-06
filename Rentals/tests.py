from django.test import TestCase
from .models import Rental

# Create your tests here.
class RentalTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.rental = Rental.objects.create(
            price_pw=300,
            price_pm=1200,
            location='123 Bumbahole street',
            property_type='2 bed flat',
            url='herro.com',
        )

    def test_rental_model(self):
        self.assertEqual(self.rental.price_pw, 300)
        self.assertEqual(self.rental.price_pm, 1200)
        self.assertEqual(self.rental.location, '123 Bumbahole street')
        self.assertEqual(str(self.rental), '2 bed flat')
        self.assertEqual(self.rental.url, 'herro.com')
