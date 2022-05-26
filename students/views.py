from django.shortcuts import render
from .models import Students
# Create your views here.
def student(request):
    return render(request,'students/student.html')



def students(request):
    return render(request ,'students/students.html')


