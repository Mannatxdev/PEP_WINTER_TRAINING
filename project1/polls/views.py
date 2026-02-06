from django.contrib import messages
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



# def form_view(request):
#     if request.method ==  "POST":
#         print(request.POST)
#         name =  request.POST.get('your_name')
#     return render(request, "form.html")

# from django.shortcuts import render



def form_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        u = user(
            title=title,
            description= description,
        )
        u.save()

    return render(request, "form.html")


# i have to store this data in admin
# /form and /admin

from .models import LoginUser
from django.shortcuts import redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = LoginUser.objects.get(username=username, is_active=True)
        except LoginUser.DoesNotExist:
            messages.error(request,"Invalid username or password")
        else:            
            if user.password == password:
                messages.success(request,f"Welcome,{username}!")
                return redirect("home")
            messages.error(request,"Invalid username or password")
                                
    return render(request, "login.html")