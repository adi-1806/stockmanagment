from django.db import models

# Create your models here.

class selled_motor(models.Model):
    company=models.CharField(max_length=50)
    model_name=models.CharField(max_length=100)
    hp=models.DecimalField(max_digits=3, decimal_places=1)
    hsncode=models.CharField(max_length=50)
    price=models.IntegerField(null=True)
    others=models.CharField(max_length=100)
    customer_name=models.CharField(max_length=100)
    customer_phno=models.IntegerField()
    customer_address=models.TextField()

    def __str__(self) :
        return f"{self.company},{self.model_name},{self.hp},{self.customer_name},{self.customer_phno},{self.customer_address}"
