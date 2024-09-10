from django.shortcuts import render

# Create your views here.
def faq(request):
    """ A view to render the faq page """

    
    return render(request, 'templates/faq.html')