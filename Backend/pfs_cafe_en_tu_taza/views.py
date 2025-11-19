from django.shortcuts import render

# Create your views here. 
from django.http import JsonResponse
from .models import Farms, Orders, Posts, Producers, Products, Users

def farm_list(request):
    farms_manager = getattr(Farms, 'objects', None)
    if farms_manager is None:
        farms_manager = getattr(Farms, '_default_manager')
    farms = farms_manager.using('cafe').all()
    data = [{'farms_id': farm.farms_id, 'farms_name': farm.farms_name, 'farms_status': farm.farms_status} for farm in farms]
    return JsonResponse(data, safe=False)

def order_list(request):
    orders_manager = getattr(Orders, 'objects', None)
    if orders_manager is None:
        orders_manager = getattr(Orders, '_default_manager')
    orders = orders_manager.using('cafe').all()
    data = [{'orders_id': order.orders_id, 'orders_name': order.orders_name, 'orders_status': order.orders_status} for order in orders]
    return JsonResponse(data, safe=False)

def post_list(request):
    posts_manager = getattr(Posts, 'objects', None)
    if posts_manager is None:
        posts_manager = getattr(Posts, '_default_manager')
    posts = posts_manager.using('cafe').all()
    data = [{'posts_id': post.posts_id, 'posts_name': post.posts_name, 'posts_status': post.posts_status} for post in posts]
    return JsonResponse(data, safe=False)

def producer_list(request):
    producers_manager = getattr(Producers, 'objects', None)
    if producers_manager is None:
        producers_manager = getattr(Producers, '_default_manager')
    producers = producers_manager.using('cafe').all()
    data = [{'producers_id': producer.producers_id, 'producers_name': producer.producers_name, 'producers_status': producer.producers_status} for producer in producers]
    return JsonResponse(data, safe=False)

def product_list(request):
    products_manager = getattr(Products, 'objects', None)
    if products_manager is None:
        products_manager = getattr(Products, '_default_manager')
    products = products_manager.using('cafe').all()
    data = [{'products_id': product.products_id, 'products_name': product.products_name, 'products_status': product.products_status} for product in products]
    return JsonResponse(data, safe=False)

def user_list(request):
    users_manager = getattr(Users, 'objects', None)
    if users_manager is None:
        users_manager = getattr(Users, '_default_manager')
    users = users_manager.using('cafe').all()
    data = [{'users_id': user.users_id, 'users_name': user.users_name, 'users_status': user.users_status} for user in users]
    return JsonResponse(data, safe=False)
