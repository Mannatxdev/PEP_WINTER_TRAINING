from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import user, FormModel, LoginUser, SignupUser
from django.contrib import messages

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



#def form_view(request):
#   if request.method ==  "POST":
#        print(request.POST)
#        name =  request.POST.get('your_name')
#    return render(request, "form.html")


def form_view(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        # Save to FormModel (title/description fields) instead of `user` model
        u = FormModel(
            title=title,
            description=description,
        )
        u.save()
        # redirect to avoid duplicate submissions
        return redirect('form_view')

    # on GET, show existing items
    items = FormModel.objects.all()
    return render(request, "form.html", {"items": items})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = None

        try:
            user = SignupUser.objects.get(username=username, is_active=True)
        except SignupUser.DoesNotExist:
            try:
                user = LoginUser.objects.get(username=username, is_active=True)
            except LoginUser.DoesNotExist:
                user = None

        if user and user.check_password(password):
            messages.success(request, f"Welcome, {username}!")
            return redirect("home")
        
        messages.error(request, "Invalid username or password")

    return render(request, "login.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not username or not email or not password:
            messages.error(request, "All fields are  required.")
        elif SignupUser.objects.filter(username=username).exists():
            messages.error(request, "username already taken.")
        elif SignupUser.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")

        else:
            new_user= SignupUser(username=username, email=email)
            new_user.set_password(password)
            new_user.save()
            messages.success(request, "Signup successfull, you can now log in.")
            return redirect("login")
    return render(request, "sign_up.html")
