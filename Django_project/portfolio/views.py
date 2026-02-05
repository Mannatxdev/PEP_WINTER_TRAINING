

# from django.shortcuts import render
# from django.http import HttpResponse
# from .models import User
# from django.template import loader



# def index(request):
#     myuser = User.objects.all().values()
#     templates = loader.get_template('user_list.html')
#     context = {
#         'myuser': myuser,
#     }
#     return HttpResponse(templates.render(context, request))

# if request.method == 'POST':
#         form = RegisterForm(request.POST)
#         if form.is_valid():
#             User.objects.create_user(
#                 username=form.cleaned_data['username'],
#                 email=form.cleaned_data['email'],
#                 password=form.cleaned_data['password'],
#                 first_name=form.cleaned_data['first_name'],
#                 last_name=form.cleaned_data['last_name']
#             )
#             return redirect('login')
#     else:
#         form = RegisterForm()

#     return render(request, 'register.html', {'form': form})
    


# from django.shortcuts import render
# from django.template import loader
# from .models import User
# from django.http import HttpResponse

# def index(request):
#     users = User.objects.all()   
#     template = loader.get_template('user_list.html')
#     context = {
#         'User': User,
#     }
#     return HttpResponse(template.render(context, request))

from django.shortcuts import render
from django.contrib.auth.models import User

def index(request):
    users = User.objects.all()   
    return render(request, 'user_list.html', {'users': users})
