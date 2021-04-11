from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import Product, Snippet, LANGUAGE_CHOICE, STYLE_CHOICE, Promotion

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

# class SnippetSerializer(serializers.Serializer):
#     class Meta:
#         id = serializers.IntegerField(read_only=True)
#         title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#         code = serializers.CharField(style={'base_template': 'textarea.html'})
#         linenos = serializers.BooleanField(required=False)
#         language = serializers.ChoiceField(choices=LANGUAGE_CHOICE, default='python')
#         style = serializers.ChoiceField(choices=STYLE_CHOICE, default='friendly')

#         def create(self, validated_data):
#             return Snippet.objects.create(validated_data)

#         def update(self, instance, validated_data):
#             instance.title = validated_data.get('title', instance.title)
#             instance.code = validated_data.get('code', instance.code)
#             instance.linenos = validated_data.get('linenos', instance.linenos)
#             instance.language = validated_data.get('language', instance.language)
#             instance.style = validated_data.get('style', instance.style)
#             instance.save()
#             return instance

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Snippet
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style', 'owner']


