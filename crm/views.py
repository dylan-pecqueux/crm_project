from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ClientSerializer, ContractSerializer, ContractDetailSerializer
from .models import Client, Contract
from .permissions import IsSales, IsSalesContact
from .filters import ContractFilterSet


class ClientView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["company_name", "email"]

    def get_permissions(self):
        if self.action == "create" or self.action == "list":
            permission_classes = [IsSales]
        elif self.action == "retrieve" or self.action == "update":
            permission_classes = [IsAuthenticated, IsSalesContact]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]


class ContractView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Contract.objects.all()
    filter_backends = [DjangoFilterBackend]
    filter_class = ContractFilterSet

    def create(self, request):
        request.data["sales_contact"] = request.user.pk
        serializer = ContractSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ["create", "update"]:
            return ContractSerializer
        if self.action in ["retrieve", "list"]:
            return ContractDetailSerializer
        return ContractSerializer

    def get_permissions(self):
        if self.action == "create" or self.action == "list":
            permission_classes = [IsSales]
        elif self.action == "retrieve" or self.action == "update":
            permission_classes = [IsAuthenticated, IsSalesContact]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
