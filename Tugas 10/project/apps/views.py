from django.contrib import messages
from django.db.models.signals import post_save
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q
from django.contrib.auth.models import User
from apps.models import AccountUser
from apps.signals import check_nim
from apps.forms import StudentRegisterForm


# Create your views here.
def readStudent(request):
    data = AccountUser.objects.all()

    context = {'data_list': data}

    return render(request, 'index.html', context)


@csrf_protect
def createStudent(request):
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            post_save.disconnect(check_nim)
            form.fullname = form.cleaned_data.get("fullname")
            form.nim = form.cleaned_data.get("nim")
            form.email = form.cleaned_data.get("email")
            post_save.send(
                sender=AccountUser, created=None,                instance=form,                dispatch_uid="check_nim")
            messages.success(request, 'Data Berhasil disimpan')
            return redirect('apps:read-data-student')
    else:
        form = StudentRegisterForm()

    return render(request, 'forms.html', {'forms': form})


@csrf_protect
def updateStudent(request, id):
    form_update = AccountUser.objects.get(account_user_related_user=id)
    if request.method == 'POST':
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            form_update.account_user_fullname = form.cleaned_data.get("fullname")
            form_update.account_user_student_number = form.cleaned_data.get("nim")
            form_update.account_user_related_user = form.cleaned_data.get("email")
            form_update.account_user_updated_by = request.user.username
            form_update.save()
            messages.success(request, 'Data Berhasil diupdate')
            return redirect('apps:read-data-student')
    else:
        form = StudentRegisterForm(initial={
            'fullname': form_update.account_user_fullname,
            'nim': form_update.account_user_student_number,
            'email': form_update.account_user_related_user,
        })
    return render(request, 'forms.html', {'forms': form})



@csrf_protect
def deleteStudent(request, id):
    member = AccountUser.objects.get(account_user_related_user=id)
    user = User.objects.get(username=id)
    member.delete()
    user.delete()
    messages.success(request, 'Data Berhasil dihapus')
    return redirect('apps:read-data-student')