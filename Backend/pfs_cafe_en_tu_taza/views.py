from django.shortcuts import render

# Create your views here
from django.http import JsonResponse
from .models import Farms, Orders, Posts, Producers, Products, Users


def get_model_data(model_class, id_field, name_field, status_field):
    items = model_class.objects.using('cafe').all()
    data = [{
        id_field: getattr(item, id_field),
        name_field: getattr(item, name_field),
        status_field: getattr(item, status_field)
    } for item in items]
    return JsonResponse(data, safe=False)


def farm_list(request):
    return get_model_data(Farms, 'farms_id', 'farms_name', 'farms_status')


def order_list(request):
    return get_model_data(Orders, 'orders_id', 'orders_name', 'orders_status')


def post_list(request):
    return get_model_data(Posts, 'posts_id', 'posts_name', 'posts_status')


def producer_list(request):
    return get_model_data(Producers, 'producers_id', 'producers_name', 'producers_status')


def product_list(request):
    return get_model_data(Products, 'products_id', 'products_name', 'products_status')


def user_list(request):
    return get_model_data(Users, 'users_id', 'users_name', 'users_status')
