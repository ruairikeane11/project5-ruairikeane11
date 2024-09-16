from django import forms
from .models import Subscribe


class NewsLetterForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email',
                'aria-label': 'Newsletter'
            }),
        }
