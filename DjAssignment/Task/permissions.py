from rest_framework import permissions

class IsNotEmployee(permissions.BasePermission):
    """
    Custom permission to prohibit users with role 'Employee' from performing certain actions.
    """

    def has_permission(self, request, view):
        # If user has role 'Employee', deny permission
        return not (hasattr(request.user, 'role') and request.user.role == 'Employee')
