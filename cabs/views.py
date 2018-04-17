from django.shortcuts import render
from rest_framework import routers, serializers, viewsets
from cabs.serializers import CabSerializer
from cabs.models import Cab


class CabViewSet(viewsets.ModelViewSet):
    queryset = Cab.objects.all()
    serializer_class = CabSerializer