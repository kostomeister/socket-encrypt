from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    brand = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"

    def __str__(self) -> str:
        return f"{self.name} - {self.color} - {self.brand}"
