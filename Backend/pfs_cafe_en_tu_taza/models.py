from django.db import models
from django.contrib.auth.models import User

class Producer(models.Model):
    nombre = models.CharField(max_length=45)
    telefono = models.IntegerField(unique=True)
    cedula = models.IntegerField(unique=True)
    def __str__(self):
        return self.nombre

class Farm(models.Model):
    nombre = models.CharField(max_length=45)
    ubicacion = models.CharField(max_length=20, unique=True)
    extension = models.IntegerField()
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    texto = models.CharField(max_length=2000)
    def __str__(self):
        return self.titulo

class FarmPost(models.Model):
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.farm} - {self.post}"

class Order(models.Model):
    emisor = models.CharField(max_length=45)
    receptor = models.CharField(max_length=45)
    numero_de_factura = models.IntegerField(unique=True)
    fecha = models.DateField()
    forma_de_pago = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=30)
    cantidad = models.IntegerField()
    precio_unitario = models.IntegerField()
    importe_total = models.IntegerField()
    descuentos = models.CharField(max_length=5, blank=True, null=True)
    impuestos = models.IntegerField()
    cantidad_adeudada = models.IntegerField()
    condiciones_de_pago = models.CharField(max_length=200)
    def __str__(self):
        return f"Factura #{self.numero_de_factura} - {self.emisor}"

class OrderUser(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.order} - {self.user}"

class Product(models.Model):
    nombre = models.CharField(max_length=45)
    categoria = models.CharField(max_length=30)
    precio = models.IntegerField()
    inventario = models.IntegerField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre

class ProductFarm(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    farm = models.ForeignKey(Farm, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product} - {self.farm}"

class UserProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.user} - {self.product}"