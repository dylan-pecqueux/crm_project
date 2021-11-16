from rest_framework.permissions import BasePermission
from .models import Client


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


class IsSalesContact(BasePermission):

    message = "Access not allowed ! Only the sales contact can access"

    def has_object_permission(self, request, view, obj):
        is_sales_contact = Client.objects.get(email=obj.email)
        return is_sales_contact.sales_contact == request.user
