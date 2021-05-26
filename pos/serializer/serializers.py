from rest_framework import serializers
from django.contrib.auth.models import User, Group
from pos.models.models import Product, Snippet, LANGUAGE_CHOICE, STYLE_CHOICE, Promotion

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id', 
            'description', 
            'hargaBeli', 
            'hargaJual', 
            'barcode', 
            'returnable'
            )

class PromotionSerializer(serializers.HyperlinkedModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Promotion
        fields = ['name', 'description', 'dateFrom', 'dateTo', 'created', 'percentage', 'products']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'snippets']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


