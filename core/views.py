from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    if 'q' in request.GET:
        qidirish = request.GET['q']
        umumiy  = Q(Q(price__icontains=qidirish) | Q(name__icontains=qidirish))
        post = Stock.objects.filter(umumiy)
    else:
        post = Stock.objects.all()
    # post = Stock.objects.all()
    return render (request, 'index.html', {'post':post})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user=User.objects.create_user(username=username, password=password)
            form.save()
            #Below 2 lines, if you want user to get logged in
            user = authenticate(username=username, password=password)
            login(request, form)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form':form})