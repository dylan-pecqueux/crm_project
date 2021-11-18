from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, mixins
from django_filters.rest_framework import DjangoFilterBackend
from .serializers import (
    ClientSerializer,
    ContractSerializer,
    ContractDetailSerializer,
    EventSerializer,
    EventDetailSerializer,
    EventPatchSerializer,
)
from .models import Client, Contract, Event
from .permissions import IsSales, IsSalesContact, IsSupport, IsSupportContact
from .filters import ContractFilterSet, EventFilterSet


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


class MyClientsView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Client.objects.all()
    permission_classes = [IsSales]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["company_name", "email"]

    def list(self, request):
        user_clients = self.queryset.filter(sales_contact=request.user.pk)
        serializer = ClientSerializer(user_clients, many=True)
        return Response(serializer.data)


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


class MyContractsView(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Contract.objects.all()
    permission_classes = [IsSales]
    filter_backends = [DjangoFilterBackend]
    filter_class = ContractFilterSet

    def list(self, request):
        user_contracts = self.queryset.filter(sales_contact=request.user.pk)
        serializer = ContractSerializer(user_contracts, many=True)
        return Response(serializer.data)


class EventView(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend]
    filter_class = EventFilterSet

    def create(self, request):
        client_contract = get_object_or_404(Contract, id=request.data["event_status"])
        if request.data["client"] != client_contract.client.pk:
            return Response(
                data="The contract client and the client need to be the same",
                status=400,
            )
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        kwargs["partial"] = True
        return super().update(request, *args, **kwargs)

    def get_serializer_class(self):
        if self.action in ["create", "list"]:
            return EventSerializer
        if self.action == "update":
            return EventPatchSerializer
        if self.action == "retrieve":
            return EventDetailSerializer
        return EventSerializer

    def get_permissions(self):
        if self.action == "create":
            permission_classes = [IsSales]
        elif self.action == "retrieve" or self.action == "update":
            permission_classes = [IsAuthenticated, IsSupportContact]
        elif self.action == "list":
            permission_classes = [IsSales, IsSupport]
        return [permission() for permission in permission_classes]
