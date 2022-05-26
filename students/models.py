from secrets import choice
from tabnanny import verbose
from django.db import models

# Create your models here.

class Students(models.Model):
    x = [('Male','Male'),('Female','Female')]
    y = [('Active','Active'),('Inactive','Inactive')]
    firstName = models.CharField(max_length=100,verbose_name='First Name')
    lastName = models.CharField(max_length=100,verbose_name='Last Name')
    studentID = models.PositiveIntegerField(verbose_name='ID')
    level=models.SmallIntegerField()
    GPA = models.DecimalField(max_digits=3,decimal_places=2)
    dateOfBirth=models.DateField(default='NULL',verbose_name='Data of birth')
    department=models.CharField(max_length=2)
    email=models.EmailField(verbose_name='Email')
    mobileNumber=models.CharField(max_length=13,verbose_name='Mobile number')
    status=models.CharField(choices=y ,max_length=10,default='NULL')
    gender=models.CharField(choices=x ,max_length=10,default='NULL')

