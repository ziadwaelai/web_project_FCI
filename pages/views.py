from unittest import result
from django.shortcuts import render,redirect
from students.models import Students
from students.views import Students
from django.db.models import Q
from .forms import UpdateForm
# Create your views here.


def homePage(request):
    return render(request,'pages/home page.html')



def index(request):
    return render(request,'pages/index.html')



def addNewStudent(request):
    if request.method=='POST':
        firstName=request.POST['firstName']
        lastName=request.POST['lastName']
        email=request.POST['email']
        studentID=request.POST['studentID']
        mobileNumber=request.POST['mobileNumber']
        GPA=request.POST['GPA']
        level=request.POST['level']
        department=request.POST['department']
        dateOfBirth=request.POST['dateOfBirth']
        status=request.POST['status']
        gender=request.POST['gender']
        ins = Students(firstName=firstName,lastName=lastName,email=email,studentID=studentID,
                        mobileNumber=mobileNumber,GPA=GPA,level=level,department=department,
                        dateOfBirth=dateOfBirth,status=status,gender=gender)
        ins.save()
    return render(request,'pages/addNewStudent.html')





def assignDepartment(request, pk):
    stu = Students.objects.get(studentID=pk)
    form = UpdateForm(request.POST or None, instance=stu)
    if form.is_valid():
        form.save()
      #  messages.info(request,'Student Assign Department Successfully')
        return redirect('all_student_status')
    return render(request, 'pages/assign department.html', {'student': stu, 'form': form})


def editStudentDataPage(request,studentID):
    student=Students.objects.get(pk=studentID)
    return render(request,'pages/edit student data page.html',{'student':student})



def delete(request, pk):
    todo = Students.objects.get(studentID=pk)
    todo.delete()
    return redirect('all_student_status')



def allStudentStatus(request):
    if 'q' in request.GET:
        q = request.GET['q']
        # data = Data.objects.filter(last_nameicontains=q)
        multiple_q = Q(Q(firstName__icontains=q) |Q(lastName__icontains=q)| Q(studentID__icontains=q))
        data = Students.objects.filter(multiple_q)
    else:
        data = Students.objects.all()

    return render(request, 'pages/all student status.html', {'student_list': data})


