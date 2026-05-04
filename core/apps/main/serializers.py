from rest_framework import serializers
from . import models


class FAQSerialzer(serializers.ModelSerializer):
    class Meta:
        model = models.FAQ
        fields = ["id", "question", "answer", "created_at", "updated_at"]


class CreationConsultingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultingRequest
        fields = ["name", "phone_number", "goal"]


class ConsultingRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ConsultingRequest
        fields = ["id", "name", "phone_number", "created_at", "updated_at"]
