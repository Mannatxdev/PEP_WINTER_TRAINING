from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            send_mail(
                subject="New Contact Query",
                message=f"""
Name: {contact.name}
Email: {contact.email}
Message:
{contact.message}
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            messages.success(request, "Your message has been sent successfully!")
            form = ContactForm()

    else:
        form = ContactForm()

    # return render(request, "main/contact.html", {"form": form})
    return render(request, "contact.html", {"form": form})

