from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile,Projects,Rates,Comments

# Create your views here.
def welcome(request):
    return render(request, 'test.html')

def profile(request,username):
    profile = User.objects.get(username=username)
    
    try:
        profile_details = Profile.get_by_id(profile.id)
    except:
        profile_details = Profile.filter_by_id(profile.id)
    projects = Projects.get_profile_projects(profile.id)
    
    return render(request, 'users/profile.html',{"profile":profile,"profile_details":profile_details,"projects":projects}) 
