from django.shortcuts import render
from .models import ShopPhone


def home(request):
    shops = ShopPhone.objects.all()
    return render(request,'base.html',{'shops' : shops})


    

# Create your views here.
