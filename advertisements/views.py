from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement, AdvertisementStatusChoices
from .serializers import AdvertisementSerializer
from django_filters.rest_framework import DjangoFilterBackend

 


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'created_at']


    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update"]:
            return [IsAuthenticated()]
        return []

    
    def list(self, request, *args, **kwargs):
        """Получение списка объявлений."""
        print("List view called with request data:", request.data)
        # Вызываем базовый метод list
        return super().list(request, *args, **kwargs)