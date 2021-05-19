from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from pos.models.models import Faktur
from pos.models.shipmentmodels import *
from pos.serializer.shipmentserializers import CreateFakturSerializer
from pos.serializer.orderserializers import *


class CreateFakturView(CreateAPIView):
    queryset = Faktur.objects.all()
    serializer_class = CreateFakturSerializer
    

class CreateRequestOrder(CreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = CreateRequestOrderSerializer
    

class UpdateStatusRequestOrder(CreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = UpdateStatusRequestOrderSerializers
    

class CreateSentOrder(CreateAPIView):
    queryset = OrderSent.objects.all()
    serializer_class = CreateSentOrderSerializer
    

class UpdateStatusSentOrder(CreateAPIView):
    queryset = OrderSent.objects.all()
    serializer_class = UpdateSentOrderSerializers
    

class CreateReturnOrder(CreateAPIView):
    queryset = OrderReturn.objects.all()
    serializer_class = CreateReturnOrderSerializer
    

class CreateReturnOrderFromSentOrder(CreateAPIView):
    queryset = OrderReturn.objects.all()
    serializer_class = CreateReturnOrderFromSentOrderSerializer
    

class UpdateReturOrderSerializers(CreateAPIView):
    queryset = OrderReturn.objects.all()
    serializer_class = UpdateReturOrderSerializers
    