from django import forms
from order.models import OrderItem, Product


class OrderItemForm(forms.ModelForm):

    class Meta:
        model = OrderItem
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.none()
    #
    #     if 'category' in self.data:
    #         try:
    #             category_id = int(self.data.get('category'))
    #             self.fields['product'].queryset = Product.objects.filter(category_id=category_id).order_by('categoryname')
    #         except (ValueError, TypeError):
    #             pass  # invalid input from the client; ignore and fallback to empty City queryset
    #     elif self.instance.pk:
    #         self.fields['product'].queryset = self.instance.category.product_set.order_by('productname')
    #