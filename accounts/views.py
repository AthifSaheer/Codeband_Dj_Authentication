from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from accounts.forms import CustomUserCreationForm
from django.urls import reverse

def register_view(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            print("USer successfully registered")
            return redirect(reverse('register'))
    return render(request, 'registration/register.html', {'form':form})