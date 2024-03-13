# from django import forms
# class StudentForm (forms.Form):
#     name=forms.CharField(max_length=200)
#     age=forms.IntegerField()
#     marks=forms.IntegerField()
#     addrs=forms.CharField(max_length=200)
#     phone=forms.IntegerField()

from django import forms

class FormName(forms.ModelForm):
    
