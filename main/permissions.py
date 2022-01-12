from rest_framework.permissions import BasePermission


class IsAuthor(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.is_authenticated and\
            request.user == obj.user


class IsAdmin(BasePermission):
    # CREATE, LIST
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        return request.user.is_authenticated and \
               request.user.is_staff
