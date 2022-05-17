from ckeditor.widgets import CKEditorWidget
from django import forms

from ckeditor_uploader.fields import RichTextUploadingField

import labordelivery
from django.forms import inlineformset_factory  # Facilitates multiple form in group
from .models import Questionnaire, QuestionnaireItem
from django_filters.views import FilterView

class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

class QuestionnaireCreateForm(BaseForm, forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Questionnaire
        fields = ['date', 'title']


class QuestionnaireForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Questionnaire
        fields = '__all__'


class QuestionnaireEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Questionnaire
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



class QuestionnaireItemEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = QuestionnaireItem
        fields = '__all__'


class QuestionnaireItemForm(forms.ModelForm):

    class Meta:
        model = QuestionnaireItem
        fields = '__all__'


NewQuestionnaireItemFormSet = inlineformset_factory(Questionnaire, QuestionnaireItem,
                                 # # fields='__all__',
                                 fields=['product', 'labordelivery', 'qty', 'numworkstation', 'numserver', 'numipaddress', ],
                                 # exclude=('total_price',),
                        extra=1)  # access both customer and order form
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     # TNT Line #1
    #     self.fields['product'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
    #     self.fields['labordelivery'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
    #
    #     self.fields['qty'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
    #     self.fields['numworkstation'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
    #     self.fields['numserver'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
    #     self.fields['numipaddress'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;',
    #
    #

