from django.urls import path
from . import views

urlpatterns = [

    #Parent Panel
    path('parent/childs',views.ParentChilds.as_view()),
    path('parent/childs/<int:pk>',views.ParentChildsDetail.as_view()),
    
    path('parent/subject-register',views.SubjectRegisterRequestListCreateAPIView.as_view()),
    path('parent/subject-register/<int:pk>',views.SubjectRegisterRequestDetailAPIView.as_view()),


    #Teacher Panel
    path('teacher/subjects',views.TeacherSubjectListCreateAPIView.as_view()),
    path('teacher/subjects/<int:pk>',views.TeacherSubjectDetailAPIView.as_view()),
    
        #chat
    path('teacher/subjects/<int:pk>/messages',views.MessageListCreateAPIView.as_view()),

    
    path('teacher/subject-requests',views.TeacherSubjectRegisterListAPIView.as_view()),
    path('teacher/subject-requests/<int:pk>',views.TeacherSubjectRegisterDetailAPIView.as_view()),

    #Student Panel
    path('student/subjects',views.StudentSubjectListAPIView.as_view()),
    path('student/subjects/<int:pk>',views.StudentSubjectDetailAPIView.as_view()),
        
        #chat
    path('student/subjects/<int:pk>/messages',views.MessageListCreateAPIView.as_view()),


]