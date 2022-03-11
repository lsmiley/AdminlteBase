from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from .models import Sizingtype
from .forms import SizingtypeForm
from django_filters.views import FilterView
from .filters import SizingtypeFilter


class SizingtypeListView(FilterView):
    filterset_class = SizingtypeFilter
    queryset = Sizingtype.objects.filter()
    template_name = 'sizingtype.html'
    paginate_by = 10


class SizingtypeCreateView(SuccessMessageMixin, CreateView):  # createview class to add new sizingtype, mixin used to display message
    model = Sizingtype  # setting 'Sizingtype' model as model
    form_class = SizingtypeForm  # setting 'SizingtypeForm' form as form
    template_name = "edit_sizingtype.html"  # 'edit_sizingtype.html' used as the template
    success_url = '/sizingtype'  # redirects to 'sizingtype' page in the url after submitting the form
    success_message = "Sizingtype has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Sizingtype'
        context["savebtn"] = 'Add to Sizingtype'
        return context


class SizingtypeUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit sizingtype, mixin used to display message
    model = Sizingtype  # setting 'Sizingtype' model as model
    form_class = SizingtypeForm  # setting 'SizingtypeForm' form as form
    template_name = "edit_sizingtype.html"  # 'edit_sizingtype.html' used as the template
    success_url = '/sizingtype'  # redirects to 'sizingtype' page in the url after submitting the form
    success_message = "Sizingtype has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Sizingtype'
        context["savebtn"] = 'Update Sizingtype'
        context["delbtn"] = 'Delete Sizingtype'
        return context


class SizingtypeDeleteView(View):  # view class to delete sizingtype
    template_name = "delete_sizingtype.html"  # 'delete_sizingtype.html' used as the template
    success_message = "Sizingtype has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        sizingtype = get_object_or_404(Sizingtype, pk=pk)
        return render(request, self.template_name, {'object': sizingtype})

    def post(self, request, pk):
        sizingtype = get_object_or_404(Sizingtype, pk=pk)
        sizingtype.is_deleted = True
        sizingtype.save()
        messages.success(request, self.success_message)
        return redirect('sizingtype')
