from django import forms

class SearchForm(forms.Form):
    person_info = forms.CharField(max_length=70)