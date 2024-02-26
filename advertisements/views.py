from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from .models import Advertisement

from rest_framework import permissions
from .serializers import AdvertisementSerializer
from .filters import AdvertisementFilter
 


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_class = AdvertisementFilter

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['status', 'created_at']
    ordering_fields = ['id']
    ordering = ['id']  # Сортировка по возрастанию id по умолчанию


    def perform_update(self, serializer):
        advertisement = serializer.instance
        if advertisement.creator != self.request.user:
            raise PermissionError("You do not have permission to perform this action.")
        serializer.save()
    
    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise PermissionError("You do not have permission to perform this action.")

        instance.delete()


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