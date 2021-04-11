from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from .financemodels import *
from .financeserializers import *

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class SalesTransactionViewSet(viewsets.ModelViewSet):
    queryset = SalesTransaction.objects.all()
    serializer_class = GetSalesTransactionSerializer


class CreateSalesTransactionView(CreateAPIView):
    queryset = SalesTransaction.objects.all()
    serializer_class = CreateSalesTransactionSerializer