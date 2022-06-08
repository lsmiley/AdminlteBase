from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.db.models import Q
from django.template import loader
from django.contrib import messages
from django.template.loader import render_to_string
from django.http import JsonResponse, HttpResponse, QueryDict, HttpResponseRedirect
from django.db.models import Sum
from django_tables2 import RequestConfig
from rest_framework.templatetags.rest_framework import data

from order.models import Order, OrderItem, CURRENCY
from order.forms import OrderCreateForm, OrderEditForm, OrderItemEditForm, OrderItemForm
from order.tables import OrderTable
from product.models import Product, Prodvendor
from questionnaire.tables import ProductTable, QuestionnaireItemTable, QuestionnaireTable
from order.utils import set_pagination

from django.views.generic.edit import (
    View,
    CreateView,
    UpdateView
)


import datetime


@method_decorator(staff_member_required, name='dispatch')
class HomepageView(ListView):
    template_name = 'index.html'
    model = Order
    queryset = Order.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        total_sales = orders.aggregate(Sum('final_value'))['final_value__sum'] if orders.exists() else 0
        paid_value = orders.filter(is_paid=True).aggregate(Sum('final_value'))['final_value__sum']\
            if orders.filter(is_paid=True).exists() else 0
        remaining = total_sales - paid_value
        diviner = total_sales if total_sales > 0 else 1
        paid_percent, remain_percent = round((paid_value/diviner)*100, 1), round((remaining/diviner)*100, 1)
        total_sales = f'{total_sales} {CURRENCY}'
        paid_value = f'{paid_value} {CURRENCY}'
        remaining = f'{remaining} {CURRENCY}'
        orders = OrderTable(orders)
        RequestConfig(self.request).configure(orders)
        context.update(locals())
        return context


@staff_member_required
def auto_create_order_view(request):
    new_order = Order.objects.create(
        title='Order 66',
        date=datetime.datetime.now()

    )
    new_order.title = f'Order - {new_order.id}'
    new_order.save()
    return redirect(new_order.get_edit_url())


@method_decorator(staff_member_required, name='dispatch')
class DashboardMainView(ListView):
    template_name = 'dashboard-main.html'
    model = Order
    queryset = Order.objects.all()[:10]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = Order.objects.all()
        total_sales = orders.aggregate(Sum('final_value'))['final_value__sum'] if orders.exists() else 0
        paid_value = orders.filter(is_paid=True).aggregate(Sum('final_value'))['final_value__sum']\
            if orders.filter(is_paid=True).exists() else 0
        remaining = total_sales - paid_value
        diviner = total_sales if total_sales > 0 else 1
        paid_percent, remain_percent = round((paid_value/diviner)*100, 1), round((remaining/diviner)*100, 1)
        total_sales = f'{total_sales} {CURRENCY}'
        paid_value = f'{paid_value} {CURRENCY}'
        remaining = f'{remaining} {CURRENCY}'
        orders = OrderTable(orders)
        RequestConfig(self.request).configure(orders)
        context.update(locals())
        return context


@staff_member_required
def auto_create_order_view(request):
    new_order = Order.objects.create(
        title='Order 66',
        date=datetime.datetime.now()

    )
    new_order.title = f'Order - {new_order.id}'
    new_order.save()
    return redirect(new_order.get_edit_url())


@method_decorator(staff_member_required, name='dispatch')
class OrderListView(ListView):
    template_name = 'list.html'
    model = Order
    paginate_by = 50

    def get_queryset(self):
        qs = Order.objects.all()
        if self.request.GET:
            qs = Order.filter_data(self.request, qs)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = OrderTable(self.object_list)
        RequestConfig(self.request).configure(orders)
        context.update(locals())
        return context


@method_decorator(staff_member_required, name='dispatch')
class CreateOrderView(CreateView):
    template_name = 'form.html'
    form_class = OrderCreateForm
    model = Order

    def get_success_url(self):
        self.new_object.refresh_from_db()
        return reverse('update_order', kwargs={'pk': self.new_object.id})

    def form_valid(self, form):
        object = form.save()
        object.refresh_from_db()
        self.new_object = object
        return super().form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class OrderUpdateView(UpdateView):
    model = Order
    template_name = 'order_update.html'
    form_class = OrderEditForm

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


@method_decorator(staff_member_required, name='dispatch')
class GboUpdateView(UpdateView):
    model = Order
    template_name = 'gboitem.html'
    form_class = OrderEditForm

    def get_success_url(self):
        return reverse('update_gbo', kwargs={'pk': self.object.id})

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


@staff_member_required
def delete_order(request, pk):
    instance = get_object_or_404(Order, id=pk)
    instance.delete()
    messages.warning(request, 'The order is deleted!')
    return redirect(reverse('homepage'))


@staff_member_required
def done_order_view(request, pk):
    instance = get_object_or_404(Order, id=pk)
    instance.is_paid = True
    instance.save()
    return redirect(reverse('homepage'))


# @login_required(login_url="/login_user/")
def edit_orderitem(request):
    if request.method!="POST":
        return HttpResponse("<h2>Method Not Allowed</h2>")
    else:
        orderitem = OrderItem.objects.get(id=request.POST.get('id', ''))
        if orderitem == None:
            return HttpResponse("<h2>OrderItem Not Found</h2>")
        else:
            order_num = Order.id
            orderitem.numworkstation = request.POST.get('numworkstation', '')
            orderitem.numserver = request.POST.get('numserver', '')
            orderitem.numipaddress = request.POST.get('numipaddress', '')
            orderitem.nummonths = request.POST.get('nummonths', '')
            orderitem.labordelivery = request.POST.get('labordelivery', '')
            orderitem.save()

            messages.success(request, "Updated Successfully")
            # return HttpResponseRedirect("update_orderitem/"+str(orderitem.id)+"")
            return HttpResponseRedirect("update1/"+str(order_num)+"")


class OrderItemUpdateView(UpdateView):
    model = OrderItem
    fields = '__all__'
    template_name = "edit_orderitem.html"
    # template_name = 'orderitem_update.html'
    form_class = OrderItemEditForm


    def get_success_url(self):
        self.object.refresh_from_db()
        return reverse('edit_orderitem', kwargs={'pk': self.object.id})
        # return reverse('update_orderitem', kwargs={'pk': self.object.id})


class OrderItemView(View):
    context = {'segment': 'orderitems'}

    def get(self, request, pk=None, action=None):
        if request.is_ajax():
            if pk and action == 'edit':
                edit_row = self.edit_row(pk)
                return JsonResponse({'edit_row': edit_row})
            elif pk and not action:
                edit_row = self.get_row_item(pk)
                return JsonResponse({'edit_row': edit_row})

        if pk and action == 'edit':
            context, template = self.edit(request, pk)
        else:
            context, template = self.list(request)

        if not context:
            html_template = loader.get_template('page-500.html')
            return HttpResponse(html_template.render(self.context, request))

        return render(request, template, context)

    def post(self, request, pk=None, action=None):
        self.update_instance(request, pk)
        return redirect('orderitems')

    def put(self, request, pk, action=None):
        is_done, message = self.update_instance(request, pk, True)
        edit_row = self.get_row_item(pk)
        return JsonResponse({'valid': 'success' if is_done else 'warning', 'message': message, 'edit_row': edit_row})

    def delete(self, request, pk, action=None):
        orderitem = self.get_object(pk)
        orderitem.delete()

        redirect_url = None
        if action == 'single':
            messages.success(request, 'Item deleted successfully')
            redirect_url = reverse('orderitems')

        response = {'valid': 'success', 'message': 'Item deleted successfully', 'redirect_url': redirect_url}
        return JsonResponse(response)

    """ Get pages """

    def list(self, request):
        filter_params = None

        search = request.GET.get('search')
        if search:
            filter_params = None
            for key in search.split():
                if key.strip():
                    if not filter_params:
                        filter_params = Q(bill_for__icontains=key.strip())
                    else:
                        filter_params |= Q(bill_for__icontains=key.strip())

        orderitems = OrderItem.objects.filter(filter_params) if filter_params else OrderItem.objects.all()

        self.context['orderitems'], self.context['info'] = set_pagination(request, orderitems)
        if not self.context['orderitems']:
            return False, self.context['info']

        return self.context, 'app/orderitems/list.html'

    def edit(self, request, pk):
        orderitem = self.get_object(pk)

        self.context['orderitem'] = orderitem
        self.context['form'] = OrderItemForm(instance=orderitem)

        return self.context, 'app/orderitems/edit.html'

    """ Get Ajax pages """

    def edit_row(self, pk):
        orderitem = self.get_object(pk)
        form = OrderItemForm(instance=orderitem)
        context = {'instance': orderitem, 'form': form}
        return render_to_string('app/orderitems/edit_row.html', context)

    """ Common methods """

    def get_object(self, pk):
        orderitem = get_object_or_404(OrderItem, id=pk)
        return orderitem

    def get_row_item(self, pk):
        orderitem = self.get_object(pk)
        edit_row = render_to_string('app/orderitems/edit_row.html', {'instance': orderitem})
        return edit_row

    def update_instance(self, request, pk, is_urlencode=False):
        orderitem = self.get_object(pk)
        form_data = QueryDict(request.body) if is_urlencode else request.POST
        form = OrderItemForm(form_data, instance=orderitem)
        if form.is_valid():
            form.save()
            if not is_urlencode:
                messages.success(request, 'OrderItem saved successfully')

            return True, 'OrderItem saved successfully'

        if not is_urlencode:
            messages.warning(request, 'Error Occurred. Please try again.')
        return False, 'Error Occurred. Please try again.'


# AJAX
def load_products(request):
    category_id = request.GET.get('category_id')
    products = Product.objects.filter(category_id=category_id).all()
    return render(request, 'orderitem_mgr/product_dropdown_list_options.html', {'products': products})

