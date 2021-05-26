from rest_framework.generics import ListAPIView
from pos.models.inventorymodels import ProductInventory
from pos.serializer.productinventoryserializer import ProductInventorySerilizer
from rest_framework.response import Response
from django.db.models import Q


class CabangInventoryViews(ListAPIView):
        queryset = ProductInventory.objects
        serializer_class = ProductInventorySerilizer

        def list(self, request, *args, **kwargs):
                queryParam = request.query_params
                cabang = queryParam.get('cabang')
                prodDesc = queryParam.get('desc')

                if ( prodDesc is None ):
                        return Response([])

                productInventories = ProductInventory.objects.filter(
                        Q(inventory__cabang__id = cabang) &
                        ( Q(product__description__contains = prodDesc) | 
                        Q(product__barcode__contains = prodDesc) )
                )
                ser = ProductInventorySerilizer(data = productInventories, many=True, context={})
                
                ser.is_valid()
                return Response({
                        'results': ser.data
                        })




            
