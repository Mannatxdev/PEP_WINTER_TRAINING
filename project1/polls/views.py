from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import user

def index(request):
    myusers = user.objects.all().values()
    template = loader.get_template('user_list.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))


from .forms import InputForm

def home_view(request):
    context = {}
    context["form"] =  InputForm()
    return render(request, "home.html",  context)



def form_view(request):
    if request.method ==  "POST":
        print(request.POST)
        name =  request.POST.get('your_name')
    return render(request, "form.html")