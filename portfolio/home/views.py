from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')


#error 
def custom_404(request, exception):
    return render(request, '404.html', status=404)

