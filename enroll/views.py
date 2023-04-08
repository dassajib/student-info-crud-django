from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistratin
from .models import User

# Create your views here.
def add_show(request):
    if request.method == 'POST':
        form_model = StudentRegistratin(request.POST)
        if form_model.is_valid():
            name = form_model.cleaned_data['name']
            email = form_model.cleaned_data['email']
            password = form_model.cleaned_data['password']
            user_object = User(name=name, email=email, password=password)
            user_object.save()
            form_model = StudentRegistratin()

    else:
        form_model = StudentRegistratin()

    studentInfo = User.objects.all()

    return render(request, 'enroll/addandshow.html', {'form': form_model, 'studentInfo': studentInfo})


def update_data(request, id):
    if request.method == "POST":
        data = User.objects.get(pk=id)
        form_model = StudentRegistratin(request.POST, instance=data)
        if form_model.is_valid():
            form_model.save()

    else:
        data = User.objects.get(pk=id)
        form_model = StudentRegistratin(instance=data)
    return render(request, 'enroll/update.html', {'form':form_model})

def delete_data(request, id):
    if request.method == 'POST':
        data = User.objects.get(pk=id)
        data.delete() 
        return HttpResponseRedirect('/')