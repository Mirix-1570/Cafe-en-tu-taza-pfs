from django.shortcuts import render
from .models import Farms, FarmPost, Order, OrderUser, Post, Producer, Product, ProductFarm, User, UserProduct, Farm
from rest_framework import generics
from .serializers import FarmSerializer, FarmPostSerializer, OrderSerializer, OrderUserSerializer, PostSerializer, ProducerSerializer, ProductSerializer, ProductFarmSerializer, UserSerializer, UserProductSerializer

class FarmListCreateView(generics.ListCreateAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class FarmRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class FarmPostListCreateView(generics.ListCreateAPIView):
    queryset = FarmPost.objects.all()
    serializer_class = FarmPostSerializer

class FarmPostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FarmPost.objects.all()
    serializer_class = FarmPostSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderUserListCreateView(generics.ListCreateAPIView):
    queryset = OrderUser.objects.all()
    serializer_class = OrderUserSerializer

class OrderUserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderUser.objects.all()
    serializer_class = OrderUserSerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class ProducerListCreateView(generics.ListCreateAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProducerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductFarmListCreateView(generics.ListCreateAPIView):
    queryset = ProductFarm.objects.all()
    serializer_class = ProductFarmSerializer

class ProductFarmRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductFarm.objects.all()
    serializer_class = ProductFarmSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProductListCreateView(generics.ListCreateAPIView):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer

class UserProductRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserProduct.objects.all()
    serializer_class = UserProductSerializer