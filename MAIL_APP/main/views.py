from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from .forms import EmailForm

def send_email_view(request):
    success = False

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            to_email = form.cleaned_data['to_email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [to_email],
                fail_silently=False,
            )
            success = True
    else:
        form = EmailForm()

    return render(request, 'send_email.html', {'form': form, 'success': success})


