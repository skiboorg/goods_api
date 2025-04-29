from django.contrib import admin
from .models import *

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [ProductInline]

class ProductAdmin(admin.ModelAdmin):
    model = Product
    inlines = [ImageInline]

class ProductRateAdmin(admin.ModelAdmin):
    model = ProductRate
    list_display = ('product__category__name','product__name','like_it','comment',)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRate, ProductRateAdmin)