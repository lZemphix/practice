from django.db import models

# Create your models here.
class Category(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)

class Partner(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=64)
    description = models.TextField()

class Discount(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=256)
    description = models.TextField()
    how_get = models.TextField()
    promocode = models.CharField(max_length=64, null=True, blank=True)
    validity_period = models.CharField(max_length=128)
    partner_description = models.ForeignKey(to=Partner, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='discounts_imgs')
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)

