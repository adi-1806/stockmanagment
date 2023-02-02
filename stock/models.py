from django.db import models

# Create your models here.

class motor_products(models.Model):
    company=models.CharField(max_length=50)
    model_name=models.CharField(max_length=100)
    hp=models.IntegerField()
    others=models.CharField(max_length=100)
    quantity=models.IntegerField()
    hsncode=models.CharField(max_length=50)

class other_products(models.Model):
    item_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    specifications=models.CharField(max_length=50)
    hsncode=models.CharField(max_length=50)