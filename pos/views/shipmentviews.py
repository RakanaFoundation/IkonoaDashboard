from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from pos.models.models import Faktur
from pos.models.shipmentmodels import *
from pos.serializer.shipmentserializers import CreateFakturSerializer
from pos.serializer.orderserializers import *
from rest_framework.permissions import IsAuthenticated

class CreateFakturView(CreateAPIView):
    queryset = Faktur.objects.all()
    serializer_class = CreateFakturSerializer
    permission_classes = [IsAuthenticated]

class CreateRequestOrder(CreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = CreateRequestOrderSerializer
    permission_classes = [IsAuthenticated]

class UpdateStatusRequestOrder(CreateAPIView):
    queryset = OrderRequest.objects.all()
    serializer_class = UpdateStatusRequestOrderSerializers
    permission_classes = [IsAuthenticated]

class CreateSentOrder(CreateAPIView):
    queryset = OrderSent.objects.all()
    serializer_class = CreateSentOrderSerializer
    permission_classes = [IsAuthenticated]

class UpdateStatusSentOrder(CreateAPIView):
    queryset = OrderSent.objects.all()
    serializer_class = UpdateSentOrderSerializers
    permission_classes = [IsAuthenticated]

class CreateReturnOrder(CreateAPIView):
    queryset = OrderReturn.objects.all()
    serializer_class = CreateReturnOrderSerializer
    permission_classes = [IsAuthenticated]

class CreateReturnOrderFromSentOrder(CreateAPIView):
    queryset = OrderReturn.objects.all()
    serializer_class = CreateReturnOrderFromSentOrderSerializer
    permission_classes = [IsAuthenticated]

class UpdateReturOrderSerializers(CreateAPIView):
    queryset = OrderReturn.objects.all()
    serializer_class = UpdateReturOrderSerializers
    permission_classes = [IsAuthenticated]