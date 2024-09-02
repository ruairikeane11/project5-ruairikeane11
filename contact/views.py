from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from .forms import ContactForm
from django.contrib import messages


def contact_us(request):
    """
    Renders the contact page with ContactForm
    """
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, "Your request has been submitted successfully!", extra_tags='info')
    else:
        form = ContactForm()

    submitted_contacts = Contact.objects.all().order_by('-created_on')

    return render(
        request,
        "contact/contact.html",
        {"form": form,
         'submitted_contacts': submitted_contacts},
    )

