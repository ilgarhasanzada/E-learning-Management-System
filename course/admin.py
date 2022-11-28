from django.contrib import admin

from course.models import Message, Subject,SubjectRegister
# Register your models here.

admin.site.register(Subject)
admin.site.register(SubjectRegister)
admin.site.register(Message)
