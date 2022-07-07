from django.contrib.admin.views.decorators import staff_member_required
from django.db import transaction
from django.db.models import Sum
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django_tables2 import RequestConfig

from product.models import Product, Category, Prodvendor
from .tables import ProductTable, SizerItemTable, SizerTable
from .forms import SizerItemFormSet, SizerEditForm, SizerItemForm
from .models import Sizer, SizerItem


class SizerList(ListView):
    model = Sizer


class SizerCreate(CreateView):
    model = Sizer
    fields = ['title', 'date']


class SizerSizerItemCreate(CreateView):
    model = Sizer
    fields = ['title', 'date']
    success_url = reverse_lazy('sizer-list')

    def get_context_data(self, **kwargs):
        data = super(SizerSizerItemCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['sizeritems'] = SizerItemFormSet(self.request.POST)
        else:
            data['sizeritems'] = SizerItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        sizeritems = context['sizeritems']
        with transaction.atomic():
            self.object = form.save()

            if sizeritems.is_valid():
                sizeritems.instance = self.object
                sizeritems.save()
        return super(SizerSizerItemCreate, self).form_valid(form)


@method_decorator(staff_member_required, name='dispatch')
class SizerUpdate(UpdateView):
    model = Sizer
    success_url = '/'
    form_class = SizerEditForm
    fields = ['title', 'date']
    sizer_num = Sizer.id

    categories = Category.objects.all()
    total_categories = categories.count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        instance = self.object
        qs_p = Product.objects.filter(active=True)[:1000]
        products = ProductTable(qs_p)
        sizer_items = SizerItemTable(instance.sizer_items.all())
        # sizeritems = SizerItems.objects.all()  # show the list
        # sizeritems = sizeritems.count()

        categories = Category.objects.all()
        total_categories = categories.count()

        prods = Product.objects.all()
        total_prods = prods.count()

        Sizer.objects.annotate(
            sumworkstation=Sum('sizer_items__numworkstation', sumnumserver=Sum('sizer_items__numserver'),
                               sumipaddress=Sum('sizer_items__numipaddress')))

        RequestConfig(self.request).configure(products)
        RequestConfig(self.request).configure(sizer_items)

        context.update(locals())
        return context

    def save(self, *args, **kwargs):

        super().save(*args, **kwargs)
        self.sizer.save()


class SizerSizerItemUpdate(UpdateView):
    model = Sizer
    fields = ['title', 'date']
    success_url = reverse_lazy('sizer-list')

    def get_context_data(self, **kwargs):
        instance = self.object
        sizer_items = SizerItemTable(instance.sizer_items.all())
        data = super(SizerSizerItemUpdate, self).get_context_data(**kwargs)
        Sizer.objects.annotate(
            sumworkstation=Sum('sizer_items__numworkstation', sumnumserver=Sum('sizer_items__numserver'),
                               sumipaddress=Sum('sizer_items__numipaddress')))

        RequestConfig(self.request).configure(sizer_items)


        if self.request.POST:
            data['sizeritems'] = SizerItemFormSet(self.request.POST, instance=self.object)
        else:
            data['sizeritems'] = SizerItemFormSet(instance=self.object)

        return data

    def form_valid(self, form):
        context = self.get_context_data()
        sizeritems = context['sizeritems']
        with transaction.atomic():
            self.object = form.save()

            if sizeritems.is_valid():
                sizeritems.instance = self.object
                sizeritems.save()
        return super(SizerSizerItemUpdate, self).form_valid(form)


class SizerDelete(DeleteView):
    model = Sizer
    success_url = reverse_lazy('sizer-list')


#   ***** Start of Expense Tracker  *****

class EpenseDashboardListView(ListView):
    template_name = 'dashboard.html'
    paginate_by = 20

