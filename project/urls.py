from django.conf.urls import url

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    #url('^$',views.welcome,name = 'welcome'),
    url('^$',views.home,name='home'),
    url(r'^profile/(?P<username>\w+)', views.profile, name='profile'),
    url('^uploads/',views.post_site,name='post_site'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^api/profiles/$', views.ProfileList.as_view(),name='profile_list'),
    url(r'^api/projects/$', views.ProjectsList.as_view(),name='projects_list'),
    url(r'^projects/(\d+)',views.projects,name='projects'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)