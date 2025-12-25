from rest_framework.permissions import BasePermission

class IsFieldExecutive(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='FIELD_EXECUTIVE').exists()


class IsSupervisor(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='SUPERVISOR').exists()
