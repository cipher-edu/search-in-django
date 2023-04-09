from django.db import models

# Create your models here.
class Worker(models.Model):
    name = models.CharField(max_length=150, verbose_name='Ishchi nomi')
    def __str__(self):
        return self.name
    
class Brand(models.Model):
    brand_name = models.CharField(max_length=150, verbose_name='Tovars brandi')
    def __str__(self):
        return self.brand_name
    
class Stock(models.Model):
    name = models.CharField(max_length=150)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name='Tovar brandi')
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Qabul qilivchi")
    price = models.IntegerField()

    def __str__(self):
        return self.name