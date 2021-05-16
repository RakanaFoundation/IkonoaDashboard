from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .logintokenobtainpairserializer import LoginTokenObtainPairSerializer


class LoginTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginTokenObtainPairSerializer