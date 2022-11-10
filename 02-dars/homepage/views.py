from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def homePageView(request):
    return HttpResponse("Hello World!")

def data_of_mine(request):
    return HttpResponse("Men Maxammadsoliyev Umidbek 2002 - yil 15 - oktyabrda tug'ilganman")