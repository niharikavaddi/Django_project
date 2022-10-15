from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# This function adds and retrieves data
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            fm = StudentRegistration()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'CrudApp/addandshow.html', {'form': fm, 'stu': stud})


# This function deletes data
def delete_student(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        data.delete()
        return HttpResponseRedirect('/')


def update_student(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=data)
        if fm.is_valid():
            fm.save()
    else:
        data = User.objects.get(pk=id)
        fm = StudentRegistration(instance=data)
    return render(request, 'CrudApp/updatestudent.html', {'form': fm})
