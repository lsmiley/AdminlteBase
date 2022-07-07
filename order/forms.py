from ckeditor.widgets import CKEditorWidget
from django import forms

from ckeditor_uploader.fields import RichTextUploadingField

import labordelivery
from django.forms import inlineformset_factory  # Facilitates multiple form in group
from .models import Order, OrderItem
from product.models import Product, Category

class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class OrderCreateForm(BaseForm, forms.ModelForm):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = ['date', 'title']


# class QuestionnaireCreateForm(BaseForm, forms.ModelForm):
#     # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     TranStartDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
#     # aix = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}))
#     # Other_Features_or_Platforms_Note = CKEditorWidget(attrs={'toolbar': 'Basic', 'height': 70, 'width': 430,})
#     # AntiVirusMalware = forms.BooleanField()
#
#     class Meta:
#         model = Order
#         fields = ['date',
#                   'title',
#                   'due_date',
#                   'prepardedby',
#                   'team',
#                   'RequesterFirstName',
#                   'RequesterLastName',
#                   'RequesterRole',
#                   'RequesterEmail',
#                   'CustomerName',
#                   'SalesContactName',
#                   'SalesContactEmail',
#                   'TranStartDate',
#                   'Revenue_Structure_Select',
#                   'Revenue_Structure_Cost_Explain',
#                   'rfs_num',
#                   'appttus_num',
#                   'Solution_Design',
#                   'Solution_Owner',
#                   'Service_Delivery_Requirements',
#                   'Restricted_Delivery',
#                   'Questionaire_num_consoles',
#                   'Questionaire_num_workstation',
#                   'Questionaire_num_server',
#
#                   'AntiVirusMalware',
#                   'DLP_on_Workstations',
#                   'DLP_on_Servers',
#                   'Encryption_on_Workstations',
#                   'Encryption_on_Servers',
#                   'NAS_Storage',
#                   'Windows',
#                   'AIX',
#                   'VDI',
#                   'URL_Filtering',
#                   'HIPs_on_Workstations',
#                   'HIPs_on_Servers',
#                   'Firewall_on_Workstations',
#                   'Firewall_on_Servers',
#                   'BigFix_Patching_Scanning',
#                   'Linux',
#                   'Integrity_Monitoring',
#                   'Citrix',
#                   'Other_Features_or_Platforms',
#                   'Other_Features_or_Platforms_Note',
#
#                   ]
#
#         widgets = {
#
#
#             'RequesterFirstName': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
#             'RequesterLastName': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
#             'RequesterEmail': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
#             'due_date': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
#
#             'date': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
#             'TranStartDate': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
#
#             'AntiVirusMalware': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'DLP_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'DLP_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Encryption_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Encryption_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'NAS_Storage': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Windows': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'AIX': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'VDI': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'URL_Filtering': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'HIPs_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'HIPs_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Firewall_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Firewall_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'BigFix_Patching_Scanning': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Linux': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Integrity_Monitoring': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Citrix': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Other_Features_or_Platforms': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#             'Restricted_Delivery': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
#
#         }
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
#         # Customer's Infor section
#         self.fields['CustomerName'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['SalesContactName'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['SalesContactEmail'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['TranStartDate'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['rfs_num'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['appttus_num'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['Revenue_Structure_Select'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
#         self.fields['Revenue_Structure_Cost_Explain'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
#         self.fields['Solution_Design'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
#         self.fields['Solution_Owner'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
#         self.fields['Service_Delivery_Requirements'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
#         # self.fields['Restricted_Delivery'].widget.attrs['style'] = 'width:120px; height:20px; font-size: 12px;'
#         self.fields['Revenue_Structure_Cost_Explain'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#
#         self.fields['prepardedby'].widget.attrs['style'] = 'width:120px; height:20px; font-size: 10px;'
#         self.fields['Questionaire_num_consoles'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['Questionaire_num_workstation'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
#         self.fields['Questionaire_num_server'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'

class OrderEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'style': 'width:300px;height:25px; align:center;'}),


        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)



        # TNT Line #1
        self.fields['date'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'


        # TNT Line #1
        self.fields['executetransitionplan_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['executetransitionplan_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transitionhoursitem'].disabled = True

        self.fields['executetransitionplan_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transitionhours'].disabled = True

        self.fields['executetransitionplan_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transformationhoursitem'].disabled = True

        self.fields['executetransitionplan_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transformationhours'].disabled = True

        # TNT Line #2
        self.fields['createbestpracticecustom_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['createbestpracticecustom_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transitionhoursitem'].disabled = True

        self.fields['createbestpracticecustom_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transitionhours'].disabled = True

        self.fields['createbestpracticecustom_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transformationhoursitem'].disabled = True

        self.fields['createbestpracticecustom_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transformationhours'].disabled = True

    # TNT Line #3
        self.fields['testinfrastructurepoc_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['testinfrastructurepoc_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transitionhoursitem'].disabled = True

        self.fields['testinfrastructurepoc_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transitionhours'].disabled = True

        self.fields['testinfrastructurepoc_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transformationhoursitem'].disabled = True

        self.fields['testinfrastructurepoc_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transformationhours'].disabled = True

    # TNT Line #4
        self.fields['troubleshoottune_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['troubleshoottune_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transitionhoursitem'].disabled = True

        self.fields['troubleshoottune_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transitionhours'].disabled = True

        self.fields['troubleshoottune_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transformationhoursitem'].disabled = True

        self.fields['troubleshoottune_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transformationhours'].disabled = True

    # TNT Line #5
        self.fields['installconfigure_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['installconfigure_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transitionhoursitem'].disabled = True

        self.fields['installconfigure_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transitionhours'].disabled = True

        self.fields['installconfigure_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transformationhoursitem'].disabled = True

        self.fields['installconfigure_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transformationhours'].disabled = True


    # TNT Line #6
        self.fields['administratortraining_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['administratortraining_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transitionhoursitem'].disabled = True

        self.fields['administratortraining_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transitionhours'].disabled = True

        self.fields['administratortraining_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transformationhoursitem'].disabled = True

        self.fields['administratortraining_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transformationhours'].disabled = True


    # TNT Line #7
        self.fields['developserviceresponsibilitymatrix_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['developserviceresponsibilitymatrix_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transitionhoursitem'].disabled = True

        self.fields['developserviceresponsibilitymatrix_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transitionhours'].disabled = True

        self.fields['developserviceresponsibilitymatrix_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transformationhoursitem'].disabled = True

        self.fields['developserviceresponsibilitymatrix_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transformationhours'].disabled = True


    # TNT Line #8
        self.fields['establishanyneededserviceaccounts_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['establishanyneededserviceaccounts_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transitionhoursitem'].disabled = True

        self.fields['establishanyneededserviceaccounts_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transitionhours'].disabled = True

        self.fields['establishanyneededserviceaccounts_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transformationhoursitem'].disabled = True

        self.fields['establishanyneededserviceaccounts_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transformationhours'].disabled = True


    # TNT Line #9
        self.fields['researchandsetupemailautomation_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['researchandsetupemailautomation_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transitionhoursitem'].disabled = True

        self.fields['researchandsetupemailautomation_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transitionhours'].disabled = True

        self.fields['researchandsetupemailautomation_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transformationhoursitem'].disabled = True

        self.fields['researchandsetupemailautomation_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transformationhours'].disabled = True


    # TNT Line #10
        self.fields['installconfigureremoteconsoles_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['installconfigureremoteconsoles_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transitionhoursitem'].disabled = True

        self.fields['installconfigureremoteconsoles_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transitionhours'].disabled = True

        self.fields['installconfigureremoteconsoles_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transformationhoursitem'].disabled = True

        self.fields['installconfigureremoteconsoles_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transformationhours'].disabled = True


    # TNT Line #11
        self.fields['workwithsecops_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['workwithsecops_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transitionhoursitem'].disabled = True

        self.fields['workwithsecops_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transitionhours'].disabled = True

        self.fields['workwithsecops_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transformationhoursitem'].disabled = True

        self.fields['workwithsecops_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transformationhours'].disabled = True


    # TNT Line #12
        self.fields['staffingccoordinating_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['staffingccoordinating_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transitionhoursitem'].disabled = True

        self.fields['staffingccoordinating_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transitionhours'].disabled = True

        self.fields['staffingccoordinating_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transformationhoursitem'].disabled = True

        self.fields['staffingccoordinating_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transformationhours'].disabled = True


    # TNT Line #13
        self.fields['identifytestdocument_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['identifytestdocument_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transitionhoursitem'].disabled = True

        self.fields['identifytestdocument_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transitionhours'].disabled = True

        self.fields['identifytestdocument_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transformationhoursitem'].disabled = True

        self.fields['identifytestdocument_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transformationhours'].disabled = True


    # TNT Line #14
        self.fields['obtainnetworkandosaccesswave1_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['obtainnetworkandosaccesswave1_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transitionhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave1_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transitionhours'].disabled = True

        self.fields['obtainnetworkandosaccesswave1_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transformationhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave1_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transformationhours'].disabled = True


    # TNT Line #15
        self.fields['obtainnetworkandosaccesswave2_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['obtainnetworkandosaccesswave2_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transitionhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave2_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transitionhours'].disabled = True

        self.fields['obtainnetworkandosaccesswave2_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transformationhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave2_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transformationhours'].disabled = True


    # TNT Line #16
        self.fields['developprovideagentsoftware_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['developprovideagentsoftware_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transitionhoursitem'].disabled = True

        self.fields['developprovideagentsoftware_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transitionhours'].disabled = True

        self.fields['developprovideagentsoftware_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transformationhoursitem'].disabled = True

        self.fields['developprovideagentsoftware_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transformationhours'].disabled = True


    # TNT Line #17
        self.fields['installconfigureodbc_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['installconfigureodbc_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transitionhoursitem'].disabled = True

        self.fields['installconfigureodbc_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transitionhours'].disabled = True

        self.fields['installconfigureodbc_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transformationhoursitem'].disabled = True

        self.fields['installconfigureodbc_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transformationhours'].disabled = True


    # TNT Line #18
        self.fields['customerreviewsignoff_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['customerreviewsignoff_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transitionhoursitem'].disabled = True

        self.fields['customerreviewsignoff_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transitionhours'].disabled = True

        self.fields['customerreviewsignoff_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transformationhoursitem'].disabled = True

        self.fields['customerreviewsignoff_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transformationhours'].disabled = True


    # TNT Line #10
        self.fields['establishhealthcheck_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['establishhealthcheck_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transitionhoursitem'].disabled = True

        self.fields['establishhealthcheck_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transitionhours'].disabled = True

        self.fields['establishhealthcheck_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transformationhoursitem'].disabled = True

        self.fields['establishhealthcheck_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transformationhours'].disabled = True


    # TNT Line #20
        self.fields['developworkflows_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['developworkflows_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transitionhoursitem'].disabled = True

        self.fields['developworkflows_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transitionhours'].disabled = True

        self.fields['developworkflows_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transformationhoursitem'].disabled = True

        self.fields['developworkflows_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transformationhours'].disabled = True


    # TNT Line #21
        self.fields['operationaldocumentation_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['operationaldocumentation_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transitionhoursitem'].disabled = True

        self.fields['operationaldocumentation_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transitionhours'].disabled = True

        self.fields['operationaldocumentation_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transformationhoursitem'].disabled = True

        self.fields['operationaldocumentation_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transformationhours'].disabled = True


    # TNT Line #22
        self.fields['shadowestablishreviewallprocedures_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['shadowestablishreviewallprocedures_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transitionhoursitem'].disabled = True

        self.fields['shadowestablishreviewallprocedures_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transitionhours'].disabled = True

        self.fields['shadowestablishreviewallprocedures_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transformationhoursitem'].disabled = True

        self.fields['shadowestablishreviewallprocedures_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transformationhours'].disabled = True


    # TNT Line #23
        self.fields['otherdetail_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['otherdetail_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transitionhoursitem'].disabled = True

        self.fields['otherdetail_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transitionhours'].disabled = True

        self.fields['otherdetail_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transformationhoursitem'].disabled = True

        self.fields['otherdetail_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transformationhours'].disabled = True


    # TNT Line #24
        self.fields['SpecialItemsDesc1'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem1_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem1_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transitionhoursitem'].disabled = True

        self.fields['specialitem1_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transitionhours'].disabled = True

        self.fields['specialitem1_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transformationhoursitem'].disabled = True

        self.fields['specialitem1_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transformationhours'].disabled = True

    # TNT Line #25
        self.fields['SpecialItemsDesc2'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem2_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem2_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transitionhoursitem'].disabled = True

        self.fields['specialitem2_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transitionhours'].disabled = True

        self.fields['specialitem2_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transformationhoursitem'].disabled = True

        self.fields['specialitem2_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transformationhours'].disabled = True

    # TNT Line #26
        self.fields['SpecialItemsDesc3'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem3_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem3_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transitionhoursitem'].disabled = True

        self.fields['specialitem3_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transitionhours'].disabled = True

        self.fields['specialitem3_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transformationhoursitem'].disabled = True

        self.fields['specialitem3_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transformationhours'].disabled = True

    # TNT Line #27
        self.fields['SpecialItemsDesc4'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem4_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem4_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transitionhoursitem'].disabled = True

        self.fields['specialitem4_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transitionhours'].disabled = True

        self.fields['specialitem4_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transformationhoursitem'].disabled = True

        self.fields['specialitem4_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transformationhours'].disabled = True

    # TNT Line #28
        self.fields['SpecialItemsDesc5'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem5_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem5_transitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transitionhoursitem'].disabled = True

        self.fields['specialitem5_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transitionhours'].disabled = True

        self.fields['specialitem5_transformationhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transformationhoursitem'].disabled = True

        self.fields['specialitem5_transformationhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transformationhours'].disabled = True

        self.fields['totaltransitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['totaltransitionhoursitem'].disabled = True

        # self.fields['product'].queryset = Product.objects.none()
        #
        # if 'category' in self.data:
        #     try:
        #         category_id = int(self.data.get('category'))
        #         self.fields['product'].queryset = Product.objects.filter(category_id=category_id).order_by('categoryname')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['product'].queryset = self.instance.country.city_set.order_by('productname')


class SizingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):                                                        # used to set css classes to the various fields
        super().__init__(*args, **kwargs)
        self.fields['Date'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['title'].widget.attrs.update({'class': 'textinput form-control'})

        self.fields['Value'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Discount'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Final_value'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Is paid'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum numconsole'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_numserver'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_workstation'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_ipaddress'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_endpoint'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_hours'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_fte'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_srvshourscalc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_wkstnshourscalc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_ipshourscalc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Sum_consolehourscalc'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Tntdescription'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Managementmod1stline'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Managementmod2ndline'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransitiontotalfte'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransitiontotalhours'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransitiontotalband8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransitiontotal1stlinemgr'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransitiontotal2ndlinemgr'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransitiontotals'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransformationtotalfte'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransformationtotalhours'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransformationtotalband8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransformationtotal1stlinemgr'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransformationtotal2ndlinemgr'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Totaltransformationtotals'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transitionhoursfte'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transitionfirstlinemanagementband8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transitionsecondlinemanagementband8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transitionfirstlinemanagementband8weeks'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transitionsecondlinemanagementband8weeks'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transitionsubtotalshours:'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transitionfirstlinemanagementband8hours'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transfortionhoursfte:'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transformationfirstlinemanagementband8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transformationsecondlinemanagementband8'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transformationfirstlinemanagementband8weeks'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Transformationsecondlinemanagementband8weeks'].widget.attrs.update({'class': 'textinput form-control'})
        self.fields['Tranformationsubtotalshours:'].widget.attrs.update({'class': 'textinput form-control'})






        # TNT Line #1
        self.fields['date'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        # TNT Line #1
        self.fields['executetransitionplan_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['executetransitionplan_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transitionhoursitem'].disabled = True

        self.fields['executetransitionplan_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transitionhours'].disabled = True

        self.fields['executetransitionplan_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transformationhoursitem'].disabled = True

        self.fields['executetransitionplan_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['executetransitionplan_transformationhours'].disabled = True

        # TNT Line #2
        self.fields['createbestpracticecustom_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['createbestpracticecustom_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transitionhoursitem'].disabled = True

        self.fields['createbestpracticecustom_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transitionhours'].disabled = True

        self.fields['createbestpracticecustom_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transformationhoursitem'].disabled = True

        self.fields['createbestpracticecustom_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['createbestpracticecustom_transformationhours'].disabled = True

        # TNT Line #3
        self.fields['testinfrastructurepoc_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['testinfrastructurepoc_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transitionhoursitem'].disabled = True

        self.fields['testinfrastructurepoc_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transitionhours'].disabled = True

        self.fields['testinfrastructurepoc_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transformationhoursitem'].disabled = True

        self.fields['testinfrastructurepoc_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['testinfrastructurepoc_transformationhours'].disabled = True

        # TNT Line #4
        self.fields['troubleshoottune_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['troubleshoottune_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transitionhoursitem'].disabled = True

        self.fields['troubleshoottune_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transitionhours'].disabled = True

        self.fields['troubleshoottune_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transformationhoursitem'].disabled = True

        self.fields['troubleshoottune_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['troubleshoottune_transformationhours'].disabled = True

        # TNT Line #5
        self.fields['installconfigure_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['installconfigure_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transitionhoursitem'].disabled = True

        self.fields['installconfigure_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transitionhours'].disabled = True

        self.fields['installconfigure_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transformationhoursitem'].disabled = True

        self.fields['installconfigure_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigure_transformationhours'].disabled = True

        # TNT Line #6
        self.fields['administratortraining_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['administratortraining_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transitionhoursitem'].disabled = True

        self.fields['administratortraining_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transitionhours'].disabled = True

        self.fields['administratortraining_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transformationhoursitem'].disabled = True

        self.fields['administratortraining_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['administratortraining_transformationhours'].disabled = True

        # TNT Line #7
        self.fields['developserviceresponsibilitymatrix_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['developserviceresponsibilitymatrix_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transitionhoursitem'].disabled = True

        self.fields['developserviceresponsibilitymatrix_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transitionhours'].disabled = True

        self.fields['developserviceresponsibilitymatrix_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transformationhoursitem'].disabled = True

        self.fields['developserviceresponsibilitymatrix_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developserviceresponsibilitymatrix_transformationhours'].disabled = True

        # TNT Line #8
        self.fields['establishanyneededserviceaccounts_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['establishanyneededserviceaccounts_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transitionhoursitem'].disabled = True

        self.fields['establishanyneededserviceaccounts_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transitionhours'].disabled = True

        self.fields['establishanyneededserviceaccounts_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transformationhoursitem'].disabled = True

        self.fields['establishanyneededserviceaccounts_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishanyneededserviceaccounts_transformationhours'].disabled = True

        # TNT Line #9
        self.fields['researchandsetupemailautomation_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['researchandsetupemailautomation_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transitionhoursitem'].disabled = True

        self.fields['researchandsetupemailautomation_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transitionhours'].disabled = True

        self.fields['researchandsetupemailautomation_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transformationhoursitem'].disabled = True

        self.fields['researchandsetupemailautomation_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['researchandsetupemailautomation_transformationhours'].disabled = True

        # TNT Line #10
        self.fields['installconfigureremoteconsoles_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['installconfigureremoteconsoles_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transitionhoursitem'].disabled = True

        self.fields['installconfigureremoteconsoles_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transitionhours'].disabled = True

        self.fields['installconfigureremoteconsoles_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transformationhoursitem'].disabled = True

        self.fields['installconfigureremoteconsoles_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureremoteconsoles_transformationhours'].disabled = True

        # TNT Line #11
        self.fields['workwithsecops_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['workwithsecops_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transitionhoursitem'].disabled = True

        self.fields['workwithsecops_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transitionhours'].disabled = True

        self.fields['workwithsecops_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transformationhoursitem'].disabled = True

        self.fields['workwithsecops_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['workwithsecops_transformationhours'].disabled = True

        # TNT Line #12
        self.fields['staffingccoordinating_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['staffingccoordinating_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transitionhoursitem'].disabled = True

        self.fields['staffingccoordinating_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transitionhours'].disabled = True

        self.fields['staffingccoordinating_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transformationhoursitem'].disabled = True

        self.fields['staffingccoordinating_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['staffingccoordinating_transformationhours'].disabled = True

        # TNT Line #13
        self.fields['identifytestdocument_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['identifytestdocument_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transitionhoursitem'].disabled = True

        self.fields['identifytestdocument_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transitionhours'].disabled = True

        self.fields['identifytestdocument_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transformationhoursitem'].disabled = True

        self.fields['identifytestdocument_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['identifytestdocument_transformationhours'].disabled = True

        # TNT Line #14
        self.fields['obtainnetworkandosaccesswave1_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['obtainnetworkandosaccesswave1_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transitionhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave1_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transitionhours'].disabled = True

        self.fields['obtainnetworkandosaccesswave1_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transformationhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave1_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave1_transformationhours'].disabled = True

        # TNT Line #15
        self.fields['obtainnetworkandosaccesswave2_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['obtainnetworkandosaccesswave2_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transitionhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave2_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transitionhours'].disabled = True

        self.fields['obtainnetworkandosaccesswave2_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transformationhoursitem'].disabled = True

        self.fields['obtainnetworkandosaccesswave2_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['obtainnetworkandosaccesswave2_transformationhours'].disabled = True

        # TNT Line #16
        self.fields['developprovideagentsoftware_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['developprovideagentsoftware_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transitionhoursitem'].disabled = True

        self.fields['developprovideagentsoftware_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transitionhours'].disabled = True

        self.fields['developprovideagentsoftware_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transformationhoursitem'].disabled = True

        self.fields['developprovideagentsoftware_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developprovideagentsoftware_transformationhours'].disabled = True

        # TNT Line #17
        self.fields['installconfigureodbc_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['installconfigureodbc_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transitionhoursitem'].disabled = True

        self.fields['installconfigureodbc_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transitionhours'].disabled = True

        self.fields['installconfigureodbc_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transformationhoursitem'].disabled = True

        self.fields['installconfigureodbc_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['installconfigureodbc_transformationhours'].disabled = True

        # TNT Line #18
        self.fields['customerreviewsignoff_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['customerreviewsignoff_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transitionhoursitem'].disabled = True

        self.fields['customerreviewsignoff_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transitionhours'].disabled = True

        self.fields['customerreviewsignoff_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transformationhoursitem'].disabled = True

        self.fields['customerreviewsignoff_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['customerreviewsignoff_transformationhours'].disabled = True

        # TNT Line #10
        self.fields['establishhealthcheck_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['establishhealthcheck_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transitionhoursitem'].disabled = True

        self.fields['establishhealthcheck_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transitionhours'].disabled = True

        self.fields['establishhealthcheck_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transformationhoursitem'].disabled = True

        self.fields['establishhealthcheck_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['establishhealthcheck_transformationhours'].disabled = True

        # TNT Line #20
        self.fields['developworkflows_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['developworkflows_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transitionhoursitem'].disabled = True

        self.fields['developworkflows_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transitionhours'].disabled = True

        self.fields['developworkflows_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transformationhoursitem'].disabled = True

        self.fields['developworkflows_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['developworkflows_transformationhours'].disabled = True

        # TNT Line #21
        self.fields['operationaldocumentation_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['operationaldocumentation_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transitionhoursitem'].disabled = True

        self.fields['operationaldocumentation_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transitionhours'].disabled = True

        self.fields['operationaldocumentation_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transformationhoursitem'].disabled = True

        self.fields['operationaldocumentation_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['operationaldocumentation_transformationhours'].disabled = True

        # TNT Line #22
        self.fields['shadowestablishreviewallprocedures_count'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['shadowestablishreviewallprocedures_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transitionhoursitem'].disabled = True

        self.fields['shadowestablishreviewallprocedures_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transitionhours'].disabled = True

        self.fields['shadowestablishreviewallprocedures_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transformationhoursitem'].disabled = True

        self.fields['shadowestablishreviewallprocedures_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['shadowestablishreviewallprocedures_transformationhours'].disabled = True

        # TNT Line #23
        self.fields['otherdetail_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['otherdetail_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transitionhoursitem'].disabled = True

        self.fields['otherdetail_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transitionhours'].disabled = True

        self.fields['otherdetail_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transformationhoursitem'].disabled = True

        self.fields['otherdetail_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['otherdetail_transformationhours'].disabled = True

        # TNT Line #24
        self.fields['SpecialItemsDesc1'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem1_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem1_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transitionhoursitem'].disabled = True

        self.fields['specialitem1_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transitionhours'].disabled = True

        self.fields['specialitem1_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transformationhoursitem'].disabled = True

        self.fields['specialitem1_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem1_transformationhours'].disabled = True

        # TNT Line #25
        self.fields['SpecialItemsDesc2'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem2_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem2_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transitionhoursitem'].disabled = True

        self.fields['specialitem2_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transitionhours'].disabled = True

        self.fields['specialitem2_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transformationhoursitem'].disabled = True

        self.fields['specialitem2_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem2_transformationhours'].disabled = True

        # TNT Line #26
        self.fields['SpecialItemsDesc3'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem3_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem3_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transitionhoursitem'].disabled = True

        self.fields['specialitem3_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transitionhours'].disabled = True

        self.fields['specialitem3_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transformationhoursitem'].disabled = True

        self.fields['specialitem3_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem3_transformationhours'].disabled = True

        # TNT Line #27
        self.fields['SpecialItemsDesc4'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem4_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem4_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transitionhoursitem'].disabled = True

        self.fields['specialitem4_transitionhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transitionhours'].disabled = True

        self.fields['specialitem4_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transformationhoursitem'].disabled = True

        self.fields['specialitem4_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem4_transformationhours'].disabled = True

        # TNT Line #28
        self.fields['SpecialItemsDesc5'].widget.attrs['style'] = 'width:500px; height:20px; font-size: 10px;'
        self.fields['specialitem5_count'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'

        self.fields['specialitem5_transitionhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transitionhoursitem'].disabled = True

        self.fields['specialitem5_transitionhours'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transitionhours'].disabled = True

        self.fields['specialitem5_transformationhoursitem'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transformationhoursitem'].disabled = True

        self.fields['specialitem5_transformationhours'].widget.attrs[
            'style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['specialitem5_transformationhours'].disabled = True

        self.fields['totaltransitionhoursitem'].widget.attrs['style'] = 'width:80px; height:20px; font-size: 10px;'
        self.fields['totaltransitionhoursitem'].disabled = True

    class Meta:
        model = Category
        fields = '__all__'


class OrderItemEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'

# ***** Start for Dependent DropDown List ******
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['product'].queryset = Product.objects.filter(category_id=category_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty Product queryset
        elif self.instance.pk:
            self.fields['product'].queryset = self.instance.category.product_set.order_by('productname')
# ****** End for Dependent DropDown List


NewOrderItemFormSet = inlineformset_factory(Order, OrderItem,
                                 # # fields='__all__',
                                 fields=['product', 'labordelivery', 'qty', 'numworkstation', 'numserver', 'numipaddress', 'desc'],
                                 # exclude=('total_price',),
                        extra=5)  # access both customer and order form


# ***** Start for Dependent DropDown List ******
#                         def __init__(self, *args, **kwargs):
#                             super().__init__(*args, **kwargs)
#                             self.fields['product'].queryset = Product.objects.none()
#
#                             if 'category' in self.data:
#                                 try:
#                                     category_id = int(self.data.get('category'))
#                                     self.fields['product'].queryset = Product.objects.filter(category_id=category_id).order_by('name')
#                                 except (ValueError, TypeError):
#                                     pass  # invalid input from the client; ignore and fallback to empty Product queryset
#                             elif self.instance.pk:
#                                 self.fields['product'].queryset = self.instance.category.product_set.order_by('productname')
    # ****** End for Dependent DropDown List




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




