from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView
from django.shortcuts import render
from .views import *
from django.urls import path
from django.urls import include

router = SimpleRouter()
router.register('api', UserViewSet)

urlpatterns = [
   path('', include(router.urls)),
   path('token/', CustomTokenObtainPairView.as_view(), name='token'),
   path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

