from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Accessory(models.Model):
    name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)
    pin_number = models.IntegerField(
        blank=True,
        null=True,
        verbose_name="GPIO pin number",
        validators=[MinValueValidator(1), MaxValueValidator(100)]
    )

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Accessories'
