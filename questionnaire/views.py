from django.contrib.messages.views import SuccessMessageMixin
from django.http import JsonResponse, HttpResponse, QueryDict, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, View
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.urls import reverse_lazy
from django.db.models import Q
from django.template import loader
from django.contrib import messages
from django.template.loader import render_to_string
# from django.http import JsonResponse, HttpResponse, QueryDict, HttpResponseRedirect
from django.db.models import Sum
from django.views.generic.detail import SingleObjectMixin
from django_tables2 import RequestConfig
from rest_framework.templatetags.rest_framework import data

from django.core.files.storage import FileSystemStorage
from xhtml2pdf import pisa

from .models import Questionnaire, QuestionnaireItem, CURRENCY

from product import models

from django_filters.views import FilterView
from .filters import QuestionnaireFilter, DashboardQuestionnaireFilter


from .forms import QuestionnaireCreateForm, QuestionnaireForm, QuestionnaireEditForm, QuestionnaireItemEditForm, QuestionnaireItemForm, QuestionnaireCreateForm
from product.models import Product, Category, Prodvendor
from acctcust.models import Acctcust
from .tables import ProductTable, QuestionnaireItemTable, QuestionnaireTable
from .utils import set_pagination
from django.views.generic.edit import (
    FormView,
    View,
    CreateView,
    UpdateView
)


class QuestionnaireListView(FilterView):
    filterset_class = QuestionnaireFilter
    form_class = QuestionnaireForm
    queryset = Questionnaire.objects.filter()
    template_name = 'dashboard-questionaire.html'
    paginate_by = 20

@method_decorator(staff_member_required, name='dispatch')
class QuestionnaireCreateView(SuccessMessageMixin,
                             CreateView):  # createview class to add new questionnaire, mixin used to display message
    model = Questionnaire  # setting 'Product' model as model
    form_class = QuestionnaireForm  # setting 'QuestionnaireForm' form as form
    template_name = "edit_questionnaire.html"  # 'edit_questionnaire.html' used as the template
    success_url = 'questionnaire'  # redirects to 'questionnaire' page in the url after submitting the form
    success_message = "Questionnaire has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Questionnaire'
        context["savebtn"] = 'Add to Questionnaire'
        return context


class QuestionnaireUpdateView(SuccessMessageMixin,
                             UpdateView):  # updateview class to edit questionnaire, mixin used to display message
    model = Questionnaire  # setting 'Questionnaire' model as model
    form_class = QuestionnaireForm  # setting 'QuestionnaireForm' form as form
    template_name = "edit_questionnaire.html"  # 'edit_questionnaire.html' used as the template
    pk_url_kwarg = "pk"
    success_url = '/questionnaire/'  # redirects to 'questionnaire' page in the url after submitting the form
    success_message = "Questionnaire has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Questionnaire'
        context["savebtn"] = 'Update Questionnaire'
        context["delbtn"] = 'Delete Questionnaire'
        return context


class QuestionnaireDeleteView(View):  # view class to delete questionnaire
    template_name = "delete_questionnaire.html"  # 'delete_questionnaire.html' used as the template
    success_message = "Questionnaire has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        questionnaire = get_object_or_404(Questionnaire, pk=pk)
        return render(request, self.template_name, {'object': questionnaire})

    def post(self, request, pk):
        questionnaire = get_object_or_404(Questionnaire, pk=pk)
        questionnaire.is_deleted = True
        questionnaire.save()
        messages.success(request, self.success_message)
        return redirect('questionnaire')


@method_decorator(staff_member_required, name='dispatch')
class QuestionnaireUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit category, mixin used to display message
    model = Category  # setting 'Category' model as model
    form_class = QuestionnaireForm  # setting 'QuestionnaireForm' form as form
    template_name = "edit_questionnaire.html"  # 'edit_category.html' used as the template
    success_url = '/questionnaire'  # redirects to 'category' page in the url after submitting the form
    success_message = "Questionnaire has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Questionnaire'
        context["savebtn"] = 'Update Questionnaire'
        context["delbtn"] = 'Delete Questionnaire'
        return context



@method_decorator(staff_member_required, name='dispatch')
class CreateQuestionnaireView(CreateView):
    template_name = 'form_questionnaire.html'
    form_class = QuestionnaireCreateForm
    model = Questionnaire

    # questionnaires = Questionnaire.objects.all()
    # total_questionnaires = questionnaires.count()
    #
    # qs_p = Questionnaire.objects.filter(active=True)[:12]
    # questionnaires = QuestionnaireTable(qs_p)

    def get_success_url(self):
        self.new_object.refresh_from_db()
        return reverse('update_questionnaire', kwargs={'pk': self.new_object.id})

    def form_valid(self, form):
        object = form.save()
        object.refresh_from_db()
        self.new_object = object
        return super().form_valid(form)
