from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def kohil(request):
    return render(request,'rcb.html')

def abd(request):
    return HttpResponse('<h1>Mr abd</h1>')