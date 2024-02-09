from django import forms
from .models import FileStorage


class FileUploadForm(forms.ModelForm):
    class Meta:
        model = FileStorage
        fields = ['file']
