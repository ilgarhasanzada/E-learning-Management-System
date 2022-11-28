from rest_framework.generics import ListCreateAPIView,ListAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView
from django.contrib.auth import get_user_model
from api.v1.serializers import  MessageSerializer, SubjectRegisterAcceptSerializer, SubjectRegisterRequestSerializer, SubjectSerializer,StudentSerializer
from account.models import Teacher,Student

from course.models import Message, Subject, SubjectRegister
from . import permissions as my_permissions
from rest_framework.generics import get_object_or_404
User=get_user_model()

#Valideyn muellime request atmasi ucun
class SubjectRegisterRequestListCreateAPIView(ListCreateAPIView):
    serializer_class=SubjectRegisterRequestSerializer
    permission_classes=[my_permissions.IsParent]
    def get_queryset(self):
        return SubjectRegister.objects.filter(parent=self.request.user)
    def perform_create(self, serializer):
        parent=self.request.user
        serializer.save(parent=parent)

class SubjectRegisterRequestDetailAPIView(RetrieveDestroyAPIView):
    serializer_class=SubjectRegisterRequestSerializer
    permission_classes=[my_permissions.IsParent]
    def get_queryset(self):
        return SubjectRegister.objects.filter(parent=self.request.user)
    
#Valideynin usaqlari

class ParentChilds(ListAPIView):
    serializer_class=StudentSerializer
    permission_classes=[my_permissions.IsParent]

    def get_queryset(self):
        return Student.objects.filter(parents=self.request.user)

class ParentChildsDetail(RetrieveAPIView):
    serializer_class=StudentSerializer
    permission_classes=[my_permissions.IsParent]

    def get_queryset(self):
        return Student.objects.filter(parents=self.request.user)

#Muellime gelen requestler

class TeacherSubjectRegisterListAPIView(ListAPIView):
    serializer_class=SubjectRegisterAcceptSerializer
    permission_classes=[my_permissions.IsTeacher]
    def get_queryset(self):
        teacher=get_object_or_404(Teacher,user=self.request.user)
        return SubjectRegister.objects.filter(teacher=teacher)

class TeacherSubjectRegisterDetailAPIView(RetrieveUpdateAPIView):
    serializer_class=SubjectRegisterAcceptSerializer
    permission_classes=[my_permissions.isRequestTeacher]
    def get_queryset(self):
        teacher=get_object_or_404(Teacher,user=self.request.user)
        return SubjectRegister.objects.filter(teacher=teacher)
#Muellimin kurslari


class TeacherSubjectListCreateAPIView(ListCreateAPIView):
    serializer_class=SubjectSerializer
    permission_classes=[my_permissions.IsTeacher]
    def get_queryset(self):
        teacher=get_object_or_404(Teacher,user=self.request.user)
        return Subject.objects.filter(teacher=teacher)
    def perform_create(self, serializer):
        teacher=get_object_or_404(Teacher,user=self.request.user)
        serializer.save(teacher=teacher)

class TeacherSubjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class=SubjectSerializer
    permission_classes=[my_permissions.IsTeacher]

    def get_queryset(self):
        teacher=get_object_or_404(Teacher,user=self.request.user)
        return Subject.objects.filter(teacher=teacher)
  

#Sagirdin kurslari
class StudentSubjectListAPIView(ListAPIView):
    serializer_class=SubjectSerializer
    def get_queryset(self):
        student=Student.objects.get(user=self.request.user)
        return Subject.objects.filter(students=student)

class StudentSubjectDetailAPIView(RetrieveAPIView):
    serializer_class=SubjectSerializer
    def get_queryset(self):
        student=Student.objects.get(user=self.request.user)
        return Subject.objects.filter(students=student)

#Chat in Subject

class MessageListCreateAPIView(ListCreateAPIView):
    serializer_class=MessageSerializer
    permission_classes=[my_permissions.IsSubjectTeacherOrIsSubjectStudent]
    def get_queryset(self):
        subject=get_object_or_404(Subject)
        return Message.objects.filter(subject=subject)
    def perform_create(self, serializer):
        subject=get_object_or_404(Subject)
        serializer.save(subject=subject,message_owner=self.request.user)

