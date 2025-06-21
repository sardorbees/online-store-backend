from django.db import models

class YourModel(models.Model):
    name = models.CharField(max_length=255)

class Meta:
    verbose_name = 'Локация'
    verbose_name_plural = 'Локация'