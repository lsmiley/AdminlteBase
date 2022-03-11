import django_filters
from .models import Sizingtype


class SizingtypeFilter(django_filters.FilterSet):                            # Sizingtypefilter used to filter based on name

    Sizingtypename = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Sizingtype
        fields = ['Sizingtypename']
