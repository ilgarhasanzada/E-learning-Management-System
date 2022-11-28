from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from course.models import SubjectRegister

@receiver(post_save,sender=SubjectRegister)
def add_to_course(sender, instance, created, **kwargs):
    subject=instance.subject
    student=instance.student
    if instance.is_accepted:
        subject.students.add(student)
        subject.save()