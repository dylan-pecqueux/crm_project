import django_filters
from django_filters import rest_framework as filters
from .models import Contract


class ContractFilterSet(filters.FilterSet):
    company_name = django_filters.CharFilter(field_name="client__company_name")
    email = django_filters.CharFilter(field_name="client__email")

    class Meta:
        model = Contract
        fields = ["company_name", "email", "created_time", "amount"]
