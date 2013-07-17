from django import forms

class UploadFileImage(forms.Form):
    photo = forms.ImageField()

