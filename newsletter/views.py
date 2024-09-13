from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import NewsLetterForm

# Create your views here.
def subscribe(request):
    if request.method == 'POST':
        Form = NewsLetterForm(REQUEST.post)
        if form.is_valid():
            form.save()  # Save the subscriber's email to the database
            messages.success(request, 'Thank you for subscribing to our newsletter!')
            return redirect('home')
    else:
        form = NewsLetterForm()
    
    return render(request, 'newsletter/subscribe.html', {'form': form})

