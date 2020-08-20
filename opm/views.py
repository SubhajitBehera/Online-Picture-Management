from django.shortcuts import render,redirect
from opm.models import UserModel,PhotosModel,AdminModel
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
    photo=request.FILES["s1"]
    caption=request.POST.get("s2")
    PhotosModel(photo=photo,captions=caption).save()
    messages.success(request,'Photo uploaded')
    return redirect('uploadphoto')


def uploadvideo(request):
    return render(request,'uploadvideo.html')


def video_upload(request):
    video=request.FILES["v1"]
    text=request.POST.get("v2")
    PhotosModel(videos=video,text=text).save()
    messages.success(request,'Video is uploaded')
    return redirect('uploadvideo')


def viewall(request):
    return render(request,'viewall.html',{"data":PhotosModel.objects.all()})


def delete(request,id):
    PhotosModel.objects.get(id=id).delete()
    return redirect('viewall')


def edit(request,id):
    image =PhotosModel.objects.get(id=id)
    return render(request,'edit.html',{"edit":image})


def edit_all(request):
    e_photo=request.FILES["i1"]
    e_caption=request.POST.get("i2")
    e_video=request.FILES["i3"]
    e_text=request.POST.get("i4")
    PhotosModel(photo=e_photo,captions=e_caption,videos=e_video,text=e_text).save()

    return redirect('edit')


def adminlogin(request):
    return render(request,'adminregister.html')


def register(request):
    admin=request.POST.get('a1')
    a_email=request.POST.get('a2')
    cnumber=request.POST.get('a3')
    password=request.POST.get('a4')
    AdminModel(admin_name=admin,email=a_email,cno=cnumber,password=password).save()
    messages.success(request,'Admin Register Succesfully')
    return redirect('log')


def log(request):
    return render(request,'admin_open.html')


def view_all_user(request):
    return render(request,'view_all_user.html',{"data":UserModel.objects.all()})


def delete_user(request,id):
        PhotosModel.objects.get(id=id).delete()
        return redirect('view_all_user')


def view_photo_video(request):
    return render(request,"viewphoto_video.html",{"data":PhotosModel.objects.all()})