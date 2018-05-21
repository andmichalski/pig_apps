from django import forms
from .models import DBFFile

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = DBFFile
        fields = ['file1', 'file2']
