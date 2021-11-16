from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import ClientSerializer
from .models import Client
from .permissions import IsSales, IsSalesContact


class ClientView(viewsets.ModelViewSet):

    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["id", "company_name"]
    search_fields = ["=company_name"]
    ordering_fields = ["company_name", "id"]
    ordering = ["id"]

    def get_permissions(self):
        if self.action == "create" or self.action == "list":
            permission_classes = [IsSales]
        elif self.action == "retrieve" or self.action == "update":
            permission_classes = [IsAuthenticated, IsSalesContact]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
