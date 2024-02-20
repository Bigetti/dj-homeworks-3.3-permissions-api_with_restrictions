from django_filters import rest_framework as filters
from django_filters import DateFromToRangeFilter, FilterSet
from .models import Advertisement



from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    published = DateFromToRangeFilter()

    class Meta:
        model = Advertisement
        fields = ['published']  # Указываете поля, по которым будет производиться фильтрация
