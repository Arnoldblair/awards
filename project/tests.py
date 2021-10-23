from django.test import TestCase
from .models import Profile,Projects,Rates

# Create your tests here.

class ProfileTestClass(TestCase):
    def setUp(self):
        self.edwin = Profile( profile_photo='',bio='hello', website='www.1337x.to', phone_number='07000000')

    def test_instance(self):
        self.assertTrue(isinstance(self.edwin,Profile))

    def test_save(self):
        self.edwin.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)