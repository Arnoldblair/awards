from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Projects,Rates
from django.http import Http404
from .forms import ProfileEditForm,ProjectUploadForm,VotesForm

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

def home(request):
    projects = Projects.objects.all()
    print(f"projects:{projects}")
    # context = {
    #     'projects':project,
    # }
    return render(request,'home.html',{"projects":projects})

def post_site(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectUploadForm(request.POST, request.FILES)
        if form.is_valid():
            home = form.save(commit=False)
            home.profile =current_user
            form.save()
        return redirect('home')
    else:
        form =ProjectUploadForm()
            
    return render(request,'uploads.html',{"form":form,})    