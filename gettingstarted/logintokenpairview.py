from pos.models.usermodels import Employee
from django.core import serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class LoginTokenPairView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})

        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        employee = Employee.objects.get(user = user)

        return Response({
            'token': token.key,
            'user': {
                'id': user.id,
                'username': user.username, 
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': user.date_joined.isoformat(),
                'is_superuser': user.is_superuser,
                'email': user.email
            },
            'cabang':  {
                'id': employee.cabang.id,
                'address': employee.cabang.address,
                'phone': employee.cabang.phone,
                'email': employee.cabang.email,
                'name': employee.cabang.name,
                'code': employee.cabang.code,
                'dist': employee.cabang.dist.name
            }
        })