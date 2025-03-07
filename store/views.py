from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from . import models
from . import serializers

class ProductView(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer