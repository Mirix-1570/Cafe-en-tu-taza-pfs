"""
URL configuration for cafe_en_tu_taza_pfs project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from pfs_cafe_en_tu_taza.views import farm_list, order_list, post_list, producer_list, product_list, user_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('farms/', farm_list, name='farm-list'),
    path('orders/', order_list, name='order-list'),
    path('posts/', post_list, name='post-list'),
    path('producers/', producer_list, name='producer-list'),
    path('products/', product_list, name='product-list'),
    path('users/', user_list, name='user-list'),
]
