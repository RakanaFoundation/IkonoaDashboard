from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from pos.models.usermodels import Employee
from django.core import serializers


class LoginTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(LoginTokenObtainPairSerializer, cls).get_token(user)
        employee = Employee.objects.get(user = user)

        # Add custom claims
        token['user'] = {
                'username': user.username, 
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': user.date_joined.isoformat(),
                'is_superuser': user.is_superuser,
                'email': user.email
            }
            
        token['cabang'] = {
            'id': employee.cabang.id,
            'address': employee.cabang.address,
            'phone': employee.cabang.phone,
            'email': employee.cabang.email,
            'name': employee.cabang.name,
            'code': employee.cabang.code,
            'dist': employee.cabang.dist.name
        }

        return token
  