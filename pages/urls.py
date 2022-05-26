from django.urls import path

from . import views

urlpatterns =[
    path('',views.homePage,name='home_page'),
    path('index',views.index,name='index'),
    path('add_student',views.addNewStudent,name='add_student'),
    path('all_student_status',views.allStudentStatus,name='all_student_status'),
    path('edit_student_data/<studentID>',views.editStudentDataPage,name='edit_student_data'),
    path('delete/<int:pk>',views.delete,name='delete'),
    path('assign_department/<int:pk>',views.assignDepartment,name='assign_department'),
]