from django.db import models

class Farms(models.Model):
    pk = models.CompositePrimaryKey('id_finca', 'producers_id_producers')
    id_finca = models.IntegerField()
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    ubicacion = models.CharField(db_column='Ubicacion', unique=True, max_length=20)  # Field name made lowercase.
    extension = models.IntegerField(db_column='Extension')  # Field name made lowercase.
    producers_id_producers = models.ForeignKey('Producers', models.DO_NOTHING, db_column='producers_id_producers')

    def __str__(self):
        return str(self.nombre)

class FarmsHasPosts(models.Model):
    pk = models.CompositePrimaryKey('farms_id_finca', 'farms_producers_id_producers', 'posts_id_posts')
    farms_id_finca = models.ForeignKey(Farms, models.DO_NOTHING, db_column='farms_id_finca')
    farms_producers_id_producers = models.ForeignKey(Farms, models.DO_NOTHING, db_column='farms_producers_id_producers', to_field='producers_id_producers', related_name='farmshasposts_farms_producers_id_producers_set')
    posts_id_posts = models.ForeignKey('Posts', models.DO_NOTHING, db_column='posts_id_posts')

    def __str__(self):
        return str(self.farms_producers_id_producers)

class Orders(models.Model):
    id_orders = models.AutoField(primary_key=True)
    emisor = models.CharField(db_column='Emisor', unique=True, max_length=45)  # Field name made lowercase.
    receptor = models.CharField(db_column='Receptor', unique=True, max_length=45)  # Field name made lowercase.
    numero_de_factura = models.IntegerField(db_column='Numero de Factura', unique=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    fecha = models.DateField(db_column='Fecha')  # Field name made lowercase.
    forma_de_pago = models.CharField(db_column='Forma de Pago', max_length=30)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descripcion = models.CharField(db_column='Descripcion', max_length=30)  # Field name made lowercase.
    cantidad = models.IntegerField(db_column='Cantidad')  # Field name made lowercase.
    precio_unitario = models.IntegerField(db_column='Precio unitario')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    importe_total = models.IntegerField(db_column='Importe total')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    descuentos = models.CharField(db_column='Descuentos', max_length=5, blank=True, null=True)  # Field name made lowercase.
    impuestos = models.IntegerField(db_column='Impuestos')  # Field name made lowercase.
    cantidad_adeudada = models.IntegerField(db_column='Cantidad adeudada')  # Field name made lowercase. Field renamed to remove unsuitable characters.
    condiciones_de_pago = models.CharField(db_column='Condiciones de pago', max_length=200)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    def __str__(self):
        return str(self.emisor)

class OrdersHasUsers(models.Model):
    pk = models.CompositePrimaryKey('orders_id_orders', 'users_users_id')
    orders_id_orders = models.ForeignKey(Orders, models.DO_NOTHING, db_column='orders_id_orders')
    users_users = models.ForeignKey('Users', models.DO_NOTHING)

    def __str__(self):
        return str(self.orders_id_orders)

class Posts(models.Model):
    id_posts = models.AutoField(primary_key=True)
    titulo = models.CharField(db_column='Titulo', max_length=200)  # Field name made lowercase.
    texto = models.CharField(db_column='Texto', max_length=2000)  # Field name made lowercase.

    def __str__(self):
        return str(self.titulo)

class Producers(models.Model):
    id_producers = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', unique=True)  # Field name made lowercase.
    cedula = models.IntegerField(db_column='Cedula', unique=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.nombre)

class Products(models.Model):
    pk = models.CompositePrimaryKey('id_products', 'orders_id_orders')
    id_products = models.AutoField()
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    categoria = models.CharField(db_column='Categoria', max_length=30)  # Field name made lowercase.
    precio = models.IntegerField(db_column='Precio')  # Field name made lowercase.
    inventario = models.IntegerField(db_column='Inventario')  # Field name made lowercase.
    orders_id_orders = models.ForeignKey(Orders, models.DO_NOTHING, db_column='orders_id_orders')

    def __str__(self):
        return str(self.nombre)

class ProductsHasFarms(models.Model):
    pk = models.CompositePrimaryKey('products_id_products', 'products_orders_id_orders', 'farms_id_finca', 'farms_producers_id_producers')
    products_id_products = models.ForeignKey(Products, models.DO_NOTHING, db_column='products_id_products')
    products_orders_id_orders = models.ForeignKey(Products, models.DO_NOTHING, db_column='products_orders_id_orders', to_field='orders_id_orders', related_name='productshasfarms_products_orders_id_orders_set')
    farms_id_finca = models.ForeignKey(Farms, models.DO_NOTHING, db_column='farms_id_finca')
    farms_producers_id_producers = models.ForeignKey(Farms, models.DO_NOTHING, db_column='farms_producers_id_producers', to_field='producers_id_producers', related_name='productshasfarms_farms_producers_id_producers_set')

    def __str__(self):
        return str(self.products_id_products)

class Users(models.Model):
    users_id = models.AutoField(primary_key=True)
    nombre = models.CharField(db_column='Nombre', max_length=45)  # Field name made lowercase.
    correo = models.CharField(db_column='Correo', unique=True, max_length=50)  # Field name made lowercase.
    telefono = models.IntegerField(db_column='Telefono', unique=True)  # Field name made lowercase.
    cedula = models.IntegerField(db_column='Cedula', unique=True)  # Field name made lowercase.

    def __str__(self):
        return str(self.nombre)

class UsersHasProducts(models.Model):
    pk = models.CompositePrimaryKey('users_users_id', 'products_products_id')
    users_users = models.ForeignKey(Users, models.DO_NOTHING)
    products_products = models.ForeignKey(Products, models.DO_NOTHING)

    def __str__(self):
        return str(self.users_users)