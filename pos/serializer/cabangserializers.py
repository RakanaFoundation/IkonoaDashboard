from rest_framework import serializers
from pos.models.cabangmodels import Cabang

class CabangSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cabang
        fields = [ 'id', 'address', 'phone', 'email', 'name']