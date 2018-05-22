from django import forms
from .models import DBFFile
from django.forms import formset_factory

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = DBFFile
        fields = ['file']


UploadFormSet = formset_factory(UploadFileForm, extra=1)



class NumberFilesForm(forms.Form):
    number_dbfs = forms.IntegerField(max_value=20)