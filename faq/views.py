from django.shortcuts import render
from .models import Faq
from .forms import FaqForm


# Create your views here.
def faq(request):
    """View to display all FAQs"""
    faqs = Faq.objects.all()
    return render(request, 'faq/faq.html', {'faqs': faqs})
