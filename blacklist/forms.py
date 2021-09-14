from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from .models import *



class NewPersonForm(forms.ModelForm):
    class Meta:
        model=Person
        fields=['name','kolasid','count']+['places[name]' for name in Person.keys()]+['detail','first','recent','image','file']
    
    def clean(self,*args, **kwargs):
        content1=self.cleaned_data.get('name')
        content2=self.cleaned_data.get('kolasid')
        if content1=="" and content2=="":
            raise ValidationError(_("이름과 Kolas Id 둘다 빈칸으로 둘 순 없습니다."))
        return super(NewPersonForm, self).clean(*args, **kwargs)
    
    def save(self,commit=True):
        person=Person(**self.cleaned_data)
        if commit:
            person.save()
        return person