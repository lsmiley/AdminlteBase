from django import forms
from product.models import Product, Category


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'active': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'title': forms.TextInput(attrs={'style': 'width:120px;height:25px; align:center;'}),
            'productname': forms.TextInput(attrs={'style': 'width:120px;height:25px; align:center;'}),
            'productdesc': forms.TextInput(attrs={'style': 'width:180px;height:25px; align:center;'}),
            'category': forms.Select(attrs={'style': 'width:120px;height:20px; align:center;'}),
            'prodvendor': forms.Select(attrs={'style': 'width:120px;height:20px; align:center;'}),

            'productcomplexitybase': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'totalcomplexity': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'productcomplexityfac': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),

            'numcomponent': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            # 'primarycomp': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'primarycomplexity': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),


            # Component #1
            'component1': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component1desc': forms.TextInput(attrs={'style': 'width:95px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs1': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac1': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours1': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component1_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component1_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component1_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component1_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent1note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent1technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #2
            'component2': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component2desc': forms.TextInput(attrs={'style': 'width:95px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs2': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac2': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours2': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component2_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component2_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component2_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component2_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent2note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent2technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #3
            'component3': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component3desc': forms.TextInput(attrs={'style': 'width:95px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs3': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac3': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours3': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'component3_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component3_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component3_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component3_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent3note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent3technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #4
            'component4': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component4desc': forms.TextInput(attrs={'style': 'width:95px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs4': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac4': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours4': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component4_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component4_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'cComponent4_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component4_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent4note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent4technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #5
            'component5': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component5desc': forms.TextInput(attrs={'style': 'width:95px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs5': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac5': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours5': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component5_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component5_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component5_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component5_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent5note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent5technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #6
            'component6': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component6desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs6': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac6': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours6': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component6_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component6_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component6_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component6_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent6note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent6technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #7
            'component7': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component7desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs7': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac7': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours7': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component7_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component7_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component7_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component7_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent7note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent7technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #8
            'component8': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component8desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs8': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac8': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours8': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component8_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component8_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component8_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component8_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent8note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent8technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #9
            'component9': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component9desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs9': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac9': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours9': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component9_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component9_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component9_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component9_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent9note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent9technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            # Component #10
            'component10': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component10desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs10': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac10': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours10': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component10_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component10_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component10_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component10_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent10note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent10technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            'component11': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component11desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs11': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac11': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours11': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component11_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component11_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component11_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component11_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent11note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent11technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            'component12': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component12desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs12': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac12': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours12': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component12_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component12_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component12_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component12_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent12note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent12technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            'component13': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component13desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs13': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac13': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours13': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component13_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component13_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component13_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component13_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent13note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent13technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            'component14': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component14desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs14': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac14': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours14': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component14_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component14_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component14_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component14_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent14note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent14technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

            'component15': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'component15desc': forms.TextInput(attrs={'style': 'width:105px;height:20px; align:center; font-size: 9px;'}),
            'componentcomplexityhrs15': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'componentcomplexityfac15': forms.NumberInput(attrs={'style': 'width:60px;height:20px; align:center; font-size: 9px; text-align:center'}),
            'ComponentHours15': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'Component15_Wkstn': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component15_Svr': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component15_IP': forms.CheckboxInput(attrs={'style': 'width:20px;height:12px; align:center;'}),
            'Component15_Qty': forms.NumberInput(attrs={'style': 'width:80px;height:20px; align:center;'}),
            'memocomponent15note': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),
            'memocomponent15technote': forms.Textarea(attrs={'style': 'width:80px;height:60px; align:center; font-size: 9px;'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # self.fields['productname'].widget.attrs['style'] = 'width:120px; height:25px; font-size: 12px;'

        # Component #1
        # self.fields['Component1_Wkstn'].widget = forms.HiddenInput()
        # self.fields['Component1_Svr'].widget = forms.HiddenInput()
        # self.fields['Component1_IP'].widget = forms.HiddenInput()
        # self.fields['Component1_Qty'].widget = forms.HiddenInput()

