from django import forms

from .models import Testquestionnaire, TestquestionnaireItem

class BaseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TestquestionnaireForm(forms.ModelForm):
    class Meta:
        model = Testquestionnaire
        fields = [
            "date",
            "title",
            "rfs_num",
            "sales_connect_num",
            "appttus_num",
            "sizingtype",
            "due_date",
            "PricingStructureSelect",
            "team",
            "assigned_by",
            "assigned_to",
            "RequesterFirstName",
            "RequesterLastName",
            "RequesterRole",
            "RequesterEmail",
            "CustomerName",
            "CustomerStatus",
            "Solution_Design",
            "SalesContactName",
            "SalesContactEmail",
            "TranStartDate",
            "Firm_Price_or_NBIE",
            "Service_Delivery_Requirements",
            "Solution_Owner",
            "Revenue_Structure_Select",
            "Revenue_Structure_Cost_Explain",
            "Restricted_Delivery",
            "Restricted_Delivery_Explanation",
            "Questionnaire_num_consoles",
            "Questionnaire_num_workstation",
            "Questionnaire_num_server",
            "Questionnaire_num_ipaddress",
            "Questionnaire_num_total_endpoints",
            "AntiVirusMalware",
            "DLP_on_Workstations",
            "DLP_on_Servers",
            "Encryption_on_Workstations",
            "Encryption_on_Servers",
            "prodcomponent1_wkstn",
            "NAS_Storage",
            "Windows",
            "AIX",
            "VDI",
            "URL_Filtering",
            "HIPs_on_Workstations",
            "HIPs_on_Servers",
            "Firewall_on_Workstations",
            "Firewall_on_Servers",
            "BigFix_Patching_Scanning",
            "Linux",
            "Integrity_Monitoring",
            "Citrix",
            "Other_Features_or_Platforms",
            "Other_Features_or_Platforms_Note",
            "Environment_and_Platforms_Note",
            "EmsServiceRequested",
        ]

        widgets = {


            'RequesterFirstName': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
            'RequesterLastName': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
            'RequesterEmail': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
            'due_date': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),

            'date': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
            'TranStartDate': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),

            'AntiVirusMalware': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'DLP_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'DLP_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Encryption_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Encryption_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'NAS_Storage': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Windows': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'AIX': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'VDI': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'URL_Filtering': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'HIPs_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'HIPs_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Firewall_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Firewall_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'BigFix_Patching_Scanning': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Linux': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Integrity_Monitoring': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Citrix': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Other_Features_or_Platforms': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Restricted_Delivery': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),

        }

    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

            # Requester's Infor section
            self.fields['title'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['RequesterFirstName'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['RequesterLastName'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['team'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['RequesterRole'].widget.attrs['style'] = 'width:110px; height:25px; font-size: 12px;'
            self.fields['RequesterEmail'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['due_date'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['date'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'

            self.fields['CustomerStatus'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'



            self.fields['PricingStructureSelect'].widget.attrs[
                'style'] = 'width:120px; height:25px; font-size: 12px;'

            # Customer's Infor section
            self.fields['CustomerName'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
            self.fields['SalesContactName'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
            self.fields['SalesContactEmail'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
            self.fields['TranStartDate'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
            self.fields['rfs_num'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
            self.fields['appttus_num'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
            self.fields['Revenue_Structure_Select'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
            self.fields['Revenue_Structure_Cost_Explain'].widget.attrs[
                'style'] = 'width:160px; height:25px; font-size: 12px;'
            self.fields['Solution_Design'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
            self.fields['Solution_Owner'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
            self.fields['Service_Delivery_Requirements'].widget.attrs[
                'style'] = 'width:160px; height:25px; font-size: 12px;'
            # self.fields['Restricted_Delivery'].widget.attrs['style'] = 'width:120px; height:20px; font-size: 12px;'

            self.fields['Revenue_Structure_Cost_Explain'].widget.attrs[
                'style'] = 'width:120px; height:25px; font-size: 12px;'

            # self.fields['prepardedby'].widget.attrs['style'] = 'width:120px; height:20px; font-size: 10px;'
            self.fields['Questionnaire_num_consoles'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['Questionnaire_num_workstation'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['Questionnaire_num_server'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['Questionnaire_num_ipaddress'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'
            self.fields['Questionnaire_num_total_endpoints'].widget.attrs['style'] = 'width:100px; height:25px; font-size: 12px;'


class TestquestionnaireItemForm(forms.ModelForm):
    class Meta:
        model = TestquestionnaireItem
        fields = [
            "qty",
            "price",
            "discount_price",
            "base",
            "discount_base",
            "fte",
            "discount_fte",
            "numworkstation",
            "numserver",
            "numipaddress",
            "total_endpoints",
            "desc",
            "numappchange",
            "srvshourscalc",
            "deliveryoption",
            "regions",
            "currencytype",
            "defaultfte_year",
            "workweek",
            "deliveryctrcostfactor",
            "band2count",
            "band2percentage",
            "band3count",
            "band3percentage",
            "band4count",
            "band4percentage",
            "band5count",
            "band5percentage",
            "band6count",
            "band6percentage",
            "band7count",
            "band7percentage",
            "band8count",
            "band8percentage",
            "band9count",
            "band9percentage",
            "band10count",
            "band10percentage",
            "bandstotalcount",
            "bandstotalpercentage",
            "nummonths",
            "prodcomponent1_wkstn",
            "prodcomponent1_wkstnhours",
            "prodcomponent1_svrHours",
            "prodcomponent1_iphours",
            "prodcomponent2_wkstn",
            "prodcomponent2_wkstnhours",
            "prodcomponent2_svrHours",
            "prodcomponent2_iphours",
            "prodcomponent3_wkstn",
            "prodcomponent3_wkstnhours",
            "prodcomponent3_svrHours",
            "prodcomponent3_iphours",
            "prodcomponent4_wkstn",
            "prodcomponent4_wkstnhours",
            "prodcomponent4_svrHours",
            "prodcomponent4_iphours",
            "prodcomponent5_wkstn",
            "prodcomponent5_wkstnhours",
            "prodcomponent5_svrHours",
            "prodcomponent5_iphours",
            "prodcomponent6_wkstn",
            "prodcomponent6_wkstnhours",
            "prodcomponent6_svrHours",
            "prodcomponent6_iphours",
            "prodcomponent7_wkstn",
            "prodcomponent7_wkstnhours",
            "prodcomponent7_svrHours",
            "prodcomponent7_iphours",
            "prodcomponent8_wkstn",
            "prodcomponent8_wkstnhours",
            "prodcomponent8_svrHours",
            "prodcomponent8_iphours",
            "prodcomponent9_wkstn",
            "prodcomponent9_wkstnhours",
            "prodcomponent9_svrHours",
            "prodcomponent9_iphours",
            "prodcomponent10_wkstn",
            "prodcomponent10_wkstnhours",
            "prodcomponent10_svrHours",
            "prodcomponent10_iphours",
            "prodcomponent11_wkstn",
            "prodcomponent11_wkstnhours",
            "prodcomponent11_svrHours",
            "prodcomponent11_iphours",
            "prodcomponent12_wkstn",
            "prodcomponent12_wkstnhours",
            "prodcomponent12_svrHours",
            "prodcomponent12_iphours",
            "prodcomponent13_wkstn",
            "prodcomponent13_wkstnhours",
            "prodcomponent13_svrHours",
            "prodcomponent13_iphours",
            "prodcomponent14_wkstn",
            "prodcomponent14_wkstnhours",
            "prodcomponent14_svrHours",
            "prodcomponent14_iphours",
            "prodcomponent15_wkstn",
            "prodcomponent15_wkstnhours",
            "prodcomponent15_svrHours",
            "prodcomponent15_iphours",
            "softlifesvryesno",
            "softlifesrvhourscalc",
            "prodimage",
        ]


class TestquestionnaireCreateForm(BaseForm, forms.ModelForm):
    # date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    TranStartDate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # aix = forms.BooleanField(widget=forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}))
    # Other_Features_or_Platforms_Note = CKEditorWidget(attrs={'toolbar': 'Basic', 'height': 70, 'width': 430,})
    # AntiVirusMalware = forms.BooleanField()

    class Meta:
        model = Testquestionnaire
        fields = ['date',
                  'title',
                  'due_date',
                  # 'prepardedby',
                  'team',
                  'RequesterFirstName',
                  'RequesterLastName',
                  'RequesterRole',
                  'RequesterEmail',
                  'CustomerName',
                  'SalesContactName',
                  'SalesContactEmail',
                  'TranStartDate',
                  'Revenue_Structure_Select',
                  'Revenue_Structure_Cost_Explain',
                  'rfs_num',
                  'appttus_num',
                  'Solution_Design',
                  'Solution_Owner',
                  'Service_Delivery_Requirements',
                  'Restricted_Delivery',
                  'Questionnaire_num_consoles',
                  'Questionnaire_num_workstation',
                  'Questionnaire_num_server',

                  'AntiVirusMalware',
                  'DLP_on_Workstations',
                  'DLP_on_Servers',
                  'Encryption_on_Workstations',
                  'Encryption_on_Servers',
                  'NAS_Storage',
                  'Windows',
                  'AIX',
                  'VDI',
                  'URL_Filtering',
                  'HIPs_on_Workstations',
                  'HIPs_on_Servers',
                  'Firewall_on_Workstations',
                  'Firewall_on_Servers',
                  'BigFix_Patching_Scanning',
                  'Linux',
                  'Integrity_Monitoring',
                  'Citrix',
                  'Other_Features_or_Platforms',
                  'Other_Features_or_Platforms_Note',

                  ]

        widgets = {


            'RequesterFirstName': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
            'RequesterLastName': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
            'RequesterEmail': forms.TextInput(attrs={'style': 'width:160px;height:25px; align:center;'}),
            'due_date': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),

            'date': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),
            'TranStartDate': forms.DateInput(attrs={'style': 'width:160px;height:20px; align:center;'}),

            'AntiVirusMalware': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'DLP_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'DLP_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Encryption_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Encryption_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'NAS_Storage': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Windows': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'AIX': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'VDI': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'URL_Filtering': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'HIPs_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'HIPs_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Firewall_on_Workstations': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Firewall_on_Servers': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'BigFix_Patching_Scanning': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Linux': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Integrity_Monitoring': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Citrix': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Other_Features_or_Platforms': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),
            'Restricted_Delivery': forms.CheckboxInput(attrs={'style': 'width:20px;height:20px; align:center;'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Customer's Infor section
        self.fields['CustomerName'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['SalesContactName'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['SalesContactEmail'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['TranStartDate'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['rfs_num'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['appttus_num'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['Revenue_Structure_Select'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
        self.fields['Revenue_Structure_Cost_Explain'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
        self.fields['Solution_Design'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
        self.fields['Solution_Owner'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
        self.fields['Service_Delivery_Requirements'].widget.attrs['style'] = 'width:160px; height:25px; font-size: 12px;'
        # self.fields['Restricted_Delivery'].widget.attrs['style'] = 'width:120px; height:20px; font-size: 12px;'
        self.fields['Revenue_Structure_Cost_Explain'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'

        # self.fields['prepardedby'].widget.attrs['style'] = 'width:120px; height:20px; font-size: 10px;'
        self.fields['Questionaire_num_consoles'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['Questionaire_num_workstation'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
        self.fields['Questionaire_num_server'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'
