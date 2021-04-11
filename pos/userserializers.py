from rest_framework import serializers
from .usermodels import Employee
from .cabangserializers import CabangSerializer
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['username', 'email']

class EmployeeSerializers(serializers.ModelSerializer):
    cabang = CabangSerializer(many=False)
    user = UserSerializer(many=False)

    class Meta: 
        model = Employee
        fields = ['id', 'user', 'cabang']