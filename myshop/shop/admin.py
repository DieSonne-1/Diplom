"""
Регестрируем класс для возможности управления моделями на странице администитора
Настраиваем поля в классе для отображения в админ панели
Прописываем атрибут с теми полями , которые можно редактировать
"""

from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image']
    list_editable = ['price']


admin.site.register(Product, ProductAdmin)
