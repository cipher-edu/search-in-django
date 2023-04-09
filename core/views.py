from django.shortcuts import render
from .models import *
# Create your views here.
def home(request):
    if 'q' in request.GET:
        qidirish = request.GET['q']
        post = Stock.objects.filter(price__icontains=qidirish)
    else:
        post = Stock.objects.all()
    # post = Stock.objects.all()
    return render (request, 'index.html', {'post':post})