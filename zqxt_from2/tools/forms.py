from django import forms

class Addfrom(forms.From):
    a = forms.IntegerField()
    b = forms.IntegerField()