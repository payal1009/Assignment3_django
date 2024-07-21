from django import forms
from .models import modelClass
class FormClass(forms.Form):
    i=forms.IntegerField()
    name=forms.CharField()
    password=forms.CharField()
    email=forms.EmailField()
    date=forms.DateField()
    status=forms.BooleanField(required=False)
    
