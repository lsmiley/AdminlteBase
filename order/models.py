from django.db import models
from django.utils import timezone
from django.db.models import Sum
from django.conf import settings
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_delete
import datetime
from django.db.models import F
from django.db.models import Sum

import labordelivery
from labordelivery.models import Labordelivery
from product.models import Product

from decimal import Decimal

CURRENCY = settings.CURRENCY


class OrderManager(models.Manager):

    def active(self):
        return self.filter(active=True)


class Order(models.Model):
    # date = models.DateField(default=datetime.datetime.now())
    date = models.DateTimeField(default=timezone.now)
    # date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(blank=True, max_length=150)
    timestamp = models.DateField(auto_now_add=True)
    value = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    final_value = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    is_paid = models.BooleanField(default=True)
    objects = models.Manager()
    browser = OrderManager()

    sum_numconsole = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_numserver = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_workstation = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_ipaddress = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_endpoint = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_fte = models.DecimalField(
        default=0.00,
        decimal_places=2,
        max_digits=20)

    sum_srvshourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_wkstnshourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_ipshourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    sum_consolehourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # **** TNTWorksgeet  ****

    tntdescription = models.CharField(max_length=150, blank=True,
                                      null=True)
    managementmod1stline = models.FloatField(default='0.0')
    managementmod2ndline = models.FloatField(default='0.0')
    totaltransitiontotalfte = models.FloatField(default='0.0')
    totaltransitiontotalhours = models.FloatField(default='0.0')
    totaltransitiontotalband8 = models.FloatField(default='0.0')
    totaltransitiontotal1stlinemgr = models.FloatField(default='0.0')
    totaltransitiontotal2ndlinemgr = models.FloatField(default='0.0')
    totaltransitiontotals = models.FloatField(default='0.0')
    totaltransformationtotalfte = models.FloatField(default='0.0')
    totaltransformationtotalhours = models.FloatField(default='0.0')
    totaltransformationtotalband8 = models.FloatField(default='0.0')
    totaltransformationtotal1stlinemgr = models.FloatField(default='0.0')
    totaltransformationtotal2ndlinemgr = models.FloatField(default='0.0')
    totaltransformationtotals = models.FloatField(default='0.0')
    transitionhoursfte = models.FloatField(default='0.0')
    transitionfirstlinemanagementband8 = models.FloatField(default='0.0')
    transitionsecondlinemanagementband8 = models.FloatField(default='0.0')
    transitionfirstlinemanagementband8weeks = models.FloatField(default='0.0')
    transitionsecondlinemanagementband8weeks = models.FloatField(default='0.0')
    transitionsubtotalshours = models.FloatField(default='0.0')
    transitionfirstlinemanagementband8hours = models.FloatField(default='0.0')
    transfortionhoursfte = models.FloatField(default='0.0')
    transformationfirstlinemanagementband8 = models.FloatField(default='0.0')
    transformationsecondlinemanagementband8 = models.FloatField(default='0.0')
    transformationfirstlinemanagementband8weeks = models.FloatField(
        default='0.0')
    transformationsecondlinemanagementband8weeks = models.FloatField(
        default='0.0')
    tranformationsubtotalshours = models.FloatField(default='0.0')
    transformationfirstlinemanagementband8hours = models.FloatField(
        default='0.0')
    transitionsubtotalshoursitems = models.FloatField(default='0.0')
    transformationsubtotalshoursitems = models.FloatField(default='0.0')

    executetransitionplan_count = models.FloatField(default='1.0')
    executetransitionplan_transitionhoursitem = models.FloatField(
        default='0.30')
    executetransitionplan_transitionhours = models.FloatField(default='0.0')
    executetransitionplan_transformationhoursitem = models.FloatField(
        default='250.0')
    executetransitionplan_transformationhours = models.FloatField(
        default='250.0')

    createbestpracticecustom_count = models.FloatField(default='1.0')
    createbestpracticecustom_transitionhoursitem = models.FloatField(
        default='40.0')
    createbestpracticecustom_transitionhours = models.FloatField(
        default='40.0')
    createbestpracticecustom_transformationhoursitem = models.FloatField(
        default='33.0')
    createbestpracticecustom_transformationhours = models.FloatField(
        default='33.0')

    testinfrastructurepoc_count = models.FloatField(default='1.0')
    testinfrastructurepoc_transitionhoursitem = models.FloatField(
        default='40.0')
    testinfrastructurepoc_transitionhours = models.FloatField(default='40.0')
    testinfrastructurepoc_transformationhoursitem = models.FloatField(
        default='33.0')
    testinfrastructurepoc_transformationhours = models.FloatField(
        default='33.0')

    troubleshoottune_count = models.FloatField(default='1.0')
    troubleshoottune_transitionhoursitem = models.FloatField(default='40.0')
    troubleshoottune_transitionhours = models.FloatField(default='40.0')
    troubleshoottune_transformationhoursitem = models.FloatField(
        default='33.0')
    troubleshoottune_transformationhours = models.FloatField(default='33.0')

    installconfigure_count = models.FloatField(default='1.0')
    installconfigure_transitionhoursitem = models.FloatField(default='40.0')
    installconfigure_transitionhours = models.FloatField(default='40.0')
    installconfigure_transformationhoursitem = models.FloatField(
        default='33.0')
    installconfigure_transformationhours = models.FloatField(default='33.0')

    administratortraining_count = models.FloatField(default='1.0')
    administratortraining_transitionhoursitem = models.FloatField(
        default='20.0')
    administratortraining_transitionhours = models.FloatField(default='20.0')
    administratortraining_transformationhoursitem = models.FloatField(
        default='17.0')
    administratortraining_transformationhours = models.FloatField(
        default='17.0')

    developserviceresponsibilitymatrix_count = models.FloatField(default='1.0')
    developserviceresponsibilitymatrix_transitionhoursitem = models.FloatField(
        default='16.0')
    developserviceresponsibilitymatrix_transitionhours = models.FloatField(
        default='16.0')
    developserviceresponsibilitymatrix_transformationhoursitem = models.FloatField(
        default='13.0')
    developserviceresponsibilitymatrix_transformationhours = models.FloatField(
        default='13.0')

    establishanyneededserviceaccounts_count = models.FloatField(default='1.0')
    establishanyneededserviceaccounts_transitionhoursitem = models.FloatField(
        default='16.0')
    establishanyneededserviceaccounts_transitionhours = models.FloatField(
        default='16.0')
    establishanyneededserviceaccounts_transformationhoursitem = models.FloatField(
        default='13.0')
    establishanyneededserviceaccounts_transformationhours = models.FloatField(
        default='13.0')

    researchandsetupemailautomation_count = models.FloatField(default='1.0')
    researchandsetupemailautomation_transitionhoursitem = models.FloatField(
        default='16.0')
    researchandsetupemailautomation_transitionhours = models.FloatField(
        default='16.0')
    researchandsetupemailautomation_transformationhoursitem = models.FloatField(
        default='13.0')
    researchandsetupemailautomation_transformationhours = models.FloatField(
        default='13.0')

    installconfigureremoteconsoles_count = models.FloatField(default='1.0')
    installconfigureremoteconsoles_transitionhoursitem = models.FloatField(
        default='16.0')
    installconfigureremoteconsoles_transitionhours = models.FloatField(
        default='16.0')
    installconfigureremoteconsoles_transformationhoursitem = models.FloatField(
        default='13.0')
    installconfigureremoteconsoles_transformationhours = models.FloatField(
        default='13.0')

    workwithsecops_count = models.FloatField(default='1.0')
    workwithsecops_transitionhoursitem = models.FloatField(default='16.0')
    workwithsecops_transitionhours = models.FloatField(default='16.0')
    workwithsecops_transformationhoursitem = models.FloatField(default='13.0')
    workwithsecops_transformationhours = models.FloatField(default='13.0')

    staffingccoordinating_count = models.FloatField(default='1.0')
    staffingccoordinating_transitionhoursitem = models.FloatField(
        default='10.0')
    staffingccoordinating_transitionhours = models.FloatField(default='10.0')
    staffingccoordinating_transformationhoursitem = models.FloatField(
        default='8.0')
    staffingccoordinating_transformationhours = models.FloatField(
        default='8.0')

    identifytestdocument_count = models.FloatField(default='1.0')
    identifytestdocument_transitionhoursitem = models.FloatField(
        default='10.0')
    identifytestdocument_transitionhours = models.FloatField(default='10.0')
    identifytestdocument_transformationhoursitem = models.FloatField(
        default='8.0')
    identifytestdocument_transformationhours = models.FloatField(default='8.0')

    obtainnetworkandosaccesswave1_count = models.FloatField(default='1.0')
    obtainnetworkandosaccesswave1_transitionhoursitem = models.FloatField(
        default='10.0')
    obtainnetworkandosaccesswave1_transitionhours = models.FloatField(
        default='10.0')
    obtainnetworkandosaccesswave1_transformationhoursitem = models.FloatField(
        default='8.0')
    obtainnetworkandosaccesswave1_transformationhours = models.FloatField(
        default='8.0')

    obtainnetworkandosaccesswave2_count = models.FloatField(default='1.0')
    obtainnetworkandosaccesswave2_transitionhoursitem = models.FloatField(
        default='10.0')
    obtainnetworkandosaccesswave2_transitionhours = models.FloatField(
        default='10.0')
    obtainnetworkandosaccesswave2_transformationhoursitem = models.FloatField(
        default='8.0')
    obtainnetworkandosaccesswave2_transformationhours = models.FloatField(
        default='8.0')

    developprovideagentsoftware_count = models.FloatField(default='1.0')
    developprovideagentsoftware_transitionhoursitem = models.FloatField(
        default='10.0')
    developprovideagentsoftware_transitionhours = models.FloatField(
        default='10.0')
    developprovideagentsoftware_transformationhoursitem = models.FloatField(
        default='8.0')
    developprovideagentsoftware_transformationhours = models.FloatField(
        default='8.0')

    installconfigureodbc_count = models.FloatField(default='1.0')
    installconfigureodbc_transitionhoursitem = models.FloatField(
        default='10.0')
    installconfigureodbc_transitionhours = models.FloatField(default='10.0')
    installconfigureodbc_transformationhoursitem = models.FloatField(
        default='8.0')
    installconfigureodbc_transformationhours = models.FloatField(default='8.0')

    customerreviewsignoff_count = models.FloatField(default='1.0')
    customerreviewsignoff_transitionhoursitem = models.FloatField(
        default='10.0')
    customerreviewsignoff_transitionhours = models.FloatField(default='10.0')
    customerreviewsignoff_transformationhoursitem = models.FloatField(
        default='8.0')
    customerreviewsignoff_transformationhours = models.FloatField(
        default='8.0')

    establishhealthcheck_count = models.FloatField(default='1.0')
    establishhealthcheck_transitionhoursitem = models.FloatField(
        default='10.0')
    establishhealthcheck_transitionhours = models.FloatField(default='10.0')
    establishhealthcheck_transformationhoursitem = models.FloatField(
        default='8.0')
    establishhealthcheck_transformationhours = models.FloatField(default='8.0')

    developworkflows_count = models.FloatField(default='1.0')
    developworkflows_transitionhoursitem = models.FloatField(default='10.0')
    developworkflows_transitionhours = models.FloatField(default='10.0')
    developworkflows_transformationhoursitem = models.FloatField(default='8.0')
    developworkflows_transformationhours = models.FloatField(default='8.0')

    operationaldocumentation_count = models.FloatField(default='1.0')
    operationaldocumentation_transitionhoursitem = models.FloatField(
        default='10.0')
    operationaldocumentation_transitionhours = models.FloatField(
        default='10.0')
    operationaldocumentation_transformationhoursitem = models.FloatField(
        default='8.0')
    operationaldocumentation_transformationhours = models.FloatField(
        default='8.0')

    shadowestablishreviewallprocedures_count = models.FloatField(default='1.0')
    shadowestablishreviewallprocedures_transitionhoursitem = models.FloatField(
        default='60.0')
    shadowestablishreviewallprocedures_transitionhours = models.FloatField(
        default='60.0')
    shadowestablishreviewallprocedures_transformationhoursitem = models.FloatField(
        default='50.0')
    shadowestablishreviewallprocedures_transformationhours = models.FloatField(
        default='50.0')

    otherdetail_count = models.FloatField(default='1.0')
    otherdetail_transitionhoursitem = models.FloatField(default='249.0')
    otherdetail_transitionhours = models.FloatField(default='249.0')
    otherdetail_transformationhoursitem = models.FloatField(default='208.0')
    otherdetail_transformationhours = models.FloatField(default='208.0')

    specialitem1_count = models.FloatField(default='.01')
    specialitem1_transitionhoursitem = models.FloatField(default='.01')
    specialitem1_transitionhours = models.FloatField(default='.0001')
    specialitem1_transformationhoursitem = models.FloatField(default='.01')
    specialitem1_transformationhours = models.FloatField(default='.0001')

    specialitem2_count = models.FloatField(default='.01')
    specialitem2_transitionhoursitem = models.FloatField(default='.01')
    specialitem2_transitionhours = models.FloatField(default='.0001')
    specialitem2_transformationhoursitem = models.FloatField(default='.01')
    specialitem2_transformationhours = models.FloatField(default='.0001')

    specialitem3_count = models.FloatField(default='.01')
    specialitem3_transitionhoursitem = models.FloatField(default='.01')
    specialitem3_transitionhours = models.FloatField(default='.0001')
    specialitem3_transformationhoursitem = models.FloatField(default='.01')
    specialitem3_transformationhours = models.FloatField(default='.0001')

    specialitem4_count = models.FloatField(default='.01')
    specialitem4_transitionhoursitem = models.FloatField(default='.01')
    specialitem4_transitionhours = models.FloatField(default='.0001')
    specialitem4_transformationhoursitem = models.FloatField(default='.01')
    specialitem4_transformationhours = models.FloatField(default='.0001')

    specialitem5_count = models.FloatField(default='.01')
    specialitem5_transitionhoursitem = models.FloatField(default='.01')
    specialitem5_transitionhours = models.FloatField(default='.0001')
    specialitem5_transformationhoursitem = models.FloatField(default='.01')
    specialitem5_transformationhours = models.FloatField(default='.0001')

    totaltransitionhoursitem = models.FloatField(default='0.0')
    totaltransformationhoursitem = models.FloatField(default='0.0')
    numtransitionweeks = models.FloatField(default='12.0')
    numtransformationweeks = models.FloatField(default='12.0')

    SpecialItemsDesc1 = models.CharField(blank=True, max_length=150)
    SpecialItemsDesc2 = models.CharField(blank=True, max_length=150)
    SpecialItemsDesc3 = models.CharField(blank=True, max_length=150)
    SpecialItemsDesc4 = models.CharField(blank=True, max_length=150)
    SpecialItemsDesc5 = models.CharField(blank=True, max_length=150)

    # Account Details
    rfs_num = models.CharField(blank=True, max_length=150)
    sales_connect_num = models.CharField(blank=True, max_length=150)
    appttus_num = models.CharField(blank=True, max_length=150)
    sizingtype = models.CharField(blank=True, max_length=150)
    due_date = models.DateTimeField(default=timezone.now)

    # Owner/Team Info
    prepardedby = models.CharField(blank=True, max_length=150)
    team = models.CharField(blank=True, max_length=150)
    assigned_by = models.CharField(blank=True, max_length=150)
    assigned_to = models.CharField(blank=True, max_length=150)

    # GBO Info
    sent_gbo_date = models.DateTimeField(default=timezone.now)
    response_gbo_date = models.DateTimeField(default=timezone.now)
    approved_gbo_date = models.DateTimeField(default=timezone.now)
    gbo_reviewer = models.CharField(blank=True, max_length=150)

    transition_weeks = models.FloatField(default='12')
    transformation_weeks = models.FloatField(default='12')

    #
    # # OTC- One Time Cost: Hours
    # transition_hours = models.FloatField(default='0.0')
    # transformation_hours = models.FloatField(default='0.0')
    # sum_transition_hours = models.FloatField(default='0.0')
    # sum_transformation_hours = models.FloatField(default='0.0')
    # first_line_mgr_hrs = models.FloatField(default='0.0')
    # second_line_mgr_hrs = models.FloatField(default='0.0')

    # # Steady State Hours / FTE
    # combined_Svcs = models.FloatField(default='0.0')
    # components = models.FloatField(default='0.0')
    # custom_Optns = models.FloatField(default='0.0')
    # addl_Services = models.FloatField(default='0.0')
    # first_line_mgr_steadystate_hrs = models.FloatField(default='0.0')
    # second_line_mgr_steadystate_hrs = models.FloatField(default='0.0')
    # total_steadystate_hours = models.FloatField(default='0.0')
    #
    # # FTE
    # transition_fte = models.FloatField(default='0.0')
    # transformation_fte = models.FloatField(default='0.0')
    # total_fte  = models.FloatField(default='0.0')

    class Meta:
        ordering = ['-date']

    def calculate_totaltransitionhoursitem(self):
        return self.executetransitionplan_transitionhoursitem + self.createbestpracticecustom_transitionhoursitem + self.testinfrastructurepoc_transitionhoursitem + self.troubleshoottune_transitionhoursitem + self.installconfigure_transitionhoursitem + self.administratortraining_transitionhoursitem + self.developserviceresponsibilitymatrix_transitionhoursitem + self.establishanyneededserviceaccounts_transitionhoursitem + self.researchandsetupemailautomation_transitionhoursitem + self.installconfigureremoteconsoles_transitionhoursitem + self.workwithsecops_transitionhoursitem + self.staffingccoordinating_transitionhoursitem + self.identifytestdocument_transitionhoursitem + self.obtainnetworkandosaccesswave1_transitionhoursitem + self.obtainnetworkandosaccesswave2_transitionhoursitem + self.developprovideagentsoftware_transitionhoursitem + self.installconfigureodbc_transitionhoursitem + self.customerreviewsignoff_transitionhoursitem + self.establishhealthcheck_transitionhoursitem + self.developworkflows_transitionhoursitem + self.operationaldocumentation_transitionhoursitem + self.shadowestablishreviewallprocedures_transitionhoursitem + self.otherdetail_transitionhoursitem + self.specialitem1_transitionhoursitem + self.specialitem2_transitionhoursitem + self.specialitem3_transitionhoursitem + self.specialitem4_transitionhoursitem + self.specialitem5_transitionhoursitem,



    def calculate_totaltransformationhoursitem(self):
        return (self.executetransitionplan_transformationhoursitem + self.createbestpracticecustom_transformationhoursitem + self.testinfrastructurepoc_transformationhoursitem + self.troubleshoottune_transformationhoursitem + self.installconfigure_transformationhoursitem + self.administratortraining_transformationhoursitem + self.developserviceresponsibilitymatrix_transformationhoursitem + self.establishanyneededserviceaccounts_transformationhoursitem + self.researchandsetupemailautomation_transformationhoursitem + self.installconfigureremoteconsoles_transformationhoursitem + self.workwithsecops_transformationhoursitem + self.staffingccoordinating_transformationhoursitem + self.identifytestdocument_transformationhoursitem + \
               self.obtainnetworkandosaccesswave1_transformationhoursitem + self.obtainnetworkandosaccesswave2_transformationhoursitem + self.developprovideagentsoftware_transformationhoursitem + self.installconfigureodbc_transformationhoursitem + self.customerreviewsignoff_transformationhoursitem + self.establishhealthcheck_transformationhoursitem + self.developworkflows_transformationhoursitem + \
               self.operationaldocumentation_transformationhoursitem + self.shadowestablishreviewallprocedures_transformationhoursitem + self.otherdetail_transformationhoursitem + self.specialitem1_transformationhoursitem + \
               self.specialitem2_transformationhoursitem + self.specialitem3_transformationhoursitem + \
               self.specialitem4_transformationhoursitem + \
               self.specialitem5_transformationhoursitem,)

    def save(self, *args, **kwargs):
        totaltransitionhoursitem_BZ = 525
        # calculate_totaltransitionhoursitem = self.executetransitionplan_transitionhoursitem + self.createbestpracticecustom_transitionhoursitem + self.testinfrastructurepoc_transitionhoursitem + self.troubleshoottune_transitionhoursitem + self.installconfigure_transitionhoursitem + self.administratortraining_transitionhoursitem + self.developserviceresponsibilitymatrix_transitionhoursitem + self.establishanyneededserviceaccounts_transitionhoursitem + self.researchandsetupemailautomation_transitionhoursitem + self.installconfigureremoteconsoles_transitionhoursitem + self.workwithsecops_transitionhoursitem + self.staffingccoordinating_transitionhoursitem + self.identifytestdocument_transitionhoursitem + \
        #     self.obtainnetworkandosaccesswave1_transitionhoursitem + self.obtainnetworkandosaccesswave2_transitionhoursitem + self.developprovideagentsoftware_transitionhoursitem + self.installconfigureodbc_transitionhoursitem + self.customerreviewsignoff_transitionhoursitem + self.establishhealthcheck_transitionhoursitem + self.developworkflows_transitionhoursitem + self.operationaldocumentation_transitionhoursitem + self.shadowestablishreviewallprocedures_transitionhoursitem + self.otherdetail_transitionhoursitem + self.specialitem1_transitionhoursitem + self.specialitem2_transitionhoursitem + self.specialitem3_transitionhoursitem + self.specialitem4_transitionhoursitem + self.specialitem5_transitionhoursitem,
        # calculate_totaltransformationhoursitem = self.executetransitionplan_transformationhoursitem + self.createbestpracticecustom_transformationhoursitem + self.testinfrastructurepoc_transformationhoursitem + self.troubleshoottune_transformationhoursitem + self.installconfigure_transformationhoursitem + self.administratortraining_transformationhoursitem + self.developserviceresponsibilitymatrix_transformationhoursitem + self.establishanyneededserviceaccounts_transformationhoursitem + self.researchandsetupemailautomation_transformationhoursitem + self.installconfigureremoteconsoles_transformationhoursitem + self.workwithsecops_transformationhoursitem + self.staffingccoordinating_transformationhoursitem + self.identifytestdocument_transformationhoursitem + \
        # self.obtainnetworkandosaccesswave1_transformationhoursitem +
        # self.obtainnetworkandosaccesswave2_transformationhoursitem +
        # self.developprovideagentsoftware_transformationhoursitem +
        # self.installconfigureodbc_transformationhoursitem +
        # self.customerreviewsignoff_transformationhoursitem +
        # self.establishhealthcheck_transformationhoursitem +
        # self.developworkflows_transformationhoursitem +
        # self.operationaldocumentation_transformationhoursitem +
        # self.shadowestablishreviewallprocedures_transformationhoursitem +
        # self.otherdetail_transformationhoursitem +
        # self.specialitem1_transformationhoursitem +
        # self.specialitem2_transformationhoursitem +
        # self.specialitem3_transformationhoursitem +
        # self.specialitem4_transformationhoursitem +
        # self.specialitem5_transformationhoursitem,

        order_items = self.order_items.all()
        # orders = self.order.all()
        self.value = order_items.aggregate(Sum('total_price'))[
            'total_price__sum'] if order_items.exists() else 0.00
        self.final_value = Decimal(self.value) - Decimal(self.discount)

        self.sum_numserver = order_items.aggregate(
            Sum('numserver'))['numserver__sum'] if order_items.exists() else 0.00
        # self.sum_numconsole =
        # order_items.aggregate(Sum('numconsole'))['numconsole__sum'] if
        # order_items.exists() else 0.00
        self.sum_workstation = order_items.aggregate(Sum('numworkstation'))[
            'numworkstation__sum'] if order_items.exists() else 0
        self.sum_ipaddress = order_items.aggregate(Sum('numipaddress'))[
            'numipaddress__sum'] if order_items.exists() else 0
        self.sum_endpoint = order_items.aggregate(Sum('total_endpoints'))[
            'total_endpoints__sum'] if order_items.exists() else 0
        self.sum_numconsole = order_items.aggregate(
            Sum('qty'))['qty__sum'] if order_items.exists() else 0

        self.sum_wkstnshourscalc = order_items.aggregate(Sum('wkstnshourscalc'))[
            'wkstnshourscalc__sum'] if order_items.exists() else 0
        self.sum_srvshourscalc = order_items.aggregate(Sum('srvshourscalc'))[
            'srvshourscalc__sum'] if order_items.exists() else 0
        self.sum_ipshourscalc = order_items.aggregate(Sum('ipshourscalc'))[
            'ipshourscalc__sum'] if order_items.exists() else 0
        self.sum_ipshourscalc = order_items.aggregate(Sum('ipshourscalc'))[
            'ipshourscalc__sum'] if order_items.exists() else 0
        self.sum_consolehourscalc = order_items.aggregate(Sum('addlconhourscalc'))[
            'addlconhourscalc__sum'] if order_items.exists() else 0

        # self.sum_hours = order_items.aggregate(Sum('hours'))['hours__sum'] if order_items.exists() else 0.00
        # self.sum_fte = order_items.aggregate(Sum('fte'))['fte__sum'] if
        # order_items.exists() else 0.00

        self.sum_consolehourscalc = order_items.aggregate(Sum('addlconhourscalc'))[
            'addlconhourscalc__sum'] if order_items.exists() else 0

        tnt_transition_values = [self.executetransitionplan_transitionhoursitem, self.createbestpracticecustom_transitionhoursitem, self.testinfrastructurepoc_transitionhoursitem]

        tnt_transition_total = sum([1 + 2.59, 3 + 7])
        # tnt_transition_total2 = sum(tnt_transition_values)

        # self.totaltransitionhoursitem = tnt_transition_total
        self.totaltransitionhoursitem = tnt_transition_total
        self.totaltransformationhoursitemt = tnt_transition_values



        #

        # Total_TNT = Order.aggregate(
        #     Sum('executetransitionplan_transitionhoursitem' + 'createbestpracticecustom_transitionhoursitem'))['executetransitionplan_transitionhoursitem_sum'] if order_items.exists() else 0

        # self.totaltransitionhoursitem = self.calculate_totaltransitionhoursitem()
        # self.totaltransitionhoursitem = self.Total_TNT()


        # self.totaltransformationtotalhours = (self.numtransitionweeks *
        # self.labordelivery.workweek)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title if self.title else 'New Order'

    def get_edit_url(self):
        return reverse('update_order', kwargs={'pk': self.id})

    def get_delete_url(self):
        return reverse('delete_order', kwargs={'pk': self.id})

    def tag_final_value(self):
        return f'{self.final_value} {CURRENCY}'

    def tag_discount(self):
        return f'{self.discount} {CURRENCY}'

    def tag_value(self):
        return f'{self.value} {CURRENCY}'

    def tag_num_server(self):
        return f'{self.sum_numserver} '

    def tag_sum_srvshourscalc(self):
        return f'{self.sum_srvshourscalc} '

    def tag_num_workstation(self):
        return f'{self.sum_workstation} '

    def tag_sum_wkstnshourscalc(self):
        return f'{self.sum_wkstnshourscalc}'

    def tag_num_ipaddress(self):
        return f'{self.sum_ipaddress} '

    def tag_sum_ipshourscalc(self):
        return f'{self.sum_ipshourscalc} '

    def tag_num_console(self):
        return f'{self.sum_numconsole} '

    def tag_sum_consolehourscalc(self):
        return f'{self.sum_consolehourscalc} '

    def tag_sum_endpoint(self):
        return f'{self.sum_endpoint} '

    @staticmethod
    def filter_data(request, queryset):
        search_name = request.GET.get('search_name', None)
        date_start = request.GET.get('date_start', None)
        date_end = request.GET.get('date_end', None)
        queryset = queryset.filter(
            title__contains=search_name) if search_name else queryset
        if date_end and date_start and date_end >= date_start:
            date_start = datetime.datetime.strptime(
                date_start, '%m/%d/%Y').strftime('%Y-%m-%d')
            date_end = datetime.datetime.strptime(
                date_end, '%m/%d/%Y').strftime('%Y-%m-%d')
            print(date_start, date_end)
            queryset = queryset.filter(date__range=[date_start, date_end])
        return queryset


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='order_items')
    labordelivery = models.ForeignKey(
        Labordelivery, on_delete=models.PROTECT, default=5, )
    qty = models.PositiveIntegerField(default=1)
    price = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    final_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    total_price = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    base = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_base = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    final_base = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    total_base = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    fte = models.DecimalField(default=0.00, decimal_places=2, max_digits=20)
    discount_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    final_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    total_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    productcomplexityfac = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    numworkstation = models.IntegerField(default='0')
    numserver = models.IntegerField(db_column='Numserver', default='0')
    numipaddress = models.IntegerField(default='0')
    total_endpoints = models.IntegerField(default='0')
    desc = models.CharField(blank=True, max_length=150)

    numappchange = models.IntegerField(default='0')

    srvshourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=8)
    wkstnshourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    ipshourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    addlconhourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    appchangehourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    totalhourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    appchangefac = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    serverfte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    workstationfte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    ipendpointfte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    addlconfte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Labordelivery Options Fields
    # labordeliverytype = models.CharField(blank=True, max_length=150)
    deliveryoption = models.CharField(blank=True, max_length=150)
    regions = models.CharField(blank=True, max_length=150)
    currencytype = models.CharField(blank=True, max_length=150)
    defaultfte_year = models.CharField(blank=True, max_length=150)
    workweek = models.CharField(blank=True, max_length=150)
    deliveryctrcostfactor = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # LaborDelivery Band Info:
    band2count = models.FloatField(default='0.0')
    band2percentage = models.FloatField(default='0.0')

    band3count = models.FloatField(default='0.0')
    band3percentage = models.FloatField(default='0.0')

    band4count = models.FloatField(default='0.0')
    band4percentage = models.FloatField(default='0.0')

    band5count = models.FloatField(default='0.0')
    band5percentage = models.FloatField(default='0.0')

    band6count = models.FloatField(default='0.0')
    band6percentage = models.FloatField(default='0.0')

    band7count = models.FloatField(default='0.0')
    band7percentage = models.FloatField(default='0.0')

    band8count = models.FloatField(default='0.0')
    band8percentage = models.FloatField(default='0.0')

    band9count = models.FloatField(default='0.0')
    band9percentage = models.FloatField(default='0.0')

    band10count = models.FloatField(default='0.0')
    band10percentage = models.FloatField(default='0.0')

    bandstotalcount = models.FloatField(default='0.0')
    bandstotalpercentage = models.FloatField(default='0.0')

    # Contract number of Months
    nummonths = models.IntegerField(default='12')

    # Component #1
    prodcomponent1_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent1_wkstn = models.BooleanField(default=False)
    prodcomponent1_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent1_svr = models.BooleanField(default=False)
    prodcomponent1_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent1_IP = models.BooleanField(default=False)
    prodcomponent1_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent1_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent1_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #2
    prodcomponent2_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent2_wkstn = models.BooleanField(default=False)
    prodcomponent2_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent2_svr = models.BooleanField(default=False)
    prodcomponent2_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent2_IP = models.BooleanField(default=False)
    prodcomponent2_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent2_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent2_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #3
    prodcomponent3_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent3_wkstn = models.BooleanField(default=False)
    prodcomponent3_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent3_svr = models.BooleanField(default=False)
    prodcomponent3_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent3_IP = models.BooleanField(default=False)
    prodcomponent3_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent3_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent3_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #4
    prodcomponent4_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent4_wkstn = models.BooleanField(default=False)
    prodcomponent4_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent4_svr = models.BooleanField(default=False)
    prodcomponent4_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent4_IP = models.BooleanField(default=False)
    prodcomponent4_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent4_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent4_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #5
    prodcomponent5_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent5_wkstn = models.BooleanField(default=False)
    prodcomponent5_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent5_svr = models.BooleanField(default=False)
    prodcomponent5_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent5_IP = models.BooleanField(default=False)
    prodcomponent5_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent5_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent5_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #6
    prodcomponent6_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent6_wkstn = models.BooleanField(default=False)
    prodcomponent6_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent6_svr = models.BooleanField(default=False)
    prodcomponent6_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent6_IP = models.BooleanField(default=False)
    prodcomponent6_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent6_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent6_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #7
    prodcomponent7_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent7_wkstn = models.BooleanField(default=False)
    prodcomponent7_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent7_svr = models.BooleanField(default=False)
    prodcomponent7_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent7_IP = models.BooleanField(default=False)
    prodcomponent7_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent7_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent7_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #8
    prodcomponent8_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent8_wkstn = models.BooleanField(default=False)
    prodcomponent8_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent8_svr = models.BooleanField(default=False)
    prodcomponent8_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent8_IP = models.BooleanField(default=False)
    prodcomponent8_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent8_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent8_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #9
    prodcomponent9_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent9_wkstn = models.BooleanField(default=False)
    prodcomponent9_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent9_svr = models.BooleanField(default=False)
    prodcomponent9_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent9_IP = models.BooleanField(default=False)
    prodcomponent9_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent9_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent9_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #10
    prodcomponent10_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent10_wkstn = models.BooleanField(default=False)
    prodcomponent10_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent10_svr = models.BooleanField(default=False)
    prodcomponent10_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent10_IP = models.BooleanField(default=False)
    prodcomponent10_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent10_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent10_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #11
    prodcomponent11_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent11_wkstn = models.BooleanField(default=False)
    prodcomponent11_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent11_svr = models.BooleanField(default=False)
    prodcomponent11_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent11_IP = models.BooleanField(default=False)
    prodcomponent11_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent11_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent11_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #12
    prodcomponent12_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent12_wkstn = models.BooleanField(default=False)
    prodcomponent12_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent12_svr = models.BooleanField(default=False)
    prodcomponent12_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent12_IP = models.BooleanField(default=False)
    prodcomponent12_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent12_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent12_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #13
    prodcomponent13_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent13_wkstn = models.BooleanField(default=False)
    prodcomponent13_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent13_svr = models.BooleanField(default=False)
    prodcomponent13_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent13_IP = models.BooleanField(default=False)
    prodcomponent13_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent13_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent13_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #14
    prodcomponent14_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent14_wkstn = models.BooleanField(default=False)
    prodcomponent14_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent14_svr = models.BooleanField(default=False)
    prodcomponent14_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent14_IP = models.BooleanField(default=False)
    prodcomponent14_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent14_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent14_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    # Component #15
    prodcomponent15_desc = models.CharField(
        blank=True, null=True, max_length=150)
    prodcomponent15_wkstn = models.BooleanField(default=False)
    prodcomponent15_wkstnhours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent15_svr = models.BooleanField(default=False)
    prodcomponent15_svrHours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent15_IP = models.BooleanField(default=False)
    prodcomponent15_iphours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent15_ttl_hours = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodcomponent15_ttl_fte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)

    softlifesvryesno = models.BooleanField(default=False)
    softlifesrvhourscalc = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    softlifesvrfte = models.DecimalField(
        default=0.00, decimal_places=2, max_digits=20)
    prodimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.product.title}'

    def save(self, *args, **kwargs):
        self.final_price = self.discount_price if self.discount_price > 0 else self.price
        self.total_price = Decimal(self.qty) * Decimal(self.final_price)
        # self.addlconhourscalc = Decimal(self.qty) * Decimal(self.base)

        # self.labordeliverytype = self.labordelivery.labordeliverytype
        self.deliveryoption = self.labordelivery.deliveryoption
        self.regions = self.labordelivery.regions
        self.currencytype = self.labordelivery.currencytype
        self.defaultfte_year = Decimal(self.labordelivery.defaultfte_year)
        self.workweek = self.labordelivery.workweek
        self.deliveryctrcostfactor = self.labordelivery.deliveryctrcostfactor
        self.base = self.product.productcomplexitybase

        self.prodcomponent1_desc = self.product.component1desc
        self.prodcomponent2_desc = self.product.component2desc
        self.prodcomponent3_desc = self.product.component3desc
        self.prodcomponent4_desc = self.product.component4desc
        self.prodcomponent5_desc = self.product.component5desc
        self.prodcomponent6_desc = self.product.component6desc
        self.prodcomponent7_desc = self.product.component7desc
        self.prodcomponent8_desc = self.product.component8desc
        self.prodcomponent9_desc = self.product.component9desc
        self.prodcomponent10_desc = self.product.component10desc
        self.prodcomponent11_desc = self.product.component11desc
        self.prodcomponent12_desc = self.product.component12desc
        self.prodcomponent13_desc = self.product.component13desc
        self.prodcomponent14_desc = self.product.component14desc
        self.prodcomponent15_desc = self.product.component15desc

        # Hours Calculation for Component#1 HoursLine

        # if self.prodcomponent1_wkstn == True:
        #     self.prodcomponent1_wkstnhours = (self.wkstnshourscalc * int(self.product.componentcomplexityfac1))
        # else:
        #     self.prodcomponent1_wkstnhours = 0
        #
        # if self.prodcomponent1_svr == True:
        #     self.prodcomponent15_svrHours = (self.srvshourscalc * int(self.product.componentcomplexityfac1))
        # else:
        #     self.prodcomponent15_svrHours = 0

        # Component Hours and Factor Calculations
        #
        # self.prodcomponent1 = self.product.component1
        # # self.prodcomponent1_desc = self.product.component1desc
        #
        # if self.product.component1desc is None:
        #     self.prodcomponent1_desc = ''
        # else:
        #     self.prodcomponent1_desc = self.product.component1desc
        #
        # self.componentcomplexityfac1 = self.product.componentcomplexityfac1
        # self.prodcomponent1_svrHours = self.product.ComponentHours1
        #
        # self.prodcomponent2 = self.product.component1
        # # self.prodcomponent2_desc = self.product.component2desc
        #
        # if self.product.component2desc is None:
        #     self.prodcomponent2_desc = ''
        # else:
        #     self.prodcomponent2_desc = self.product.component2desc
        #
        # self.componentcomplexityfac2 = self.product.componentcomplexityfac2
        # self.prodcomponent2_svrHours = self.product.ComponentHours2
        #
        # self.prodcomponent3 = self.product.component1
        # # self.prodcomponent3_desc = self.product.component3desc
        #
        # if self.product.component3desc is None:
        #     self.prodcomponent3_desc = ''
        # else:
        #     self.prodcomponent3_desc = self.product.component3desc
        #
        # self.componentcomplexityfac3 = self.product.componentcomplexityfac3
        # self.prodcomponent3_svrHours = self.product.ComponentHours3
        #
        # self.prodcomponent4 = self.product.component4
        # # self.prodcomponent4_desc = self.product.component4desc
        #
        # if self.product.component4desc is None:
        #     self.prodcomponent4_desc = ''
        # else:
        #     self.prodcomponent4_desc = self.product.component4desc
        #
        # self.componentcomplexityfac4 = self.product.componentcomplexityfac4
        # self.prodcomponent4_svrHours = self.product.ComponentHours4
        #
        # self.prodcomponent5 = self.product.component5
        # # self.prodcomponent5_desc = self.product.component5desc
        #
        # if self.product.component5desc is None:
        #     self.prodcomponent5_desc = ''
        # else:
        #     self.prodcomponent5_desc = self.product.component5desc
        #
        # self.componentcomplexityfac5 = self.product.componentcomplexityfac5
        # self.prodcomponent5_svrHours = self.product.ComponentHours5
        #
        # self.prodcomponent6 = self.product.component6
        # # self.prodcomponent6_desc = self.product.component6desc
        #
        # if self.product.component6desc is None:
        #     self.prodcomponent6_desc = ''
        # else:
        #     self.prodcomponent6_desc = self.product.component6desc
        #
        # self.componentcomplexityfac6 = self.product.componentcomplexityfac6
        # self.prodcomponent6_svrHours = self.product.ComponentHours6
        #
        # self.prodcomponent7 = self.product.component7
        # # self.prodcomponent7_desc = self.product.component7desc
        #
        # if self.product.component7desc is None:
        #     self.prodcomponent7_desc = ''
        # else:
        #     self.prodcomponent7_desc = self.product.component7desc
        #
        # self.componentcomplexityfac7 = self.product.componentcomplexityfac7
        # self.prodcomponent7_svrHours = self.product.ComponentHours7
        #
        # self.prodcomponent8 = self.product.component8
        # # self.prodcomponent8_desc = self.product.component8desc
        #
        # if self.product.component8desc is None:
        #     self.prodcomponent8_desc = ''
        # else:
        #     self.prodcomponent8_desc = self.product.component8desc
        #
        # self.componentcomplexityfac8 = self.product.componentcomplexityfac8
        # self.prodcomponent8_svrHours = self.product.ComponentHours8
        #
        # self.prodcomponent9 = self.product.component9
        # # self.prodcomponent9_desc = self.product.component9desc
        #
        # if self.product.component9desc is None:
        #     self.prodcomponent9_desc = ''
        # else:
        #     self.prodcomponent9_desc = self.product.component9desc
        #
        # self.componentcomplexityfac9 = self.product.componentcomplexityfac9
        # self.prodcomponent9_svrHours = self.product.ComponentHours9
        #
        # self.prodcomponent10 = self.product.component10
        # # self.prodcomponent10_desc = self.product.component3desc
        #
        # if self.product.component10desc is None:
        #     self.prodcomponent10_desc = ''
        # else:
        #     self.prodcomponent10_desc = self.product.component10desc
        #
        # self.componentcomplexityfac10 = self.product.componentcomplexityfac10
        # self.prodcomponent10_svrHours = self.product.ComponentHours10
        #
        # self.prodcomponent11 = self.product.component11
        # # self.prodcomponent11_desc = self.product.component11desc
        #
        # if self.product.component11desc is None:
        #     self.prodcomponent11_desc = ''
        # else:
        #     self.prodcomponent11_desc = self.product.component11desc
        #
        # self.componentcomplexityfac11 = self.product.componentcomplexityfac11
        # self.prodcomponent11_svrHours = self.product.ComponentHours11
        #
        # self.prodcomponent12 = self.product.component12
        # # self.prodcomponent12_desc = self.product.component12desc
        #
        # if self.product.component12desc is None:
        #     self.prodcomponent12_desc = ''
        # else:
        #     self.prodcomponent12_desc = self.product.component12desc
        #
        # self.componentcomplexityfac12 = self.product.componentcomplexityfac12
        # self.prodcomponent12_svrHours = self.product.ComponentHours12
        #
        # self.prodcomponent13 = self.product.component13
        # # self.prodcomponent13_desc = self.product.component13desc
        #
        # if self.product.component13desc is None:
        #     self.prodcomponent13_desc = ''
        # else:
        #     self.prodcomponent13_desc = self.product.component13desc
        #
        # self.componentcomplexityfac13 = self.product.componentcomplexityfac13
        # self.prodcomponent13_svrHours = self.product.ComponentHours13
        #
        # self.prodcomponent14 = self.product.component14
        # # self.prodcomponent14_desc = self.product.component14desc
        #
        # if self.product.component14desc is None:
        #     self.prodcomponent14_desc = ''
        # else:
        #     self.prodcomponent14_desc = self.product.component14desc
        #
        # self.componentcomplexityfac14 = self.product.componentcomplexityfac14
        # self.prodcomponent14_svrHours = self.product.ComponentHours14
        #
        # self.prodcomponent15 = self.product.component15
        # # self.prodcomponent15_desc = self.product.component15desc
        #
        # if self.product.component15desc is None:
        #     self.prodcomponent15_desc = ''
        # else:
        #     self.prodcomponent15_desc = self.product.component15desc
        #
        # self.componentcomplexityfac15 = self.product.componentcomplexityfac15
        # self.prodcomponent15_svrHours = self.product.ComponentHours15

        # Server Hours Calculations

        enterednumserver = self.numserver
        # Hours Calculation for Server Line Item

        if enterednumserver >= 200500:
            self.srvshourscalc = (
                                         ((0.0285 * self.productcomplexityfac) * self.numserver) * (
                                         self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumserver > 200000:
            self.srvshourscalc = (
                                         ((0.0275 * self.productcomplexityfac) * self.numserver) * (
                                         self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumserver >= 150000:
            self.srvshourscalc = (
                                         ((0.055 * self.productcomplexityfac) * self.numserver) * (
                                         self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumserver >= 100000:
            self.srvshourscalc = (self.numserver * .14 / 12) * self.nummonths
        elif enterednumserver >= 100000:
            self.srvshourscalc = (self.numserver * .14 / 12) * self.nummonths
        elif enterednumserver >= 85000:
            self.srvshourscalc = (self.numserver * .1425 / 12) * self.nummonths
        elif enterednumserver >= 75000:
            self.srvshourscalc = (self.numserver * .145 / 12) * self.nummonths
        elif enterednumserver >= 50000:
            self.srvshourscalc = (self.numserver * .135 / 12) * self.nummonths
        elif enterednumserver >= 42000:
            self.srvshourscalc = (self.numserver * .16 / 12) * self.nummonths
        elif enterednumserver >= 37000:
            self.srvshourscalc = (self.numserver * .163 / 12) * self.nummonths
        elif enterednumserver >= 35000:
            self.srvshourscalc = (self.numserver * .165 / 12) * self.nummonths
        elif enterednumserver >= 25000:
            self.srvshourscalc = (self.numserver * .17 / 12) * self.nummonths
        elif enterednumserver >= 15000:
            self.srvshourscalc = (self.numserver * .18 / 12) * self.nummonths
        elif enterednumserver >= 10000:
            self.srvshourscalc = (self.numserver * .19 / 12) * self.nummonths
        elif enterednumserver >= 5000:
            self.srvshourscalc = (self.numserver * .195 / 12) * self.nummonths
        elif enterednumserver >= 3000:
            self.srvshourscalc = (self.numserver * .2 / 12) * self.nummonths
        elif enterednumserver >= 2601:
            self.srvshourscalc = (self.numserver * .21 / 12) * self.nummonths
        elif enterednumserver >= 2600:
            self.srvshourscalc = (self.numserver * .22 / 12) * self.nummonths
        elif enterednumserver >= 2000:
            self.srvshourscalc = (self.numserver * .23 / 12) * self.nummonths
        elif enterednumserver >= 1500:
            self.srvshourscalc = (self.numserver * .24 / 12) * self.nummonths
        elif enterednumserver >= 1000:
            self.srvshourscalc = (self.numserver * .25 / 12) * self.nummonths
        elif enterednumserver >= 750:
            self.srvshourscalc = (self.numserver * .26 / 12) * self.nummonths
        elif enterednumserver >= 500:
            self.srvshourscalc = (self.numserver * .27 / 12) * self.nummonths
        elif enterednumserver >= 250:
            self.srvshourscalc = (self.numserver * .28 / 12) * self.nummonths
        elif enterednumserver >= 200:
            self.srvshourscalc = (self.numserver * .29 / 12) * self.nummonths
        elif enterednumserver >= 100:
            self.srvshourscalc = (self.numserver * .30 / 12) * self.nummonths
        elif enterednumserver >= 50:
            self.srvshourscalc = (self.numserver * .31 / 12) * self.nummonths
        elif enterednumserver <= 50:
            self.srvshourscalc = (self.numserver * .31 / 12) * self.nummonths
        # else:
        #     self.srvshourscalc = self.base

        # Workstation Hours Calculation

        enterednumworkstation = int(self.numworkstation)
        # Hours Calculation for Workstation Line Item

        if enterednumworkstation >= 200500:
            self.wkstnshourscalc = int(
                ((0.0285 * self.productcomplexityfac) * self.numworkstation) * (
                        self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumworkstation > 200000:
            self.wkstnshourscalc = (
                                           ((0.0275 * self.productcomplexityfac) * self.numworkstation) * (
                                           self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumworkstation >= 150000:
            self.wkstnshourscalc = (
                                           ((0.055 * self.productcomplexityfac) * self.numworkstation) * (
                                           self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumworkstation >= 100000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .14 / 12) * self.nummonths
        elif enterednumworkstation >= 100000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .14 / 12) * self.nummonths
        elif enterednumworkstation >= 85000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .1425 / 12) * self.nummonths
        elif enterednumworkstation >= 75000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .145 / 12) * self.nummonths
        elif enterednumworkstation >= 50000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .135 / 12) * self.nummonths
        elif enterednumworkstation >= 42000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .16 / 12) * self.nummonths
        elif enterednumworkstation >= 37000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .163 / 12) * self.nummonths
        elif enterednumworkstation >= 35000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .165 / 12) * self.nummonths
        elif enterednumworkstation >= 25000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .17 / 12) * self.nummonths
        elif enterednumworkstation >= 15000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .18 / 12) * self.nummonths
        elif enterednumworkstation >= 10000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .19 / 12) * self.nummonths
        elif enterednumworkstation >= 5000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .195 / 12) * self.nummonths
        elif enterednumworkstation >= 3000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .2 / 12) * self.nummonths
        elif enterednumworkstation >= 2601:
            self.wkstnshourscalc = (
                                           self.numworkstation * .21 / 12) * self.nummonths
        elif enterednumworkstation >= 2600:
            self.wkstnshourscalc = (
                                           self.numworkstation * .22 / 12) * self.nummonths
        elif enterednumworkstation >= 2000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .23 / 12) * self.nummonths
        elif enterednumworkstation >= 1500:
            self.wkstnshourscalc = (
                                           self.numworkstation * .24 / 12) * self.nummonths
        elif enterednumworkstation >= 1000:
            self.wkstnshourscalc = (
                                           self.numworkstation * .25 / 12) * self.nummonths
        elif enterednumworkstation >= 750:
            self.wkstnshourscalc = (
                                           self.numworkstation * .26 / 12) * self.nummonths
        elif enterednumworkstation >= 500:
            self.wkstnshourscalc = (
                                           self.numworkstation * .27 / 12) * self.nummonths
        elif enterednumworkstation >= 250:
            self.wkstnshourscalc = (
                                           self.numworkstation * .28 / 12) * self.nummonths
        elif enterednumworkstation >= 200:
            self.wkstnshourscalc = (
                                           self.numworkstation * .29 / 12) * self.nummonths
        elif enterednumworkstation >= 100:
            self.wkstnshourscalc = (
                                           self.numworkstation * .30 / 12) * self.nummonths
        elif enterednumworkstation >= 50:
            self.wkstnshourscalc = (
                                           self.numworkstation * .31 / 12) * self.nummonths
        # else:
        #     self.wkstnshourscalc = self.base

        # Ip Address Hours Calculation

        enterednumipaddress = int(self.numipaddress)
        # Hours Calculation for Server Line Item

        if enterednumipaddress >= 200500:
            self.ipshourscalc = int(
                ((0.0285 * self.productcomplexityfac) * self.numipaddress) * (
                        self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumipaddress > 200000:
            self.ipshourscalc = (
                                        ((0.0275 * self.productcomplexityfac) * self.numipaddress) * (
                                        self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumipaddress >= 150000:
            self.ipshourscalc = (
                                        ((0.055 * self.productcomplexityfac) * self.numipaddress) * (
                                        self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumipaddress >= 100000:
            self.ipshourscalc = (self.numipaddress * .14 / 12) * self.nummonths
        elif enterednumipaddress >= 100000:
            self.ipshourscalc = (self.numipaddress * .14 / 12) * self.nummonths
        elif enterednumipaddress >= 85000:
            self.ipshourscalc = (
                                        self.numipaddress * .1425 / 12) * self.nummonths
        elif enterednumipaddress >= 75000:
            self.ipshourscalc = (
                                        self.numipaddress * .145 / 12) * self.nummonths
        elif enterednumipaddress >= 50000:
            self.ipshourscalc = (
                                        self.numipaddress * .135 / 12) * self.nummonths
        elif enterednumipaddress >= 42000:
            self.ipshourscalc = (self.numipaddress * .16 / 12) * self.nummonths
        elif enterednumipaddress >= 37000:
            self.ipshourscalc = (
                                        self.numipaddress * .163 / 12) * self.nummonths
        elif enterednumipaddress >= 35000:
            self.ipshourscalc = (
                                        self.numipaddress * .165 / 12) * self.nummonths
        elif enterednumipaddress >= 25000:
            self.ipshourscalc = (self.numipaddress * .17 / 12) * self.nummonths
        elif enterednumipaddress >= 15000:
            self.ipshourscalc = (self.numipaddress * .18 / 12) * self.nummonths
        elif enterednumipaddress >= 10000:
            self.ipshourscalc = (self.numipaddress * .19 / 12) * self.nummonths
        elif enterednumipaddress >= 5000:
            self.ipshourscalc = (
                                        self.numipaddress * .195 / 12) * self.nummonths
        elif enterednumipaddress >= 3000:
            self.ipshourscalc = (self.numipaddress * .2 / 12) * self.nummonths
        elif enterednumipaddress >= 2601:
            self.ipshourscalc = (self.numipaddress * .21 / 12) * self.nummonths
        elif enterednumipaddress >= 2600:
            self.ipshourscalc = (self.numipaddress * .22 / 12) * self.nummonths
        elif enterednumipaddress >= 2000:
            self.ipshourscalc = (self.numipaddress * .23 / 12) * self.nummonths
        elif enterednumipaddress >= 1500:
            self.ipshourscalc = (self.numipaddress * .24 / 12) * self.nummonths
        elif enterednumipaddress >= 1000:
            self.ipshourscalc = (self.numipaddress * .25 / 12) * self.nummonths
        elif enterednumipaddress >= 750:
            self.ipshourscalc = (self.numipaddress * .26 / 12) * self.nummonths
        elif enterednumipaddress >= 500:
            self.ipshourscalc = (self.numipaddress * .27 / 12) * self.nummonths
        elif enterednumipaddress >= 250:
            self.ipshourscalc = (self.numipaddress * .28 / 12) * self.nummonths
        elif enterednumipaddress >= 200:
            self.ipshourscalc = (self.numipaddress * .29 / 12) * self.nummonths
        elif enterednumipaddress >= 100:
            self.ipshourscalc = (self.numipaddress * .30 / 12) * self.nummonths
        elif enterednumipaddress >= 50:
            self.ipshourscalc = (self.numipaddress * .31 / 12) * self.nummonths
        # else:
        #     self.wkstnshourscalc = self.base

        # AddlConsole Hours Calculation

        enterednumConsole = int(self.qty)
        # Hours Calculation for Server Line Item

        if enterednumConsole >= 200500:
            self.addlconhourscalc = int(
                ((0.0285 * self.productcomplexityfac) * self.qty) * (
                        self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumConsole > 200000:
            self.addlconhourscalc = (
                                            ((0.0275 * self.productcomplexityfac) * self.qty) * (
                                            self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumConsole >= 150000:
            self.addlconhourscalc = (
                                            ((0.055 * self.productcomplexityfac) * self.qty) * (
                                            self.productcomplexityfac * self.nummonths) / 12) + self.base
        elif enterednumConsole >= 100000:
            self.addlconhourscalc = (self.qty * .14 / 12) * self.nummonths
        elif enterednumConsole >= 100000:
            self.addlconhourscalc = (self.qty * .14 / 12) * self.nummonths
        elif enterednumConsole >= 85000:
            self.addlconhourscalc = (self.qty * .1425 / 12) * self.nummonths
        elif enterednumConsole >= 75000:
            self.addlconhourscalc = (self.qty * .145 / 12) * self.nummonths
        elif enterednumConsole >= 50000:
            self.addlconhourscalc = (self.qty * .135 / 12) * self.nummonths
        elif enterednumConsole >= 42000:
            self.addlconhourscalc = (self.qty * .16 / 12) * self.nummonths
        elif enterednumConsole >= 37000:
            self.addlconhourscalc = (self.qty * .163 / 12) * self.nummonths
        elif enterednumConsole >= 35000:
            self.addlconhourscalc = (self.qty * .165 / 12) * self.nummonths
        elif enterednumConsole >= 25000:
            self.addlconhourscalc = (self.qty * .17 / 12) * self.nummonths
        elif enterednumConsole >= 15000:
            self.addlconhourscalc = (self.qty * .18 / 12) * self.nummonths
        elif enterednumConsole >= 10000:
            self.addlconhourscalc = (self.qty * .19 / 12) * self.nummonths
        elif enterednumConsole >= 5000:
            self.addlconhourscalc = (self.qty * .195 / 12) * self.nummonths
        elif enterednumConsole >= 3000:
            self.addlconhourscalc = (self.qty * .2 / 12) * self.nummonths
        elif enterednumConsole >= 2601:
            self.addlconhourscalc = (self.qty * .21 / 12) * self.nummonths
        elif enterednumConsole >= 2600:
            self.addlconhourscalc = (self.qty * .22 / 12) * self.nummonths
        elif enterednumConsole >= 2000:
            self.addlconhourscalc = (self.qty * .23 / 12) * self.nummonths
        elif enterednumConsole >= 1500:
            self.addlconhourscalc = (self.qty * .24 / 12) * self.nummonths
        elif enterednumConsole >= 1000:
            self.addlconhourscalc = (self.qty * .25 / 12) * self.nummonths
        elif enterednumConsole >= 750:
            self.addlconhourscalc = (self.qty * .26 / 12) * self.nummonths
        elif enterednumConsole >= 500:
            self.addlconhourscalc = (self.qty * .27 / 12) * self.nummonths
        elif enterednumConsole >= 250:
            self.addlconhourscalc = (self.qty * .28 / 12) * self.nummonths
        elif enterednumConsole >= 200:
            self.addlconhourscalc = (self.qty * .29 / 12) * self.nummonths
        elif enterednumConsole >= 100:
            self.addlconhourscalc = (self.qty * .30 / 12) * self.nummonths
        elif enterednumConsole >= 50:
            self.addlconhourscalc = (self.qty * .31 / 12) * self.nummonths
        # else:
        #     self.enterednumConsole = self.base

        # region AppChange Hours Calc
        enterednumappchange = int(self.numappchange)
        newhoursfactor = 0.07031
        appchangecac = 0.25

        # Factor Calc
        # Wkstns

        if not self.prodcomponent1_wkstn:
            self.prodcomponent1_wkstnhours = 0
        else:
            self.prodcomponent1_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac1)

        if not self.prodcomponent2_wkstn:
            self.prodcomponent2_wkstnhours = 0
        else:
            self.prodcomponent2_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac2)

        if not self.prodcomponent3_wkstn:
            self.prodcomponent3_wkstnhours = 0
        else:
            self.prodcomponent3_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac3)

        if not self.prodcomponent4_wkstn:
            self.prodcomponent4_wkstnhours = 0
        else:
            self.prodcomponent4_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac4)

        if not self.prodcomponent5_wkstn:
            self.prodcomponent5_wkstnhours = 0
        else:
            self.prodcomponent5_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac5)

        if not self.prodcomponent6_wkstn:
            self.prodcomponent6_wkstnhours = 0
        else:
            self.prodcomponent6_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac6)

        if not self.prodcomponent7_wkstn:
            self.prodcomponent7_wkstnhours = 0
        else:
            self.prodcomponent7_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac7)

        if not self.prodcomponent8_wkstn:
            self.prodcomponent8_wkstnhours = 0
        else:
            self.prodcomponent8_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac8)

        if not self.prodcomponent9_wkstn:
            self.prodcomponent9_wkstnhours = 0
        else:
            self.prodcomponent9_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac9)

        if not self.prodcomponent10_wkstn:
            self.prodcomponent10_wkstnhours = 0
        else:
            self.prodcomponent10_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac10)

        if not self.prodcomponent11_wkstn:
            self.prodcomponent11_wkstnhours = 0
        else:
            self.prodcomponent11_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac11)

        if not self.prodcomponent12_wkstn:
            self.prodcomponent12_wkstnhours = 0
        else:
            self.prodcomponent12_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac12)

        if not self.prodcomponent13_wkstn:
            self.prodcomponent13_wkstnhours = 0
        else:
            self.prodcomponent13_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac13)

        if not self.prodcomponent14_wkstn:
            self.prodcomponent14_wkstnhours = 0
        else:
            self.prodcomponent14_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac14)

        if not self.prodcomponent15_wkstn:
            self.prodcomponent15_wkstnhours = 0
        else:
            self.prodcomponent15_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(
                self.product.componentcomplexityfac15)

        # Componemt Factor Calc
        # Servers

        if not self.prodcomponent1_svr:
            self.prodcomponent1_svrHours = 0
        else:
            self.prodcomponent1_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac1)

        if not self.prodcomponent2_svr:
            self.prodcomponent2_svrHours = 0
        else:
            self.prodcomponent2_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac2)

        if not self.prodcomponent3_svr:
            self.prodcomponent3_svrHours = 0
        else:
            self.prodcomponent3_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac3)

        if not self.prodcomponent4_svr:
            self.prodcomponent4_svrHours = 0
        else:
            self.prodcomponent4_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac4)

        if not self.prodcomponent5_svr:
            self.prodcomponent5_svrHours = 0
        else:
            self.prodcomponent5_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac5)

        if not self.prodcomponent6_svr:
            self.prodcomponent6_svrHours = 0
        else:
            self.prodcomponent6_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac6)

        if not self.prodcomponent7_svr:
            self.prodcomponent7_svrHours = 0
        else:
            self.prodcomponent7_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac7)

        if not self.prodcomponent8_svr:
            self.prodcomponent8_svrHours = 0
        else:
            self.prodcomponent8_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac8)

        if not self.prodcomponent9_svr:
            self.prodcomponent9_svrHours = 0
        else:
            self.prodcomponent9_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac9)

        if not self.prodcomponent10_svr:
            self.prodcomponent10_svrHours = 0
        else:
            self.prodcomponent10_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac10)

        if not self.prodcomponent11_svr:
            self.prodcomponent11_svrHours = 0
        else:
            self.prodcomponent11_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac11)

        if not self.prodcomponent12_svr:
            self.prodcomponent12_svrHours = 0
        else:
            self.prodcomponent12_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac12)

        if not self.prodcomponent13_svr:
            self.prodcomponent13_svrHours = 0
        else:
            self.prodcomponent13_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac13)

        if not self.prodcomponent14_svr:
            self.prodcomponent14_svrHours = 0
        else:
            self.prodcomponent14_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac14)

        if not self.prodcomponent15_svr:
            self.prodcomponent15_svrHours = 0
        else:
            self.prodcomponent15_svrHours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac15)

        # Componemt Factor Calc
        # IP/ Endpoint

        if self.prodcomponent1_IP is False:
            self.prodcomponent1_iphours = 0
        else:
            self.prodcomponent1_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac1)

        if self.prodcomponent2_IP is False:
            self.prodcomponent2_iphours = 0
        else:
            self.prodcomponent2_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac2)

        if self.prodcomponent3_IP is False:
            self.prodcomponent3_iphours = 0
        else:
            self.prodcomponent3_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac3)

        if self.prodcomponent4_IP is False:
            self.prodcomponent4_iphours = 0
        else:
            self.prodcomponent4_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac4)

        if self.prodcomponent5_IP is False:
            self.prodcomponent5_iphours = 0
        else:
            self.prodcomponent5_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac5)

        if self.prodcomponent6_IP is False:
            self.prodcomponent6_iphours = 0
        else:
            self.prodcomponent6_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac6)

        if self.prodcomponent7_IP is False:
            self.prodcomponent7_iphours = 0
        else:
            self.prodcomponent7_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac7)

        if self.prodcomponent8_IP is False:
            self.prodcomponent8_iphours = 0
        else:
            self.prodcomponent8_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac8)

        if self.prodcomponent9_IP is False:
            self.prodcomponent9_iphours = 0
        else:
            self.prodcomponent9_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac9)

        if self.prodcomponent10_IP is False:
            self.prodcomponent10_iphours = 0
        else:
            self.prodcomponent10_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac10)

        if self.prodcomponent11_IP is False:
            self.prodcomponent11_iphours = 0
        else:
            self.prodcomponent11_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac11)

        if self.prodcomponent12_IP is False:
            self.prodcomponent12_iphours = 0
        else:
            self.prodcomponent12_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac12)

        if self.prodcomponent13_IP is False:
            self.prodcomponent13_iphours = 0
        else:
            self.prodcomponent13_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac13)

        if self.prodcomponent14_IP is False:
            self.prodcomponent14_iphours = 0
        else:
            self.prodcomponent14_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac14)

        if self.prodcomponent15_IP is False:
            self.prodcomponent15_iphours = 0
        else:
            self.prodcomponent15_iphours = float(
                self.srvshourscalc) * float(self.product.componentcomplexityfac15)

        # self.prodcomponent2_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(self.product.componentcomplexityfac2)
        # self.prodcomponent3_wkstnhours = Decimal(self.wkstnshourscalc) * Decimal(self.product.componentcomplexityfac3)
        # self.prodcomponent4_wkstnhours = Decimal(self.wkstnshourscalc) *
        # Decimal(self.product.componentcomplexityfac4)

        # # Srvrs
        # self.prodcomponent1_svrHours = (self.srvshourscalc * self.componentcomplexityfac1)
        #
        # # IP/EPs
        # self.prodcomponent1_iphours = (self.ipshourscalc * self.componentcomplexityfac1)
        #
        self.prodcomponent1_ttl_hours = (
                float(
                    self.prodcomponent1_wkstnhours) +
                float(
                    self.prodcomponent1_svrHours) +
                float(
                    self.prodcomponent1_iphours))

        self.prodcomponent2_ttl_hours = (
                float(
                    self.prodcomponent2_wkstnhours) +
                float(
                    self.prodcomponent2_svrHours) +
                float(
                    self.prodcomponent2_iphours))

        self.prodcomponent3_ttl_hours = (
                float(
                    self.prodcomponent3_wkstnhours) +
                float(
                    self.prodcomponent3_svrHours) +
                float(
                    self.prodcomponent3_iphours))

        self.prodcomponent4_ttl_hours = (
                float(
                    self.prodcomponent4_wkstnhours) +
                float(
                    self.prodcomponent4_svrHours) +
                float(
                    self.prodcomponent4_iphours))

        self.prodcomponent5_ttl_hours = (
                float(
                    self.prodcomponent5_wkstnhours) +
                float(
                    self.prodcomponent5_svrHours) +
                float(
                    self.prodcomponent5_iphours))

        self.prodcomponent6_ttl_hours = (
                float(
                    self.prodcomponent6_wkstnhours) +
                float(
                    self.prodcomponent6_svrHours) +
                float(
                    self.prodcomponent6_iphours))

        self.prodcomponent7_ttl_hours = (
                float(
                    self.prodcomponent7_wkstnhours) +
                float(
                    self.prodcomponent7_svrHours) +
                float(
                    self.prodcomponent7_iphours))

        self.prodcomponent8_ttl_hours = (
                float(
                    self.prodcomponent8_wkstnhours) +
                float(
                    self.prodcomponent8_svrHours) +
                float(
                    self.prodcomponent8_iphours))

        self.prodcomponent9_ttl_hours = (
                float(
                    self.prodcomponent9_wkstnhours) +
                float(
                    self.prodcomponent9_svrHours) +
                float(
                    self.prodcomponent9_iphours))

        self.prodcomponent10_ttl_hours = (
                float(
                    self.prodcomponent10_wkstnhours) +
                float(
                    self.prodcomponent10_svrHours) +
                float(
                    self.prodcomponent10_iphours))

        self.prodcomponent11_ttl_hours = (
                float(
                    self.prodcomponent11_wkstnhours) +
                float(
                    self.prodcomponent11_svrHours) +
                float(
                    self.prodcomponent11_iphours))

        self.prodcomponent12_ttl_hours = (
                float(
                    self.prodcomponent12_wkstnhours) +
                float(
                    self.prodcomponent12_svrHours) +
                float(
                    self.prodcomponent12_iphours))

        self.prodcomponent13_ttl_hours = (
                float(
                    self.prodcomponent13_wkstnhours) +
                float(
                    self.prodcomponent13_svrHours) +
                float(
                    self.prodcomponent13_iphours))

        self.prodcomponent14_ttl_hours = (
                float(
                    self.prodcomponent14_wkstnhours) +
                float(
                    self.prodcomponent14_svrHours) +
                float(
                    self.prodcomponent14_iphours))

        self.prodcomponent15_ttl_hours = (
                float(
                    self.prodcomponent15_wkstnhours) +
                float(
                    self.prodcomponent15_svrHours) +
                float(
                    self.prodcomponent15_iphours))

        if enterednumappchange >= 1:
            self.appchangehourscalc = int(
                (newhoursfactor * self.numappchange) * appchangecac)
        elif enterednumappchange <= 0:
            self.appchangehourscalc = 0

        self.total_endpoints = self.numserver + self.numworkstation + self.numipaddress
        # self.totalhourscalc = self.srvshourscalc + self.wkstnshourscalc

        super().save(*args, **kwargs)
        self.order.save()

    def tag_total_endpoints(self):
        return f' {self.total_endpoints} '

    def tag_final_price(self):
        return f' {self.final_price} {CURRENCY}'

    def tag_discount(self):
        return f' {self.discount_price} {CURRENCY}'

    def tag_price(self):
        return f'{self.price} {CURRENCY}'

    def tag_final_totalhourscalc(self):
        return f' {Decimal(self.srvshourscalc) + Decimal(self.wkstnshourscalc) + Decimal(self.ipshourscalc)}'

    def tag_line_total_hours(self):
        return f'{self.final_price}'

    def tag_line_base_hours(self):
        return f'{Decimal(self.qty) * Decimal(self.price)}'


@receiver(post_delete, sender=OrderItem)
def delete_order_item(sender, instance, **kwargs):
    product = instance.product
    product.qty += instance.qty
    product.save()
    instance.order.save()
