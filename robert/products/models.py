from django.db import models

class Product(models.Model):
    code=models.IntegerField()
    name=models.CharField(max_length=20)
    price=models.FloatField()
    stock=models.IntegerField()
    image_url=models.CharField(max_length=2083)


