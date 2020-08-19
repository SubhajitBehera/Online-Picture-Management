from django.db import models

class AdminModel(models.Model):
    admin_name=models.CharField(primary_key=True,max_length=50)
    email=models.CharField(max_length=60)
    cno=models.IntegerField()
    password=models.CharField(max_length=40)


class UserModel(models.Model):
    id=models.AutoField(primary_key=True)
    username=models.CharField(max_length=50)
    email=models.CharField(unique=True,max_length=40)
    contactno=models.IntegerField(unique=True)
    ps=models.CharField(max_length=20)
    gender=models.CharField(max_length=10)

class PhotosModel(models.Model):
    #username=models.ForeignKey(UserModel,on_delete=models.CASCADE,primary_key=True)
    photo = models.FileField(upload_to='photos/')
    captions = models.TextField()
    videos=models.FileField(upload_to='videos/',null=True,verbose_name="")
    text=models.TextField()





