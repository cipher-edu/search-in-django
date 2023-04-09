from django.shortcuts import render
from .models import *
from django.db.models import Q
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