from rest_framework.permissions import BasePermission



class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        # Добавляем проверку на метод 'GET' и статус 'OPEN'
        if request.method == 'GET' and request.query_params.get('status') == 'OPEN':
            return True
        return request.user and request.user.is_authenticated
    

    def has_object_permission(self, request, view, obj):
        
        return request.user == obj.author or request.method == 'GET' or request.user.is_staff