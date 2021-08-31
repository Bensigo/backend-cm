from rest_framework import serializers
from .models import BtcRate

class BtcRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = BtcRate
        fields = [
            'name',
            'exchange_rate',
            'last_refresh',
            'date',
            'currency'
        ]
        extra_kwargs = {
           "last_refresh" : { "required": False }
        }