from rest_framework import serializers
from .model import Payment

class PaymentSerializer(serializers.ModelSerializer):
    user_email = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ['id', 'user', 'user_email', 'amount', 'order', 'status', 'reference', 'time']

    def get_user_email(self, obj):
        return obj.user.email
