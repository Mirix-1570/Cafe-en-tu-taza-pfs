# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Farms(models.Model):
    farms_id = models.IntegerField(primary_key=True)
    farms_name = models.CharField(max_length=45)
    farms_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'farms'


class Orders(models.Model):
    orders_id = models.IntegerField(primary_key=True)
    orders_name = models.CharField(max_length=45)
    orders_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'orders'


class Posts(models.Model):
    posts_id = models.IntegerField(primary_key=True)
    posts_name = models.CharField(max_length=45)
    posts_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posts'


class Producers(models.Model):
    producers_id = models.IntegerField(primary_key=True)
    producers_name = models.CharField(max_length=45)
    producers_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'producers'


class Products(models.Model):
    products_id = models.IntegerField(primary_key=True)
    products_name = models.CharField(max_length=45)
    products_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Users(models.Model):
    users_id = models.IntegerField(primary_key=True)
    users_name = models.CharField(max_length=45)
    users_status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
