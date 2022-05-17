from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django_tables2 import RequestConfig
from rest_framework import viewsets
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from order.models import OrderItem, Order
from questionnaire.tables import ProductTable, QuestionnaireItemTable
from product.models import Product
from .serializers import OrderItemSerializer
from .forms import OrderItemForm
from order.forms import OrderEditForm, NewOrderItemFormSet
from django_filters.views import FilterView
from .filters import OrderItemFilter
from django.forms import inlineformset_factory  # Facilitates multiple form in group


def create(request, oid):
    '''Below I replace OrderForm with'''

    OrderItemFormSet = inlineformset_factory(Order, OrderItem, fields='__all__', exclude=('total_price',),
                                         extra=1)  # access both customer and order form

    # it means maila customer lai click garda order ma bhako detail access garako xu with instance of customer
    # parent model and then child model---
    # we can have multiple order so we need to tell which to allow by fields

    ordr = Order.objects.get(pk=oid)
    formset = OrderItemFormSet(queryset=OrderItem.objects.none(),
                           instance=ordr)  # i pass instance because i am adding order of particular customer
    # print(formset)

    # queryset =Order.objects.none() la --> already bhako product inline form ma show hudaina maila Add order ma jada
    # form = OrderForm(initial={'customer':cus})#right customer is in model--comment this wh

    if request.method == 'POST':
        # form = OrderForm(request.POST)
        formset = OrderItemFormSet(request.POST, instance=ordr)
        if formset.is_valid():
            formset.save()
        messages.success(request, "Your Sizing's Product is successfully added", extra_tags='alert')
        # return redirect('customer_app:view', oid)
        return redirect('update_order', oid)

    return render(request, 'orderitem/create.html', {'formset': formset, 'order': ordr})

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
            messages.success(request, 'OrderItem is successfully updates.', extra_tags='alert')

            return redirect('order/view', cid)

            # return redirect("/customers/order/", pk = cid)#maila update.html ko save garda or post ma jada yo url ma redirect hunxa

    # else:
    #     form = ProductForm()

    return render(request, 'orderitem/update_orderitem.html', {'form': form, 'order_record': order})



class OrderItemListView(FilterView):
    filterset_class = OrderItemFilter
    queryset = OrderItem.objects.filter()
    template_name = 'orderitem.html'
    paginate_by = 20


class OrderItemCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new orderitem, mixin used to display message
    model = OrderItem  # setting 'OrderItem' model as model
    form_class = OrderItemForm  # setting 'OrderItemForm' form as form
    template_name = "edit_orderitem.html"  # 'edit_orderitem.html' used as the template
    success_url = 'orderitem'  # redirects to 'orderitem' page in the url after submitting the form
    success_message = "OrderItem has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New OrderItem'
        context["savebtn"] = 'Add to OrderItem'
        return context

# ************ Start Of: Inserted as a Test ****************
# @login_required(login_url="/login_user/")
# def edit_orderitem(request):
#     if request.method!="POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         orderitem = OrderItem.objects.get(id=request.POST.get('id', ''))
#         if orderitem == None:
#             return HttpResponse("<h2>OrderItem Not Found</h2>")
#         else:
#             order = Order.order.id
#             orderitem.numworkstation = request.POST.get('numworkstation', '')
#             orderitem.numserver = request.POST.get('numserver', '')
#             orderitem.numipaddress = request.POST.get('numipaddress', '')
#             orderitem.nummonths = request.POST.get('nummonths', '')
#             orderitem.labordelivery = request.POST.get('labordelivery', '')
#             orderitem.save()
#
#             messages.success(request, "Updated Successfully")
#             return HttpResponseRedirect("update_orderitem/"+str(orderitem.id)+"")
#             return HttpResponseRedirect("order/"+str(order.id)+"")
#
#
# def edit(request):
#     if request.method!="POST":
#         return HttpResponse("<h2>Method Not Allowed</h2>")
#     else:
#         orderitem = OrderItem.objects.get(id=request.POST.get('id', ''))
#         if orderitem == None:
#             return HttpResponse("<h2>OrderItem Not Found</h2>")
#         else:
#             order = Order.order.id
#             orderitem.numworkstation = request.POST.get('numworkstation', '')
#             orderitem.numserver = request.POST.get('numserver', '')
#             orderitem.numipaddress = request.POST.get('numipaddress', '')
#             orderitem.nummonths = request.POST.get('nummonths', '')
#             orderitem.labordelivery = request.POST.get('labordelivery', '')
#             orderitem.save()
#
#             messages.success(request, "Updated Successfully")
#             return HttpResponseRedirect("update_orderitem/"+str(orderitem.id)+"")
#             return HttpResponseRedirect("order/"+str(order.id)+"")
# ************ End Of: Inserted as a Test ****************

class OrderItemUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit orderitem, mixin used to display message
    model = OrderItem  # setting 'OrderItem' model as model
    form_class = OrderItemForm  # setting 'OrderItemForm' form as form
    order_num = Order.id

    template_name = "edit_orderitem.html"  # 'edit_orderitem.html' used as the template
    success_url = '/update_order order.id'  # redirects to 'orderitem' page in the url after submitting the form
    # success_url = HttpResponseRedirect(next)
    success_message = "OrderItem has been updated successfully"  # displays message when form is submitted


    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit OrderItem'
        context["savebtn"] = 'Update OrderItem'
        context["delbtn"] = 'Delete OrderItem'
        return context

# ************** Start - Code to return to Update View  *************
@method_decorator(staff_member_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderEditForm
    order_num = Order.id

    def get_success_url(self):
        return reverse('update_order', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.object
        qs_p = Product.objects.filter(active=True)[:12]
        products = ProductTable(qs_p)
        order_items = OrderItemTable(instance.order_items.all())
        # orderitems = OrderItem.objects.all()  # show the list
        # orderitem_count = orderitems.count()
        RequestConfig(self.request).configure(products)
        RequestConfig(self.request).configure(order_items)
        context.update(locals())
        return context

# ************** End - Code to return to Update View  *************

class OrderItemDeleteView(View):  # view class to delete orderitem
    template_name = "delete_orderitem.html"  # 'delete_orderitem.html' used as the template
    success_message = "OrderItem has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        return render(request, self.template_name, {'object': orderitem})

    def post(self, request, pk):
        orderitem = get_object_or_404(OrderItem, pk=pk)
        orderitem.is_deleted = True
        orderitem.save()
        messages.success(request, self.success_message)
        return redirect('orderitem')

    class OrderItemViewSet(viewsets.ModelViewSet):
        queryset = OrderItem.objects.all().order_by('id')
        serializer_class = OrderItemSerializer


class OrderUpdate2View(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderEditForm

    def get_success_url(self):
        return reverse('update_order2', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.object
        qs_p = Product.objects.filter(active=True)[:12]
        products = ProductTable(qs_p)
        order_items = OrderItemTable(instance.order_items.all())
        # orderitems = OrderItem.objects.all()  # show the list
        # orderitem_count = orderitems.count()
        RequestConfig(self.request).configure(products)
        RequestConfig(self.request).configure(order_items)
        context.update(locals())
        return context
