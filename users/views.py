from .models import CustomUser
from rest_framework import serializers
from rest_framework.renderers import JSONRenderer
from rest_framework import viewsets
from .serializers import CustomTokenObtainSerializer, CustomUserSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    renderer_classes = [JSONRenderer]
    serializer_class = CustomUserSerializer

    # AUTENTICACIÓN
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_permissions(self):
        if self.request.method in ["POST", "PUT", "DELETE"]:
            return [IsAuthenticated()]
        return []

from rest_framework_simplejwt.views import TokenObtainPairView
class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
