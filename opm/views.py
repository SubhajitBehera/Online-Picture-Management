from django.shortcuts import render,redirect
from opm.models import UserModel,PhotosModel
from django.db.utils import IntegrityError
from django.contrib import messages


def home(request):
    return render(request,'home.html')


def userlogin(request):
    return render(request,'userlogin.html')


def usersignup(request):
    return render(request,'user_signup.html')


def sign_in(request):
     name=request.POST.get("t1")
     email=request.POST.get("t2")
     contact=request.POST.get("t3")
     password=request.POST.get("t4")
     gender=request.POST.get("t6")

     UserModel(username=name,email=email,contactno=contact,ps=password,gender=gender).save()

     messages.success(request, "Thanks For Registration")

     return redirect('sign_in')


def login(request):
    un = request.POST.get("t1")
    pa = request.POST.get("t2")
    try:
        UserModel.objects.get(username=un, ps=pa)
        return render(request, "student_home.html", {"name": un,"password":pa})
    except UserModel.DoesNotExist:
        messages.error(request, "Invalid User")
        return redirect('login')


def profile(request):
    return render(request,'view_profile.html',{"data":UserModel.objects.all()})


def userhome(request):
    return render(request,'student_home.html')


def logout(request):
    return redirect('main')


def contactus(request):
    return render(request,'contactus.html')


def uploadphoto(request):
    return render(request,'uploadimage.html')


def image_upload(request):
    photo=request.POST.get("s1")
    caption=request.POST.get("s2")
    PhotosModel(photo=photo,captions=caption).save()
    messages.success(request,'Photo uploaded')
    return redirect('uploadphoto')


def uploadvideo(request):
    return render(request,'uploadvideo.html')


def video_upload(request):
    video=request.POST.get("v1")
    text=request.POST.get("v2")
    PhotosModel(videos=video,text=text).save()
    messages.success(request,'Video is uploaded')
    return redirect('uploadvideo')


def viewall(request):
    return render(request,'viewall.html',{"data":PhotosModel.objects.all()})


def delete(request,pk):
    PhotosModel.objects.get(pk=pk).delete()
    return redirect('viewall')