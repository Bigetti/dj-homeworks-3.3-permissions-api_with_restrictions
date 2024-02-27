from rest_framework import generics
from django_filters import rest_framework as filters
from .models import Advertisement
from .permissions import IsAuthenticatedOrReadOnly, IsAuthor



from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    creator = filters.NumberFilter(field_name='creator_id')

    created_at_before = filters.DateFilter(field_name='created_at', lookup_expr='lte')

    status = filters.CharFilter(field_name='status')





    
    class Meta:
        model = Advertisement
        fields = ['creator', 'created_at_before', 'status']