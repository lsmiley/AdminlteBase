from rest_framework import serializers

from . import models


class TestquestionnaireManagerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestquestionnaireManager
        fields = [
        ]


class TestquestionnaireSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Testquestionnaire
        fields = [
            "date",
            "timestamp",
            "title",
            "rfs_num",
            "sales_connect_num",
            "appttus_num",
            "sizingtype",
            "due_date",
            "PricingStructureSelect",
            "team",
            "assigned_by",
            "assigned_to",
            "RequesterFirstName",
            "RequesterLastName",
            "RequesterRole",
            "RequesterEmail",
            "CustomerName",
            "CustomerStatus",
            "Solution_Design",
            "SalesContactName",
            "SalesContactEmail",
            "TranStartDate",
            "Firm_Price_or_NBIE",
            "Service_Delivery_Requirements",
            "Solution_Owner",
            "Revenue_Structure_Select",
            "Revenue_Structure_Cost_Explain",
            "Restricted_Delivery",
            "Restricted_Delivery_Explanation",
            "Questionnaire_num_consoles",
            "Questionnaire_num_workstation",
            "Questionnaire_num_server",
            "Questionnaire_num_ipaddress",
            "Questionnaire_num_total_endpoints",
            "AntiVirusMalware",
            "DLP_on_Workstations",
            "DLP_on_Servers",
            "Encryption_on_Workstations",
            "Encryption_on_Servers",
            "prodcomponent1_wkstn",
            "NAS_Storage",
            "Windows",
            "AIX",
            "VDI",
            "URL_Filtering",
            "HIPs_on_Workstations",
            "HIPs_on_Servers",
            "Firewall_on_Workstations",
            "Firewall_on_Servers",
            "BigFix_Patching_Scanning",
            "Linux",
            "Integrity_Monitoring",
            "Citrix",
            "Other_Features_or_Platforms",
            "Other_Features_or_Platforms_Note",
            "Environment_and_Platforms_Note",
            "EmsServiceRequested",
        ]


class TestquestionnaireItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.TestquestionnaireItem
        fields = [
            "qty",
            "price",
            "discount_price",
            "base",
            "discount_base",
            "fte",
            "discount_fte",
            "numworkstation",
            "numserver",
            "numipaddress",
            "total_endpoints",
            "desc",
            "numappchange",
            "srvshourscalc",
            "deliveryoption",
            "regions",
            "currencytype",
            "defaultfte_year",
            "workweek",
            "deliveryctrcostfactor",
            "band2count",
            "band2percentage",
            "band3count",
            "band3percentage",
            "band4count",
            "band4percentage",
            "band5count",
            "band5percentage",
            "band6count",
            "band6percentage",
            "band7count",
            "band7percentage",
            "band8count",
            "band8percentage",
            "band9count",
            "band9percentage",
            "band10count",
            "band10percentage",
            "bandstotalcount",
            "bandstotalpercentage",
            "nummonths",
            "prodcomponent1_wkstn",
            "prodcomponent1_wkstnhours",
            "prodcomponent1_svrHours",
            "prodcomponent1_iphours",
            "prodcomponent2_wkstn",
            "prodcomponent2_wkstnhours",
            "prodcomponent2_svrHours",
            "prodcomponent2_iphours",
            "prodcomponent3_wkstn",
            "prodcomponent3_wkstnhours",
            "prodcomponent3_svrHours",
            "prodcomponent3_iphours",
            "prodcomponent4_wkstn",
            "prodcomponent4_wkstnhours",
            "prodcomponent4_svrHours",
            "prodcomponent4_iphours",
            "prodcomponent5_wkstn",
            "prodcomponent5_wkstnhours",
            "prodcomponent5_svrHours",
            "prodcomponent5_iphours",
            "prodcomponent6_wkstn",
            "prodcomponent6_wkstnhours",
            "prodcomponent6_svrHours",
            "prodcomponent6_iphours",
            "prodcomponent7_wkstn",
            "prodcomponent7_wkstnhours",
            "prodcomponent7_svrHours",
            "prodcomponent7_iphours",
            "prodcomponent8_wkstn",
            "prodcomponent8_wkstnhours",
            "prodcomponent8_svrHours",
            "prodcomponent8_iphours",
            "prodcomponent9_wkstn",
            "prodcomponent9_wkstnhours",
            "prodcomponent9_svrHours",
            "prodcomponent9_iphours",
            "prodcomponent10_wkstn",
            "prodcomponent10_wkstnhours",
            "prodcomponent10_svrHours",
            "prodcomponent10_iphours",
            "prodcomponent11_wkstn",
            "prodcomponent11_wkstnhours",
            "prodcomponent11_svrHours",
            "prodcomponent11_iphours",
            "prodcomponent12_wkstn",
            "prodcomponent12_wkstnhours",
            "prodcomponent12_svrHours",
            "prodcomponent12_iphours",
            "prodcomponent13_wkstn",
            "prodcomponent13_wkstnhours",
            "prodcomponent13_svrHours",
            "prodcomponent13_iphours",
            "prodcomponent14_wkstn",
            "prodcomponent14_wkstnhours",
            "prodcomponent14_svrHours",
            "prodcomponent14_iphours",
            "prodcomponent15_wkstn",
            "prodcomponent15_wkstnhours",
            "prodcomponent15_svrHours",
            "prodcomponent15_iphours",
            "softlifesvryesno",
            "softlifesrvhourscalc",
            "prodimage",
        ]