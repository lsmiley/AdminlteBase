from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.db import transaction
from django.http import HttpResponse

from django_filters.views import FilterView
from .filters import SizingFilter



class SizingListView(FilterView):
    filterset_class = SizingFilter
    queryset = Sizing.objects.filter()
    template_name = 'base_sizer.html'
    paginate_by = 10


class HomepageView(TemplateView):
    template_name = "base_sizer.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sizings'] = Sizing.objects.order_by('id')
        return context


##########################################################################
#                           Sizing views                             #
##########################################################################


class SizingDetailView(DetailView):
    model = Sizing
    template_name = 'sizing_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SizingDetailView, self).get_context_data(**kwargs)
        return context




class SizingCreate(CreateView):
    model = Sizing
    template_name = 'sizing_create.html'
    form_class = SizingForm
    success_url = None

    def get_context_data(self, **kwargs):
        data = super(SizingCreate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = SizingItemFormSet(self.request.POST)
        else:
            data['items'] = SizingItemFormSet()
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(SizingCreate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sizing:sizing_detail', kwargs={'pk': self.object.pk})


class SizingUpdate(UpdateView):
    model = Sizing
    form_class = SizingForm
    template_name = 'sizing_create.html'

    def get_context_data(self, **kwargs):
        data = super(SizingUpdate, self).get_context_data(**kwargs)
        if self.request.POST:
            data['items'] = SizingItemFormSet(self.request.POST, instance=self.object)
        else:
            data['items'] = SizingItemFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        context = self.get_context_data()
        items = context['items']
        with transaction.atomic():
            form.instance.created_by = self.request.user
            self.object = form.save()
            if items.is_valid():
                items.instance = self.object
                items.save()
        return super(SizingUpdate, self).form_valid(form)

    def get_success_url(self):
        return reverse_lazy('sizing:sizing_detail', kwargs={'pk': self.object.pk})

    # @method_decorator(login_required)
    # def dispatch(self, *args, **kwargs):
    #     return super(SizingUpdate, self).dispatch(*args, **kwargs)


class SizingDelete(DeleteView):
    model = Sizing
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('homepage')

