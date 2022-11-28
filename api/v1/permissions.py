from rest_framework.permissions import SAFE_METHODS,BasePermission
from account.models import Student, Teacher
from course.models import Subject
from rest_framework.generics import get_object_or_404


class IsParent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return bool(request.user.is_parent)
        return False
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return request.user.is_teacher
        return False
class isRequestTeacher(BasePermission):
    def has_object_permission(self, request, view, obj):
        teacher=Teacher.objects.get(user=request.user)
        return obj.teacher==teacher

class IsSubjectTeacherOrIsSubjectStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_teacher:
                teacher=Teacher.objects.get(user=request.user)
                get_object_or_404(Subject,teacher=teacher)
                return True
            elif request.user.is_student:
                student=Student.objects.get(user=request.user)
                get_object_or_404(Subject,students=student)
                return True
        return False

class isRegister(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return False
        return True