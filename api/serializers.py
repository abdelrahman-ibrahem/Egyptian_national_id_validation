from rest_framework import serializers
from .util.generic import validate_egyptian_id, extract_data_from_id
from .models import APIRequestLog
from django.utils import timesince


class IDValidationSerializer(serializers.Serializer):
    id_number = serializers.CharField(max_length=14, min_length=14, trim_whitespace=True)
    
    def validate_id_number(self, value):
        is_valid, error = validate_egyptian_id(value)
        if not is_valid:
            raise serializers.ValidationError(error)
        return value


class APIRequestLogSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = APIRequestLog
        fields = ['id', 'username', 'action', 'timestamp']
        read_only_fields = ['id', 'timestamp']
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['timestamp'] =  timesince.timesince(instance.timestamp) + " ago"
        return representation
