from django.contrib import admin
from .models import Category, Paint

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # Автоматично створює slug з назви

@admin.register(Paint)
class PaintAdmin(admin.ModelAdmin):
    list_display = ['brand', 'title', 'price', 'volume', 'color_code', 'in_stock']
    list_filter = ['brand', 'category', 'in_stock']
    list_editable = ['price', 'in_stock'] 
