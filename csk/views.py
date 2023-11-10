from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def doni(request):
    return render(request,'csk.html')

def raina(request):
    return HttpResponse('<h1>Mr raina</h1>')