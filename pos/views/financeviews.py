from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from pos.models.financemodels import *
from pos.serializer.financeserializers import *
from rest_framework import filters


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

class SalesTransactionViewSet(viewsets.ModelViewSet):
    queryset = SalesTransaction.objects.all()
    serializer_class = GetSalesTransactionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=sales_id']

class CreateSalesTransactionView(CreateAPIView):
    queryset = SalesTransaction.objects.all()
    serializer_class = CreateSalesTransactionSerializer

class CreateReturSalesTransactionView(CreateAPIView):
    queryset = SalesTransaction.objects.all()
    serializer_class = CreateReturSalesTransactionSerializer
    