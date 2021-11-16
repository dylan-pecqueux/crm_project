from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .serializers import UserSerializer, ClientSerializer
from .models import Client
from .permissions import IsSales


class ClientView(viewsets.ViewSet):

    queryset = Client.objects.all()

    def create(self, request):
        serializer = ClientSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def get_permissions(self):
        if self.action == "create" or self.action == "list":
            permission_classes = [IsSales]
        return [permission() for permission in permission_classes]
