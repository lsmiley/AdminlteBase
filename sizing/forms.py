from django import forms
from .models import *
from django.forms.models import inlineformset_factory
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Fieldset, Div, HTML, ButtonHolder, Submit
from .custom_layout_object import *


class SizingItemForm(forms.ModelForm):

    class Meta:
        model = SizingItem
        exclude = ()


SizingItemFormSet = inlineformset_factory(
    Sizing, SizingItem, form=SizingItemForm,
    fields=['name', 'language'], extra=1, can_delete=True
    )


class SizingForm(forms.ModelForm):

    class Meta:
        model = Sizing
        exclude = ['created_by', ]

    def __init__(self, *args, **kwargs):
        super(SizingForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = True
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-md-3 create-label'
        self.helper.field_class = 'col-md-9'
        self.helper.layout = Layout(
            Div(
                Field('subject'),
                Field('owner'),
                Fieldset('Add items',
                    Formset('items')),
                Field('note'),
                HTML("<br>"),
                ButtonHolder(Submit('submit', 'Save')),
                )
            )
