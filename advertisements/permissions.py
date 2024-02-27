from rest_framework.permissions import BasePermission, SAFE_METHODS



class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        # Добавляем проверку на метод 'GET' и статус 'OPEN'
        if request.method == 'GET' and request.query_params.get('status') == 'OPEN':
            return True
        return request.user and request.user.is_authenticated
    

    def has_object_permission(self, request, view, obj):
        
        return request.user == obj.author or request.method == 'GET' or request.user.is_staff
    

class IsAuthenticatedOrReadOnly(BasePermission):
    """
    The request is authenticated as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return (
            request.method in SAFE_METHODS or
            request.user and
            request.user.is_authenticated
        )