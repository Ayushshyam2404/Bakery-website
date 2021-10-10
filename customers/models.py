from django.db import models


class Customer(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    email=models.EmailField()

    def __str__(self):
        sen=f'Name is : {self.name}, Password is : {self.password}'
        return sen

