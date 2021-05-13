from rest_framework import viewsets
from rest_framework.generics import CreateAPIView
from pos.models.financemodels import *
from pos.serializer.financeserializers import *
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAuthenticated]

class SalesTransactionViewSet(viewsets.ModelViewSet):
    queryset = SalesTransaction.objects.all()
    serializer_class = GetSalesTransactionSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=sales_id']
    permission_classes = [IsAuthenticated]

class CreateSalesTransactionView(CreateAPIView):
    queryset = SalesTransaction.objects.all()
    serializer_class = CreateSalesTransactionSerializer
    permission_classes = [IsAuthenticated]

class CreateReturSalesTransactionView(CreateAPIView):
    queryset = SalesTransaction.objects.all()
    serializer_class = CreateReturSalesTransactionSerializer
    permission_classes = [IsAuthenticated]
    