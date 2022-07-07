from django.forms import ModelForm, inlineformset_factory, widgets  # Facilitates multiple form in group
from django import forms
from .models import Sizer, SizerItem


class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SizerForm(ModelForm):
    class Meta:
        model = Sizer
        exclude = ()


class SizerItemForm(ModelForm):
    class Meta:
        model = SizerItem
        exclude = ()


class SizerEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Sizer
        fields = '__all__'


SizerItemFormSet = inlineformset_factory(Sizer, SizerItem,
                                         form=SizerItemForm,
                                         fields=['product', 'labordelivery', 'qty', 'numworkstation', 'numserver', 'numipaddress',],
                                         widgets={
                                                       'product': forms.Select(attrs={'style': 'width:160px;height:25px; align:center;'}),
                                                       'labordelivery': forms.Select(attrs={'style': 'width:160px;height:25px; align:center;'}),
                                                       'qty': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
                                                       'numworkstation': forms.TextInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
                                                       'numserver': forms.TextInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
                                                       'numipaddress': forms.TextInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
                                                   },
                                         extra=1)
