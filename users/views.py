from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Profile
from .forms import CustomRegistration, ProfileForm


def loginUser(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('projects')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        try:
            User.objects.get(username=username)
        except:
            messages.error(request, 'User not exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('projects')
        else:
            messages.error(request, 'Wrong credentials')

    return render(request, 'users/login_register.html')


def logoutUser(request):
    logout(request)
    messages.error(request, 'Logged out')
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomRegistration()

    if request.method == 'POST':
        form = CustomRegistration(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account Created')
            return redirect('projects')
        else:
            messages.error(request, 'ERROR')

    context = {'page': page, 'form': form}
    return render(request, 'users/login_register.html', context)


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user_profile.html', context)


@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()

    context = {'profile': profile, 'skills': skills, 'projects': projects}
    return render(request, 'users/account.html', context)


@login_required(login_url='login')
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()

            return redirect('account')

    context = {'form': form}
    return render(request, 'users/profile_form.html', context)


@login_required(login_url='login')
def createSkill(request):
    context = {}
    return render(request, 'users/skill_form.html', context)
