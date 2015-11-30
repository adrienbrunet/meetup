from django.db import models


class Beer(models.Model):
	name = models.CharField(max_length=255)
	abv = models.PositiveIntegerField(default=0)
	comments = models.TextField(blank=True)