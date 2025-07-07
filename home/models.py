from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Brand(models.Model):
    brand_name=models.CharField(max_length=100)

class Colleges(models.Model):
    colleges_name=models.CharField(max_length=100)
    colleges_address=models.CharField(max_length=100)



class StudentData(models.Model):
    student_name=models.CharField(max_length=100)
    age=models.IntegerField(null=True,blank=True)
    gender=models.CharField(max_length=30)
    email=models.EmailField(null=True,blank=True)
    phone_number=models.CharField(max_length=200,null=True,blank=True)
    colleges_name = models.ForeignKey(Colleges,on_delete=models.CASCADE,null=True,blank=True)

class Login(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=40)


class AddProducts(models.Model):
    product_name=models.CharField(max_length=50)
    productID=models.CharField(max_length=30)


class Author(models.Model):
    author_name =models.CharField(max_length=100)


class Books(models.Model):
    book_name = models.CharField(max_length=100)
    book_price = models.DecimalField(max_digits = 5,decimal_places = 2)
    published_date = models.DateField()
    written = models.IntegerField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.book_name

class Product(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    category= models.CharField(max_length=200)
    price = models.FloatField()
    brand = models.CharField(max_length=150)
    sku = models.CharField(max_length=100)
    thumbnail = models.URLField(max_length=1000)


class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20,unique=True)
    otp = models.CharField(max_length=6,blank=True,null=True)

    def __str__(self):
        return f"{self.user.username}"


class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    













    
     







    

