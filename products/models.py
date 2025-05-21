from django.db import models
from django.utils import timezone
from user.models import User

# # Create your models here.

# class Product(models.Model):
#     pass
#     # Product name
#     # Content Charecteristics
#     # time_stamp
#     # edited

# from django.contrib.auth.models import User
from django.conf import settings

# Категория товара: ноутбуки, ПК, периферия и т.д.
class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    slug = models.SlugField("Слаг (для URL)", unique=True)
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name

# Продавец
class Seller(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE , verbose_name="Продавец")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shop_name = models.CharField("Название магазина", max_length=255)
    
    class Meta:
        verbose_name = "Продавец"
        verbose_name_plural = "Продавцы"

    def __str__(self):
        return self.shop_name

# Продукт
class Product(models.Model):
    name = models.CharField("Название товара", max_length=255)
    description = models.TextField("Описание", blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    vendor = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Продавец")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField("Количество на складе", default=0)
    image = models.ImageField("Изображение", upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField("Дата добавления", auto_now_add=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name
