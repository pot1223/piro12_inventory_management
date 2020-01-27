from django.db import models


class Company(models.Model):
    companyName = models.CharField(max_length=100)
    tel = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Item(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(blank=True, upload_to="image")
    info = models.TextField(blank=True, null=True)
    price = models.CharField(max_length=100)
    remaining = models.CharField(max_length=100)
    client = models.ForeignKey(Company, on_delete=models.CASCADE)

