from rest_framework import serializers
from pos.shipmentmodels import Order, OrderReceived
from pos.shipmentmodels import OrderRequest, OrderReturn, OrderSent
from pos.shipmentmodels import Shipment

class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        field = [
            'courier',
            'trackingId',
            'detail'
        ]

class CreateReturnOrderSerializer(serializers.ModelSerializer):
    shipment = ShipmentSerializer(many=False)

    class Meta:
        model = Order
        field = [
            'cabang',
            'shipment'
        ]