from django import forms

from .models import Contact

class FeedBackForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['firstname','email','subject','message']