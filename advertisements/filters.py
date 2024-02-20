from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter, FilterSet
from .models import Advertisement



from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    creator = filters.NumberFilter(field_name='creator_id')

    created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    
    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at_before']