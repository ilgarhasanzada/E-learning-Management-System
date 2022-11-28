from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model

from account.models import Parent, Student, Teacher
User=get_user_model()
@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        if(instance.is_teacher):
            Teacher.objects.create(user=instance)
        elif(instance.is_student):
            Student.objects.create(user=instance)
        elif(instance.is_parent):
            Parent.objects.create(user=instance)