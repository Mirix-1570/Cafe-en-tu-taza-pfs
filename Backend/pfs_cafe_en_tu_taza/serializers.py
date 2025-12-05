from .models import Farm, FarmPost, Order, OrderUser, Post, Producer, Product, ProductFarm, User, UserProduct
from rest_framework import serializers

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class FarmPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FarmPost
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderUser
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductFarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductFarm
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProduct
        fields = '__all__'

