from django import forms
from .models import Sizingtype
from ckeditor.fields import RichTextField


class SizingtypeForm(forms.ModelForm):
    Sizingtypename = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    Sizingtypedesc = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    Sizingtypetype = forms.CharField(widget=forms.TextInput(), required=True, max_length=100)
    memo = RichTextField()

    class Meta:
        model = Sizingtype
        fields = ('Sizingtypename', 'Sizingtypedesc', 'Sizingtypetype', 'memo',)

