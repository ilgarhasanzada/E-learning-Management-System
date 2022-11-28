from django.db import models
from main import settings
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  age=models.PositiveIntegerField(null=True, blank=True)
  is_teacher = models.BooleanField(default=False)
  is_student = models.BooleanField(default=False)
  is_parent = models.BooleanField(default=False)


class Teacher(models.Model):
    user = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,related_name="teacher")
    def __str__(self):
        return self.user.username

class Parent(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE,related_name="parent")
    def __str__(self):
        return self.user.username

class Student(models.Model):
    class_categories=[
        ('1',1),
        ('2',2),
        ('3',3),
        ('4',4),
        ('5',5),
        ('6',6),
        ('7',7),
        ('8',8),
        ('9',9),
        ('10',10),
        ('11',11),
    ]
    class_name=models.CharField(max_length=100,choices=class_categories,verbose_name='class')
    user = models.OneToOneField(
      settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True,related_name='student')
    parents=models.ManyToManyField(settings.AUTH_USER_MODEL,blank=True,related_name='students')

    def __str__(self):
        return self.user.username


