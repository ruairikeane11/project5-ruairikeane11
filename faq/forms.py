from django import forms
from .models import Faq


class FaqForm(forms.ModelForm):
    """
    Form for adding and editing FAQs
    """
    class Meta:
        model = Faq
        fields = ['question', 'answer']
        widgets = {
            'question': forms.TextInput
            (attrs={'class': 'form-control',
             'placeholder': 'Enter your question'}),
            'answer': forms.Textarea
            (attrs={'class': 'form-control',
             'rows': 4, 'placeholder': 'Enter the answer'}),
        }
