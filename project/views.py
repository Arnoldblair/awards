from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import Profile,Projects,Rates
from django.http import Http404
from .forms import ProfileEditForm,ProjectUploadForm,VotesForm
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .permissions import IsAdminOrReadOnly
from .serializer import ProfileSerializer,ProjectsSerializer

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

def search_results(request):
    if 'titles' in request.GET and request.GET['titles']:
        search_term = request.GET.get("titles")
        searched_projects = Projects.search_by_projects(search_term)
        
        message = f'{search_term}'
        
        return render(request,'search.html',{"message":message,"projects":searched_projects})
    
    else:
        message = "You haven't searched for any term" 
        search_term = request.GET.get("titles")
        searched_projects = Projects.search_by_projects(search_term)

        return render(request,'search.html',{"message":message})   

class ProfileList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        all_profiles = Profile.objects.all()
        serializers = ProfileSerializer(all_profiles,many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

class ProjectsList(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get(self,request,format=None):
        all_projects = Projects.objects.all()
        serializers = ProjectsSerializer(all_projects,many=True)
        return Response(serializers.data)
    
    def post(self, request, format=None):
        serializers = ProjectsSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)             