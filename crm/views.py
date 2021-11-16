from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import ClientSerializer
from .models import Client
from .permissions import IsSales, IsSalesContact


class ClientView(viewsets.ViewSet):

    queryset = Client.objects.all()

    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        client = get_object_or_404(self.queryset, pk=pk)
        self.check_object_permissions(self.request, client)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def update(self, request, pk=None):
        client = get_object_or_404(self.queryset, pk=pk)
        self.check_object_permissions(self.request, client)
        serializer = ClientSerializer(client, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == "create" or self.action == "list":
            permission_classes = [IsSales]
        elif self.action == "retrieve" or self.action == "update":
            permission_classes = [IsAuthenticated, IsSalesContact]
        return [permission() for permission in permission_classes]
