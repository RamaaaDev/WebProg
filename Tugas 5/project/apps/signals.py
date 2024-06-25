from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import redirect  # Import redirect
from apps.models import AccountUser

@receiver(post_save, sender=AccountUser, dispatch_uid="nim")
def check_nim(sender, instance, created, **kwargs):
    if created:
        get_student_number = AccountUser.objects.filter(account_user_student_number=instance.account_user_student_number)
        get_email = User.objects.filter(username=instance.account_user_related_user)

        if get_student_number.exists() or get_email.exists():
            return HttpResponse('Data Exist')
    else:
        return redirect('apps:create-data-student')
