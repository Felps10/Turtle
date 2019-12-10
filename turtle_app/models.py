from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Product(models.Model):
    CATEGORY_CHOICES = [
        ('Cars', 'Cars'),
        ('Clothes', 'Clothes'),
        ('Eletronics', 'Eletronics'),
        ('Services', 'Services'),
        ('Other', 'Other'),
    ]
    name = models.CharField(max_length=100)
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='Other',
    )
    description = models.CharField(max_length=400)
    photo = models.ImageField(upload_to='turtle_app/static/uploads/')
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="products")
    buyers = [""]

    def __str__(self):
        return self.name


class Purchase(models.Model):
    buyer = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='purchases')
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name='purchases')
