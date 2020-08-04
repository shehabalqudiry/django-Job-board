from django.shortcuts import render
from .forms import SignupForm

# Create your views here.


def signup(request):
    form = SignupForm()
    context = {'form': form}
    return render(request, 'registration/signup.html', context)
