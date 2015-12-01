from django.core.validators import MaxValueValidator
from django.db import models


class Beer(models.Model):
    name = models.CharField(max_length=255)
    abv = models.PositiveIntegerField(default=0, validators=[MaxValueValidator(20)])
    comments = models.TextField(blank=True)

    def __str__(self):
        return self.name
