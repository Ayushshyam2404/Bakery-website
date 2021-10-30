from django.db import models
from django.db.models.base import Model

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=40)
    email=models.CharField(max_length=100)
    def __str__(self):
        sen=f"""Name is :{self.username}, Email is :{self.email}, """
        return sen
class Items(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    def __str__(self):
        return self.price
    def __str__(self):
        return self.name
class Order(models.Model):
    name=models.CharField(max_length=100)
    item_name=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    address=models.TextField(max_length=100)
    num=models.CharField(max_length=100)
    def __str__(self):
        return f'Name is : {self.name}'

    # def __str__(self):
    #     sen=f'Order from : {self.name}, Item : {self.item_name} ,Quantity : {self.quantity}'
