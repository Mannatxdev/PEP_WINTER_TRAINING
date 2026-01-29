from django.http import HttpResponse
from django.shortcuts import render 

def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("This is the contact page of the polls app.")

def about(request):
    return HttpResponse("This is the about page of the polls app.")

def resume(request):
    return HttpResponse("This is the about page of the polls app.")

def project(request):
    return HttpResponse("This is the about page of the polls app.")