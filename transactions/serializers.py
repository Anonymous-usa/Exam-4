from .models import Transaction
from rest_framework import serializers


class TransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Transaction
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']
        extra_kwargs = {
            'amount': {'required': True},
            'transaction_type': {'required': True},
            'date': {'required': True},
        }