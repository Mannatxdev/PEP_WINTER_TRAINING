from django.shortcuts import render, redirect


def register(request):
    return render(request, 'register.html')


def login_view(request):
    # minimal login page (no authentication wiring) so templates/linking work
    if request.method == 'POST':
        # placeholder: normally you'd authenticate here
        return redirect('register')
    return render(request, 'login.html')