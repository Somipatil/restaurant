from django.db import models

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_details = models.TextField()
    price = models.IntegerField()
    active = models.IntegerField(default='1')

    def __str__(self):
        return self.product_name

class Order(models.Model):
    name = models.CharField(max_length=20)
    phone = models.CharField(max_length = 15)
    address = models.TextField()
    delivery_date = models.DateField(blank = True)
    product_id = models.ForeignKey(Product)
    payment_option = models.CharField(max_length=50)
    order_status = models.CharField(max_length=50)
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
