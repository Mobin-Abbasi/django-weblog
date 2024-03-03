from django import forms
from .models import *


class TicketForm(forms.Form):
    name = forms.CharField(max_length=255, required=True)
    comments = forms.CharField(widget=forms.Textarea, required=True)
    email = forms.EmailField(required=True)
    subject = forms.CharField(max_length=255, required=True)
