from .models import AbdominalsData, WalkingData
from rest_framework import serializers


class WalkinDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalkingData
        fields = '__all__'


class AbdominalDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbdominalsData
        fields = '__all__'
