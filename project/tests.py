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

class ProjectTestClass(TestCase):
    def setUp(self):
        self.edwin = Profile(user = 'edwin',bio='hello')
        self.edwin.save_profile()

       

    def tearDown(self):
        Projects.objects.all().delete()
        
        Projects.objects.all().delete()    

    def test_projects(self):
        posts = Projects.posts()
        self.assertTrue(len(posts)>0)     

class RatesTestClass(TestCase):
    def setUp(self):
        self.user = Profile
        self.rate = Rates(design=10,usability=10,content=10,user=self.user,project=10)
        self.rate.save()
        
        self.assertTrue(isinstance(self.rate,Rates))                   