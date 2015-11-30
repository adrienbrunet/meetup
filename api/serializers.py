# coding: utf-8

from rest_framework import serializers

from .models import Beer


class BeerSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.pk')

    class Meta:
        model = Beer
        fields = ('pk', 'name', 'abv', 'comments', )
