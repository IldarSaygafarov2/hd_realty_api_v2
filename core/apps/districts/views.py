from rest_framework import generics

from .models import District
from .serializers import DistrictSerializer


class DistrictAPIView(generics.ListAPIView):
    queryset = District.objects.all()
    serializer_class = DistrictSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
