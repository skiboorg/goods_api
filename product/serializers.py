from rest_framework import serializers
from .models import *
from datetime import date

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'


class ProductRateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRate
        fields = '__all__'


class CategoryFullSerializer(serializers.ModelSerializer):
    filtered_product = ProductSerializer()
    total_products = serializers.SerializerMethodField()
    rated_products = serializers.SerializerMethodField()
    unrated_percentage = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ('id', 'name', 'image', 'filtered_product','total_products',
'rated_products',
'unrated_percentage',)



    def get_total_products(self, obj):
        return obj.products.count()

    def get_rated_products(self, obj):
        user = self.context['request'].user
        return obj.products.filter(rates__user=user).distinct().count()

    def get_unrated_percentage(self, obj):
        total = self.get_total_products(obj)
        rated = self.get_rated_products(obj)
        if total == 0:
            return 0
        return round((rated / total) * 100, 2)



class CategorySerializer(serializers.ModelSerializer):
    # products = serializers.SerializerMethodField()
    total_products = serializers.SerializerMethodField()
    rated_products = serializers.SerializerMethodField()
    unrated_percentage = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'image', 'total_products', 'rated_products', 'unrated_percentage']


    def get_total_products(self, obj):
        return obj.products.count()

    def get_rated_products(self, obj):
        user = self.context['request'].user
        return obj.products.filter(rates__user=user).distinct().count()

    def get_unrated_percentage(self, obj):
        total = self.get_total_products(obj)
        rated = self.get_rated_products(obj)
        if total == 0:
            return 0
        return round((rated / total) * 100, 2)

