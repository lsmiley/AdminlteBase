from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.utils.decorators import method_decorator
from django.views.generic import (
    View,
    CreateView,
    UpdateView
)
from rest_framework import viewsets
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from product.models import Category
from .models import Testquestionnaire
from .serializers import TestquestionnaireSerializer
from .forms import TestquestionnaireForm, TestquestionnaireCreateForm
from django_filters.views import FilterView
from .filters import TestquestionnaireFilter

# PDF Requirements
# from io import BytesIO
from .process import html_to_pdf
from django.template.loader import render_to_string
# from django.template.loader import get_template


class TestquestionnaireListView(FilterView):
    filterset_class = TestquestionnaireFilter
    queryset = Testquestionnaire.objects.filter()
    template_name = 'testquestionnaire.html'
    paginate_by = 20


class TestquestionnaireCreateView(SuccessMessageMixin, CreateView):  # createview class to add new testquestionnaire, mixin used to display message
    model = Testquestionnaire  # setting 'Testquestionnaire' model as model
    form_class = TestquestionnaireForm  # setting 'TestquestionnaireForm' form as form
    template_name = "edit_testquestionnaire.html"  # 'edit_testquestionnaire.html' used as the template
    success_url = '/testquestionnaire'  # redirects to 'testquestionnaire' page in the url after submitting the form
    success_message = "Testquestionnaire has been created successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'New Testquestionnaire'
        context["savebtn"] = 'Add to Testquestionnaire'
        return context


class TestquestionnaireUpdateView(SuccessMessageMixin, UpdateView):  # updateview class to edit testquestionnaire, mixin used to display message
    model = Testquestionnaire  # setting 'Testquestionnaire' model as model
    form_class = TestquestionnaireForm  # setting 'TestquestionnaireForm' form as form
    template_name = "edit_testquestionnaire.html"  # 'edit_testquestionnaire.html' used as the template
    success_url = '/testquestionnaire'  # redirects to 'testquestionnaire' page in the url after submitting the form
    success_message = "Testquestionnaire has been updated successfully"  # displays message when form is submitted

    def get_context_data(self, **kwargs):  # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Testquestionnaire'
        context["savebtn"] = 'Update Testquestionnaire'
        context["delbtn"] = 'Delete Testquestionnaire'
        return context


class TestquestionnaireDeleteView(View):  # view class to delete testquestionnaire
    template_name = "delete_testquestionnaire.html"  # 'delete_testquestionnaire.html' used as the template
    success_message = "Testquestionnaire has been deleted successfully"  # displays message when form is submitted

    def get(self, request, pk):
        testquestionnaire = get_object_or_404(Testquestionnaire, pk=pk)
        return render(request, self.template_name, {'object': testquestionnaire})

    def post(self, request, pk):
        testquestionnaire = get_object_or_404(Testquestionnaire, pk=pk)
        testquestionnaire.is_deleted = True
        testquestionnaire.save()
        messages.success(request, self.success_message)
        return redirect('testquestionnaire')


class TestquestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Testquestionnaire.objects.all().order_by('id')
    serializer_class = TestquestionnaireSerializer

# Create your views here.


@method_decorator(staff_member_required, name='dispatch')
class CreateTestquestionnaireView(CreateView):
    template_name = 'form_testquestionnaire.html'
    form_class = TestquestionnaireCreateForm
    model = Testquestionnaire

    # products = Product.objects.all()
    # total_products = products.count()
    #
    # qs_p = Product.objects.filter(active=True)[:12]
    # products = ProductTable(qs_p)

    def get_success_url(self):
        self.new_object.refresh_from_db()
        return reverse('update_testquestionnaire', kwargs={'pk': self.new_object.id})

    def form_valid(self, form):
        object = form.save()
        object.refresh_from_db()
        self.new_object = object
        return super().form_valid(form)


# # Creating a class based view
# class TestGeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         # getting the template
#         pdf = html_to_pdf('testpdf.html')
#
#         # rendering the template
#         return HttpResponse(pdf, content_type='application/pdf')
#
#
# # Creating a class based view
# class Testgeneratequestionnairepdf(View):
#     def get(self, request, *args, **kwargs):
#         # getting the template
#         pdf = html_to_pdf('testquestionnairepdf.html')
#
#         # rendering the template
#         # return HttpResponse(pdf, content_type='application/pdf')
#
#         return HttpResponseRedirect('/testgeneratequestionnairepdf', pdf, content_type='application/pdf')
