from rest_framework import serializers
from pos.models.shipmentmodels import *
from pos.models.inventorymodels import Inventory
from pos.models.cabangmodels import Cabang
from pos.models.models import Product
from pos.models.inventorymodels import ProductInventory
from pos.inventorysignals import incrementCabangInventory, reduceCabangInventory, incrementPusatInventory, reducePusatInventory


def createProductOrder(products, order):
        for productToCreate in products:
            productId = productToCreate.get("product")
            product = Product.objects.get(id=productId)
            ProductOrder.objects.create(
                product=product,
                order=order,
                quantity = productToCreate.get("quantity")
            )

def deleteSentOrder(order):
    try:
        OrderSent.objects.get(order=order).delete()
    except OrderSent.DoesNotExist:
        pass

def createSentOrder(order, detail):
    try:
        OrderSent.objects.get(order=order)
    except OrderSent.DoesNotExist:
        OrderSent.objects.create(
            order = order,
            detail = detail
        )

def reduceCabangInventoryFromOrder(order):
    try:
        productOrders = ProductOrder.objects.filter(order=order)
        cabang = order.cabang
        for productOrder in productOrders:
            reduceCabangInventory(cabang, productOrder.product, productOrder.quantity)
    except ProductOrder.DoesNotExist:
        pass

def incrementCabangInventoryFromOrder(order):
    try:
        productOrders = ProductOrder.objects.filter(order=order)
        cabang = order.cabang
        for productOrder in productOrders:
            incrementCabangInventory(cabang, productOrder.product, productOrder.quantity)
    except ProductOrder.DoesNotExist:
        pass

def reducePusatInventoryFromOrder(order):
    try:
        productOrders = ProductOrder.objects.filter(order=order)
        for productOrder in productOrders:
            reducePusatInventory(productOrder.product, productOrder.quantity)
    except ProductOrder.DoesNotExist:
        pass

def incrementPusatInventoryFromOrder(order):
    try:
        productOrders = ProductOrder.objects.filter(order=order)
        for productOrder in productOrders:
            incrementPusatInventory(productOrder.product, productOrder.quantity)
    except ProductOrder.DoesNotExist:
        pass

def createSentOrderWithProducts(order, detail, products):
    OrderSent.objects.create(
        order = order,
        detail = detail
    )

    createProductOrder(products, order)

class CreateProductOrderSerializers(serializers.ModelSerializer):
    product = serializers.IntegerField(read_only=False)

    class Meta:
        model = ProductOrder
        fields = [
            'product',
            'quantity'
        ]

class CreateRequestOrderSerializer(serializers.ModelSerializer):
    detail = serializers.CharField(allow_null=True, required=False)
    products = CreateProductOrderSerializers(many=True, required=True)
    cabang = serializers.IntegerField(required=True)

    class Meta:
        model = OrderRequest
        fields = [
            'cabang',
            'products',
            'detail'
        ]

    def create(self, validated_data):
        cabangId = validated_data.get('cabang')
        cabang = Cabang.objects.get(id=cabangId)

        order = Order.objects.create(
            cabang = cabang
        )
        orderRequest = OrderRequest.objects.create(
            order = order
        )

        products = validated_data.get('products')
        createProductOrder(products, order)

        return validated_data



class UpdateStatusRequestOrderSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=True)
    status = serializers.ChoiceField(STATUS_CHOICES_LIST, required=True)
    detail = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = OrderRequest
        fields = [
            'id',
            'status',
            'detail'
        ]

    def create(self, validated_data):
        status = validated_data.get("status")
        orderRequestId = validated_data.get("id")
        detail = validated_data.get("detail")

        orderRequest = OrderRequest.objects.get(id=orderRequestId)

        if (status != PENDING and orderRequest.status != status):
            order = orderRequest.order
            if (orderRequest.status == APPROVE and status == REJECT):
                deleteSentOrder(order)  
                incrementPusatInventoryFromOrder(order)
            elif (orderRequest.status == PENDING and status == REJECT):
                pass
            else :
                createSentOrder(order, detail)
                reducePusatInventoryFromOrder(order)            

            orderRequest.status = status
            orderRequest.save()

        return validated_data

class CreateSentOrderSerializer(serializers.ModelSerializer):
    cabang = serializers.IntegerField(read_only=False, required=True)
    detail = serializers.CharField(allow_null=True, required=False)
    products = CreateProductOrderSerializers(many=True)

    class Meta:
        model = OrderSent
        fields = [
            'cabang', 
            'detail',
            'products'
        ]

    def create(self, validated_data):
        cabangId = validated_data.get("cabang")
        cabang = Cabang.objects.get(id=cabangId)

        order = Order.objects.create(
            cabang = cabang
        )

        detail = validated_data.get("detail")
        products = validated_data.get('products')

        createSentOrderWithProducts(order, detail, products)
        return validated_data

class UpdateSentOrderSerializers(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=False, required=True)
    status = serializers.ChoiceField(STATUS_ORDER_SHIPMENT, required=True)
    detail = serializers.CharField(allow_null=True, required=False)

    class Meta:
        model = OrderSent
        fields = [
            'id',
            'status',
            'detail'
        ]

    def create(self, validated_data):
        status = validated_data.get("status")
        orderSentId = validated_data.get("id")
        detail = validated_data.get("detail")

        orderSent = OrderSent.objects.get(id=orderSentId)
        
        if (orderSent.status != status and status != INSHIPMENT):
            if orderSent.status == INSHIPMENT:
                if status == RECEIVED:
                    incrementCabangInventoryFromOrder(orderSent.order)
            elif orderSent.status == RECEIVED:
                if status == REJECT:
                    reduceCabangInventoryFromOrder(orderSent.order)
            elif orderSent.status == REJECT:
                if status == RECEIVED:
                    incrementCabangInventoryFromOrder(orderSent.order)

            orderSent.status = status
            orderSent.save()
        return validated_data

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = [
            'courier',
            'trackingId',
            'detail'
        ]

class CreateReturnOrderFromSentOrderSerializer(serializers.Serializer):
    sentOrderId = serializers.IntegerField(required=True)
    detail = serializers.CharField(allow_null=True, required=False)

    def create(self, validated_data):
        sentOrderId = validated_data.get("sentOrderId")
        orderSent = OrderSent.objects.get(id=sentOrderId)

        try:
            OrderReturn.objects.get(
                order = orderSent.order
            )
        except OrderReturn.DoesNotExist:
            OrderReturn.objects.create(
                order = orderSent.order
            )
        
        lastStatus = orderSent.status

        orderSent.status = REJECT
        orderSent.save()
        if lastStatus == RECEIVED:
            reduceCabangInventoryFromOrder(orderSent.order)
        return validated_data


class CreateReturnOrderSerializer(serializers.Serializer):
    products = CreateProductOrderSerializers(many=True, required=False, allow_null=True)
    cabang = serializers.IntegerField(read_only=False)

    def create(self, validated_data):
        cabangId = validated_data.get('cabang')
        cabang = Cabang.objects.get(id = cabangId)

        order = Order.objects.create(
            cabang=cabang
        )

        OrderReturn.objects.create(
            order = order
        )

        products = validated_data.get('products')

        if products != None:
            createProductOrder(products, order)
            reduceCabangInventoryFromOrder(order)
            
        return validated_data
        

class UpdateReturOrderSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=False, required=True)
    status = serializers.ChoiceField(STATUS_ORDER_SHIPMENT, required=True)
    detail = serializers.CharField(allow_null=True, required=False)

    def create(self, validated_data):
        status = validated_data.get("status")
        orderReturnId = validated_data.get("id")
        detail = validated_data.get("detail")

        orderReturn = OrderReturn.objects.get(id = orderReturnId)
        order = orderReturn.order
        if (orderReturn.status != status and status != INSHIPMENT):
            if orderReturn.status == INSHIPMENT:
                if status == RECEIVED:
                    incrementPusatInventoryFromOrder(order)
            elif orderReturn.status == RECEIVED:
                if status == REJECT:
                    reducePusatInventoryFromOrder(order)
            elif orderReturn.status == REJECT:
                if status == RECEIVED:
                    incrementPusatInventoryFromOrder(order)

            orderReturn.status = status
            orderReturn.save()

        return validated_data

