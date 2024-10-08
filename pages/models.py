from django.db import models

# Create your models here.
class Design(models.Model):
    design_name = models.CharField(max_length=100)
    design_image = models.ImageField(upload_to="images/")
    design_price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.design_name
    
    
    
