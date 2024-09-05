from django.db import models
from base.models.helpers.date_time_model import DateTimeModel

# Create your models here.

class MenuModel(DateTimeModel):
    flat = models.OneToOneField("canteen.FlatModel", on_delete=models.CASCADE, verbose_name="Plat ")


    def __str__(self):
        return f"{self.flat}"    

    class Meta:
        verbose_name = "Menu"
        verbose_name_plural = "Menus"