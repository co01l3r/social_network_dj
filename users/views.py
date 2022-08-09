from django.shortcuts import render
from .models import Profile


def loginPage(request):
    return render(request, 'users/login_register.html')


def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'users/profiles.html', context)


def userProfile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'users/user_profile.html', context)
