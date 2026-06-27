from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, verbose_name="اسم القطعة")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="السعر")
    image = models.ImageField(upload_to='clothes/', verbose_name="صورة القطعة")

    def __str__(self):
        return self.name