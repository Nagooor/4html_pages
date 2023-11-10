from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rohit(request):
    return render(request,'mi.html')

def bombra(request):
    return HttpResponse('<h1>Mr bowlar</h1>')