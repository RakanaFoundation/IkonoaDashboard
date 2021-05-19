from django.contrib.auth.models import User, Group
from django.shortcuts import render
from rest_framework import viewsets, permissions
from pos.serializer.serializers import ProductSerializer, UserSerializer, GroupSerializer, SnippetSerializer
from pos.serializer.serializers import PromotionSerializer
from pos.models.models import Product
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from pos.models.models import Snippet
from django.http import Http404
from rest_framework.views import APIView
from rest_framework import permissions
from pos.permissions import IsOwnerOrReadOnly
from rest_framework import filters
from pos.models.models import Promotion

class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['$description', '$barcode']
    

    def get_queryset(self):
        queryset = Product.objects.all()
        return queryset

class ProductPromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username', 'email']


class GroupViewSet(viewsets.ModelViewSet):
    """
    Api point that lets group to be viewed or edited
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
