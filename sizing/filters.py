import django_filters
from .models import Sizing


class SizingFilter(django_filters.FilterSet):                            # Sizingtypefilter used to filter based on name

    Sizing = django_filters.CharFilter(lookup_expr='icontains')           # allows filtering without entering the full name

    class Meta:
        model = Sizing
        fields = ['Sizing']
