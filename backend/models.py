from django.db import models
from django.utils import timezone
from cloudinary.models import CloudinaryField


# Create your models here.

class Task(models.Model):
     task_type = models.CharField(max_length=50)
     description = models.TextField()
     slug = models.SlugField(max_length=200, unique=True)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at =  models.DateTimeField(auto_now=True)

     def __str__(self):
          return self.description


class Catalogue(models.Model):
     name = models.CharField(max_length=50, null=True)
     photo = CloudinaryField()
     slug = models.SlugField(max_length=200, unique=True)

     class Meta:
          ordering = ('name', )
          verbose_name = 'catalogue'
          verbose_name_plural = 'catalogues'

          def __str__(self):
               return self.name



class Product(models.Model):
#     vendor = models.ForeignKey(
#         User, on_delete=models.CASCADE, related_name='vendor')
    name = models.CharField(max_length=200)
    photo = CloudinaryField(default=timezone.now)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    slug = models.SlugField(max_length=200, unique=True)
    stock = models.IntegerField(default=0)
    details = models.TextField()
    mfg = models.DateTimeField('date manufactured', default=timezone.now)
#     catalogue = models.ForeignKey(
#         Catalogue, on_delete=models.CASCADE, related_name='products')

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name