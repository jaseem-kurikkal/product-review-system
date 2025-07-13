from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Product, Review
from .serializers import ProductSerializer, ReviewSerializer
from .permissions import IsAdminOrReadOnly, IsRegularUser

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]

class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsRegularUser]

    def get_queryset(self):
        return Review.objects.filter(product_id=self.kwargs['product_pk'])

    def perform_create(self, serializer):
        product_id = self.kwargs['product_pk']
        product = Product.objects.get(pk=product_id)
        serializer.save(user=self.request.user, product=product)

    def create(self, request, *args, **kwargs):
        product_id = kwargs['product_pk']
        user = request.user

        if Review.objects.filter(product_id=product_id, user=user).exists():
            return Response({"detail": "You already reviewed this product."},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)
