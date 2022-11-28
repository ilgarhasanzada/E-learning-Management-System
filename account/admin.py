from django.contrib import admin

from account.models import CustomUser, Parent, Student, Teacher

# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Parent)
admin.site.register(Student)
admin.site.register(Teacher)


