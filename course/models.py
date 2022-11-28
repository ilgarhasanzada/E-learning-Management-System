from django.db import models

from account.models import Parent, Student, Teacher

from main import settings

class Subject(models.Model):
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
    name = models.CharField(max_length=100)
    class_name=models.CharField(max_length=100,choices=class_categories)
    group=models.CharField(max_length=1)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='subjects')
    students=models.ManyToManyField(Student,blank=True,related_name="subjects")
    def __str__(self) -> str:
        return f'{self.class_name} { self.group}, {self.name}, {self.teacher.user.first_name} {self.teacher.user.last_name}'

class SubjectRegister(models.Model):
    parent=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='parent_course_registers')
    student=models.ForeignKey(Student,on_delete=models.CASCADE,related_name='student_course_registers')
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE,related_name='course_registers')
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,related_name='teacher_requests')
    is_accepted=models.BooleanField(default=False)
    def __str__(self) -> str:
        return f'Register to {self.subject}'
    
class Message(models.Model):
    text=models.TextField(null=True,blank=True)
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE,null=True,blank=True,related_name="messages")
    message_owner=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name="messages")
    image=models.ImageField(upload_to='messages/images',null=True,blank=True)
    file=models.FileField(upload_to='messages/files',null=True,blank=True)
    created_time=models.DateTimeField(auto_now_add=True)
    updated_time=models.DateTimeField(auto_now=True)
    def __str__(self) -> str:
        return f'{self.message_owner} -- {self.subject}'