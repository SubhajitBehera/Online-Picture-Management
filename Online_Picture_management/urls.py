"""Online_Picture_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from Online_Picture_management import settings

from opm import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='main'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('usersign_up/',views.usersignup,name='usersinn_up'),
    path('sign_in/',views.sign_in,name='sign_in'),
    path('login/',views.login,name='login'),
    path('profile/',views.profile,name='profile'),
    path('userhome/',views.userhome,name='userhome'),
    path('logout/',views.logout,name='logout'),
    path('contactus/',views.contactus,name='contactus'),
    path('uploadphoto/',views.uploadphoto,name='uploadphoto'),
    path('image_upload/',views.image_upload,name='image_upload'),
    path('uploadvideo/',views.uploadvideo,name='uploadvideo'),
    path('video_upload/',views.video_upload,name='video_upload'),
    path('videos/',views.viewall,name='viewall'),
    path('delete/<int:pk>',views.delete,name='delete')
 ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
