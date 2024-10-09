from django.db import models

# Create your models here.

class Customer(models.Model):
    GENDER_CHIOCE = (
    ("M", "MAN"),
    ("W", "WOMEN"),
    )
    customer_name = models.CharField(max_length=100)
    customer_gender = models.CharField(max_length=1, choices=GENDER_CHIOCE)
    #customer_order = 


class Design(models.Model):
    design_name = models.CharField(max_length=100)
    design_image = models.ImageField(blank=False)
    design_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.design_name
    

    
