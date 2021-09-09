from django import forms
from django.forms.models import ModelForm
from .models import *

    
class UploadFileForm(forms.ModelForm):
    class Meta:
        model=PersonModel
        fields = ('no','file')
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].required = False