from .models import Order
from rest_framework import serializers

class OrderCreationSerializer(serializers.ModelSerializer):
    size = serializers.CharField(max_length=20)
    order_status = serializers.HiddenField(default='PENDING')
    quantity = serializers.IntegerField()

    class Meta:
        model = Order
        fields = ['id', 'size', 'order_status', 'quantity']

class OrderDetailSerializer(serializers.ModelSerializer):
    size = serializers.CharField()
    order_status = serializers.CharField()
    quantity = serializers.IntegerField()
    created_at = serializers.DateTimeField()
    update_at = serializers.DateTimeField()

    class Meta:
        model = Order
        fields = ['id', 'size', 'order_status', 'quantity', 'created_at', 'update_at']

class OrderStausUpdateSerializer(serializers.ModelSerializer):
    order_status = serializers.CharField()

    class Meta:
        model = Order
        fields = ['order_status']