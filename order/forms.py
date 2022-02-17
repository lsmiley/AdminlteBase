from django import forms

import labordelivery
from .models import Order, OrderItem




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


class OrderEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = Order
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

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

class OrderItemEditForm(BaseForm, forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'
