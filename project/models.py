from django.db import models
from django.db.models.signals import post_save
from django.core.validators import MaxValueValidator
from django.dispatch import receiver
from django.contrib.auth.models import User 
from tinymce.models import HTMLField
from url_or_relative_url_field.fields import URLOrRelativeURLField
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    profile_photo = CloudinaryField('image')
    bio = HTMLField(max_length=500,default='Your description')
    website = URLOrRelativeURLField() 
    phone_number = models.CharField(max_length=10,default='00000')