from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Review

class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = '__all__'
        read_only_fields = ['user', 'product']

class ProductSerializer(serializers.ModelSerializer):
    average_rating = serializers.FloatField(source='average_rating', read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'average_rating', 'reviews']
