from django.contrib import admin
from .models import *
from django.utils.safestring import mark_safe

class ProductInline(admin.TabularInline):
    model = Product
    extra = 0

class ImageInline(admin.TabularInline):
    model = Image
    extra = 0

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'image_preview',
        'name',

    )
    model = Category
    inlines = [ProductInline]

    readonly_fields = ['image_preview']

    def image_preview(self, obj):

        if obj.image:
            return mark_safe(
                '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(
                    obj.image.url))
        else:
            return 'Нет изображения'

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'image_preview',
        'name',
        'category__name',

    )
    model = Product
    inlines = [ImageInline]
    readonly_fields = ['image_preview']

    def image_preview(self, obj):

        if obj.images:
            return mark_safe(
                '<img src="{0}" width="150" height="150" style="object-fit:contain" />'.format(obj.images.first().file.url))
        else:
            return 'Нет изображения'

class ProductRateAdmin(admin.ModelAdmin):
    model = ProductRate
    list_display = ('product__category__name','product__name','like_it','comment','user')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductRate, ProductRateAdmin)