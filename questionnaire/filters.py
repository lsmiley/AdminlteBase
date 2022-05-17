import django_filters
from django_filters import DateFilter, CharFilter

from .models import *


class QuestionnaireFilter(django_filters.FilterSet):
    # start_date = DateFilter(field_name="date", lookup_expr='gte')
    # end = date = DateFilter(field_name="date", lookup_expr='lte')
    rfs_num = CharFilter(field_name='rfs_num', lookup_expr='icontains')
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Questionnaire
        fields = ['rfs_num', 'sales_connect_num', 'appttus_num', 'title', 'prepardedby', 'assigned_to']


class DashboardQuestionnaireFilter(django_filters.FilterSet):                            # prodvendorfilter used to filter based on name
    title = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name
    # start_date = DateFilter(field_name="date", lookup_expr='gte')
    # end = date = DateFilter(field_name="date", lookup_expr='lte')
    # rfs_num = CharFilter(field_name='rfs_num', lookup_expr='icontains')
    # title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Questionnaire
        fields = ['rfs_num', 'sales_connect_num', 'appttus_num', 'title', 'prepardedby', 'assigned_to']


