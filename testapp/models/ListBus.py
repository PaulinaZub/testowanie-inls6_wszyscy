from django.db import models

# Create your models here.
class Bus(models.Model):
    nameBus = models.CharField(max_length=255)
    content = models.TextField(default="")
    price = models.PositiveSmallIntegerField(default=1)
    year = models.PositiveSmallIntegerField(default=1800)
    imgCar = models.ImageField(upload_to='mediacar', blank=True, null=True)
    popular = models.IntegerField(default=0)
    def __str__(self):
        return self.nameBus

    def is_expensive(self):
        return self.price > 100

    def is_new(self):
        return self.year > 2016

    def is_popular(self):
        return self.popular > 1




