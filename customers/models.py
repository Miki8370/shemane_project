from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CustomerProfile(models.Model):
    GenderChoice =  (
    ("M", "MAN"),
    ("W", "WOMEN"),
    )

    customer = models.OneToOneField(User, on_delete=models.CASCADE)
    customer_gender = models.CharField(max_length=1, choices=GenderChoice)
    customer_email = models.EmailField(unique=True)
    customer_phone = models.CharField(max_length=12)
    customer_address = models.TextField()
    customer_profile_picture = models.ImageField(blank=False)

    def __str__(self):
        return self.customer_email
        