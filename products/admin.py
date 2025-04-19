from django.contrib import admin

# Register your models here.

from .models import Category, Vendor, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'vendor', 'price', 'stock', 'created_at')  # колонки в списке
    list_filter = ('category', 'vendor', 'created_at')  # фильтры справа
    search_fields = ('name', 'description')  # поиск по названию и описанию
    ordering = ('-created_at',)  # сортировка по умолчанию (сначала новые)
    list_editable = ('price', 'stock')  # поля, которые можно редактировать прямо из списка
    date_hierarchy = 'created_at'  # фильтрация по датам

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {"slug": ("name",)}  # автогенерация слага

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = ('shop_name', 'user')
    search_fields = ('shop_name', 'user__username')