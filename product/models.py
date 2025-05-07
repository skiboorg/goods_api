from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    image = models.FileField(upload_to='image/', blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f'{self.name}'



class Product(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    description = models.TextField(blank=True, null=True, default=None)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    file = models.FileField(upload_to='images/', blank=False, null=True)

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"

class ProductRate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rates')
    user = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='rates')
    comment = models.TextField(blank=True, null=True, default=None)
    like_it = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = "Голос"
        verbose_name_plural = "Голоса"