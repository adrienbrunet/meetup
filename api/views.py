# coding: utf-8

from rest_framework import viewsets

from .serializers import BeerSerializer


class BeerViewSet(viewsets.ModelViewSet):
    serializer_class = BeerSerializer
