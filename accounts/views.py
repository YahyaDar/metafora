from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterFormFaculty, RegisterFormStudent
from django.http import HttpResponse


def login_user(request):
    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, "There Was An Error Logging In, Try Again...")
            return redirect('login')

    else:
        return render(request, 'registration/login.html', {})


def logout_user(request):
    logout(request)
    messages.success(request, "You Were Logged Out!")
    return redirect('index')  # TODO: Update after creating views in Register app


def register_faculty(request):
    if request.method == "POST":
        form = RegisterFormFaculty(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('index')
    else:
        form = RegisterFormFaculty()

    return render(request, 'registration/register_faculty.html', {
        'form': form,
        })


def register_student(request):
    if request.method == "POST":
        form = RegisterFormStudent(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Registration Successful!")
            return redirect('index')
    else:
        form = RegisterFormStudent()

    return render(request, 'registration/register_student.html', {
        'form': form,
        })


def index(request):
    return HttpResponse("Hello World")
