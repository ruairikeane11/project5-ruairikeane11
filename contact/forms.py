from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form class for users to make a contact request
    """
    class Meta:
        model = Contact
        fields = ['title', 'name', 'email', 'content']
        widgets = {
         'content': forms.Textarea
         (attrs={'rows': 4, 'style': 'resize:none; width:100%'}),
        }
