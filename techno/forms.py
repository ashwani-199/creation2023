from django.db import models  
from django.forms import fields  
from .models import ResizeImage  
from django import forms 



class ResizeImageForm(forms.ModelForm):  
    class Meta:
        model = ResizeImage  
        fields = ['image']  