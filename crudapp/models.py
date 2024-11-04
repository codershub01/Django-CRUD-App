from django.db import models

# Create your models here.

class Student(models.Model):
    fname = models.CharField(max_length=50,blank=False, null=False)
    lname = models.CharField(max_length=50,blank=False, null=False)
    email = models.EmailField(blank=False, null=False, unique=True)
    contact = models.IntegerField()
    city = models.CharField(max_length=50,blank=False, null=False)
    