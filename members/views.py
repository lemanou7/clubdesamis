from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm
# Create your views here.

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('first_name')
            messages.success(request, f'Profile de {user} créé avec succès')
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'members/registerform.html',{'form':form})

@login_required
def profile(request):
    return render(request, 'members/profile.html')
