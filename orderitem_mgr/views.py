from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from order.models import OrderItem, Order
from product.models import Product, Category
from .forms import OrderItemForm
from order.forms import NewOrderItemFormSet

from django.forms import inlineformset_factory, NumberInput  # Facilitates multiple form in group



def create(request, oid):
    '''Below I replace OrderForm with'''

    OrderItemFormSet = inlineformset_factory(Order, OrderItem,
                                             # fields='__all__',
                                             fields=['product',
                                                     'labordelivery',
                                                     'qty',
                                                     'numworkstation',
                                                     'numserver',
                                                     'numipaddress',
                                                     'srvshourscalc',
                                                     'nummonths',
                                                     'base'],
                                             widgets={'qty': NumberInput(attrs={'style': 'width: 50px'}),
                                                      'numworkstation': NumberInput(attrs={'style': 'width: 75px'}),
                                                      'numserver': NumberInput(attrs={'style': 'width: 75px'}),
                                                      'numipaddress': NumberInput(attrs={'style': 'width: 75px'}),
                                                      'srvshourscalc': NumberInput(attrs={'type': 'hidden'}),
                                                      'nummonths': NumberInput(attrs={'style': 'width: 50px'}),
                                                      'base': NumberInput(attrs={'style': 'width: 50px'}),
                                                      },

                                             exclude=('total_price',),
                                         extra=2)  # access both customer and order form

    # it means maila customer lai click garda order ma bhako detail access garako xu with instance of customer
    # parent model and then child model---
    # we can have multiple order so we need to tell which to allow by fields

    category_context = Category.objects.all()

    product_context = Product.objects.all()

    # category_id = request.GET.get('category')
    # product1 = Product.objects.filter(category_id=category_id).order_by('productname')

    ordr = Order.objects.get(pk=oid)
    formset = OrderItemFormSet(queryset=OrderItem.objects.none(),
                           instance=ordr)  # i pass instance because i am adding order of particular customer
    # print(formset)

    # queryset =Order.objects.none() la --> already bhako product inline form ma show hudaina maila Add order ma jada
    # form = OrderForm(initial={'customer':cus})#right customer is in model--comment this wh

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['product'].queryset = Product.objects.filter(category_id=category_id).order_by('productname')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['product'].queryset = self.instance.category.product_set.order_by('productname')

    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST, instance=ordr)
        if formset.is_valid():
            formset.save()
        messages.success(request, "Your Sizing's Product is successfully added", extra_tags='alert')
        # return redirect('customer_app:view', oid)
        return redirect('update_order', oid)

    return render(request, 'orderitem/create.html', {'formset': formset, 'order': ordr, 'category': category_context, 'product':product_context})


# def load_products(request):
#     category_id = request.GET.get('category_id')
#     products = Product.objects.filter(category_id=category_id).order_by('productname')
#     return render(request, 'c.html', {'products': products})


#  ***** Start od Sample Code  *****

# def load_discipline_details(request):
#     institute_id = request.GET.get('institute_id')
#     disciplines = Discipline.objects.filter(institute=institute_id).order_by('name')
#     return render(request, 'load_discipline_dropdown_list.html', {'disciplines': disciplines})
#
#
# def load_macro_details(request):
#     discipline_id = request.GET.get('discipline_id')
#     disciplinemacrocontents = DisciplineMacroContent.objects.filter(discipline=discipline_id).order_by('macro_content')
#     return render(request, 'load_macro_dropdown_list.html', {'disciplinemacrocontents': disciplinemacrocontents})

#  ***** End of Sample Code  *****


def load_products(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id=category_id).all()
    return render(request, 'orderitem_mgr/product_dropdown_list_options.html', {'products': products})



def createnew(request, oid):
    '''Below I replace OrderForm with'''


    # it means maila customer lai click garda order ma bhako detail access garako xu with instance of customer
    # parent model and then child model---
    # we can have multiple order so we need to tell which to allow by fields

    ordr = Order.objects.get(pk=oid)
    formset = NewOrderItemFormSet(queryset=OrderItem.objects.none(),
                           instance=ordr)  # i pass instance because i am adding order of particular customer
    # print(formset)

    # queryset =Order.objects.none() la --> already bhako product inline form ma show hudaina maila Add order ma jada
    # form = OrderForm(initial={'customer':cus})#right customer is in model--comment this wh

    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = NewOrderItemFormSet(request.POST, instance=ordr)
        if formset.is_valid():
            formset.save()
        messages.success(request, "Your Sizing's Product is successfully added", extra_tags='alert')
        # return redirect('customer_app:view', oid)
        return redirect('update_order', oid)

    return render(request, 'orderitem/createnew.html', {'formset': formset, 'order': ordr})

def edit(request, cid, oid):
    # ord=Order.objects.get(pk=oid) #i get all value and show that value to next page

    ord = get_object_or_404(OrderItem, pk=oid)
    order = get_object_or_404(Order, pk=cid)

    form = OrderItemForm(instance=ord)

    # cus = get_object_or_404(Customer,pk = cid)

    if (request.method == 'POST'):

        form = OrderItemForm(request.POST, instance=ord)
        if (form.is_valid()):
            form.save()
            messages.success(request, 'Order is successfully updates.', extra_tags='alert')

            return redirect('customer_app:view', cid)

            # return redirect("/customers/order/", pk = cid)#maila update.html ko save garda or post ma jada yo url ma redirect hunxa

    # else:
    #     form = ProductForm()

    return render(request, 'orders/update.html', {'form': form, 'customer_record': customer})


