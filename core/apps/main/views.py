from rest_framework import generics

from . import models, serializers


class FAQListVIew(generics.ListAPIView):
    queryset = models.FAQ.objects.all()
    serializer_class = serializers.FAQSerialzer
