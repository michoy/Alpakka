from django.db import models

# Create your models here.

class Test(models.Model):
    promille = models.DecimalField(decimal_places=3, max_digits=4)
