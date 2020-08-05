from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib.auth import authenticate, login
from .models import Profile
# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()

    context = {'form': form}
    return render(request, 'registration/signup.html', context)


def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request, 'accounts/profile.html', {'profile': profile})


def profile_edit(request):
    pass
