# coding: utf-8

from rest_framework import serializers

from .models import Beer


class BeerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Beer
        fields = ('pk', 'name', 'abv', 'comments', )
