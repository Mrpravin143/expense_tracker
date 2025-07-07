from django.db import models

# Create your models here.


class Parents(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    gender = models.CharField(max_length=30)
    age = models.IntegerField()


class Childs(models.Model):
    name_of_chlid = models.CharField(max_length=100)
    age_of_child = models.IntegerField(default=18)
    branch = models.CharField(max_length=100,default="Computer Science")
    parent = models.ForeignKey(Parents,on_delete=models.CASCADE,null=True,blank=True)

