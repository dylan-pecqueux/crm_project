from rest_framework.permissions import BasePermission


class IsSales(BasePermission):

    message = "Access not allowed ! Only sales team can access"

    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name="sales"):
            return True
        return False


class IsSupport(BasePermission):

    message = "Access not allowed ! Only support team can access"

    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name="support"):
            return True
        return False
