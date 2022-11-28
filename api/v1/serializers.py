from rest_framework import serializers
from account.models import Parent, Student, Teacher
from django.contrib.auth import get_user_model

from course.models import Message, Subject, SubjectRegister
User=get_user_model()
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=("id","first_name","last_name","username","email","age")
class ParentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Parent
        fields="__all__"

class TeacherSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Teacher
        fields="__all__"        
class StudentSerializer(serializers.ModelSerializer):
    user=UserSerializer()
    class Meta:
        model=Student
        fields="__all__"

class MessageSerializer(serializers.ModelSerializer):
    message_owner=serializers.StringRelatedField()
    subject=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Message
        fields="__all__"
        # write_only_fields=['subject',]

class SubjectSerializer(serializers.ModelSerializer):
    teacher=TeacherSerializer(read_only=True)
    students=StudentSerializer(many=True,read_only=True)
    class Meta:
        model=Subject
        fields="__all__"
#Valideyn ucun
        
class SubjectRegisterRequestSerializer(serializers.ModelSerializer):
    parent=UserSerializer(read_only=True)
    is_accepted=serializers.BooleanField(read_only=True)
    class Meta:
        model=SubjectRegister
        fields="__all__"
        
#Muellim ucun


class SubjectRegisterAcceptSerializer(serializers.ModelSerializer):
    student=StudentSerializer(read_only=True)
    parent=UserSerializer(read_only=True)
    course=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=SubjectRegister
        exclude=['teacher','subject']

class TeacherSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=SubjectRegister
        fields="__all__"



#Chats in subjects




class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(required=True,write_only=True)
    password2=serializers.CharField(required=True,write_only=True)
    class Meta:
        model=User
        fields=("username","email","first_name","last_name","password","password2","is_student","is_teacher","is_parent","age")
    
    def create(self, validated_data):
        username=validated_data.get('username')
        email=validated_data.get('email')
        last_name=validated_data.get('last_name')
        first_name=validated_data.get('first_name')
        password=validated_data.get('password')
        password2=validated_data.get('password2')
        is_student=validated_data.get('is_student')
        is_parent=validated_data.get('is_parent')
        is_teacher=validated_data.get('is_teacher')
        age=validated_data.get('age')
        if password==password2:
            user=User(username=username,email=email,first_name=first_name,last_name=last_name,is_teacher=is_teacher,is_student=is_student,is_parent=is_parent,age=age)
            user.set_password(password)
            user.save()
            return user
        else:
            return serializers.ValidationError({
                "error":"both password do not match"
            })