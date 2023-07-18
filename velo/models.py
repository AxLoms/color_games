from django.db import models

class ShopPhone(models.Model):
    img = models.ImageField("Картинка товар", upload_to="shop")
    description = models.CharField("Описание товара", max_length=9999999)
    title = models.CharField("Название",max_length=100)
    price = models.PositiveIntegerField("Цена")
    
# Create your models here.
