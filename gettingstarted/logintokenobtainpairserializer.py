from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from pos.models.usermodels import Employee
from django.core import serializers


class LoginTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginTokenObtainPairSerializer, cls).get_token(user)
        employee = Employee.objects.get(user = user)

        userSerialized = serializers.serialize('json', [ user, ])
        cabangSerializer = serializers.serialize('json', [ employee.cabang, ])

        # Add custom claims
        token['user'] = userSerialized
        token['cabang'] = cabangSerializer
        return token
  