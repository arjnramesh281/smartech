from django.db import models

# Create your models here.

class course(models.Model):
    c_id=models.CharField(max_length=20)
    C_name=models.CharField(max_length=100)
    dis=models.TextField()
    duration=models.IntegerField()
    course_fee=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    

class contact(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    message=models.TextField()