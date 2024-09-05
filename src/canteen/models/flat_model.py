from django.db import models
from base.models.helpers.named_date_time_model import NamedDateTimeModel

# Create your models here.

class FlatModel(NamedDateTimeModel):
    summary = models.CharField(max_length=100, verbose_name="Description ")


    def __str__(self):
        return f"{self.name}"    

    class Meta:
        verbose_name = "Plat"
        verbose_name_plural = "Plats"