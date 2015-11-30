# coding: utf-8

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'beers', views.BeerViewSet, base_name='beer')

urlpatterns = [
    url(r'^', include(router.urls))
]
