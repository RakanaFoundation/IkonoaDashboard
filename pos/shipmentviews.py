from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .models import Faktur
from .shipmentserializers import CreateFakturSerializer

class CreateFakturView(CreateAPIView):
    queryset = Faktur.objects.all()
    serializer_class = CreateFakturSerializer