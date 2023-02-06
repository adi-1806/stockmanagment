from django.db import models

# Create your models here.

class motor_products(models.Model):
    company=models.CharField(max_length=50)
    model_name=models.CharField(max_length=100)
    hp=models.DecimalField(max_digits=3, decimal_places=1)
    others=models.CharField(max_length=100)
    quantity=models.IntegerField()
    hsncode=models.CharField(max_length=50)
    price=models.IntegerField(null=True)
    #date=models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) :
        return f"{self.company},{self.model_name},{self.hp}"

class other_products(models.Model):
    item_name=models.CharField(max_length=50)
    quantity=models.IntegerField()
    specifications=models.CharField(max_length=50)
    hsncode=models.CharField(max_length=50)
    price=models.IntegerField(null=True)
    #date=models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self) :
        return f"{self.item_name},{self.quantity},{self.hsncode}"
