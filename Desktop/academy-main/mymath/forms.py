from django import forms
from . import models

class textus(forms.ModelForm):
    class Meta: 
        model = models.registration
        fields = ['name', 'body', 'phone','text']
