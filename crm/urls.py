from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import ClientView, ContractView, MyContractsView, MyClientsView, EventView


router = DefaultRouter()
router.register(r"client", ClientView)
router.register(r"contract", ContractView)
router.register(r"event", EventView)
router.register(r"my_contracts", MyContractsView)
router.register(r"my_clients", MyClientsView)

urlpatterns = [
    path("", include(router.urls)),
    path("login/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("login/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
