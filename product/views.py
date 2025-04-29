from rest_framework.response import Response

from .serializers import *
from rest_framework import generics
from rest_framework.views import APIView

class GetCategories(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class GetCategory(generics.RetrieveAPIView):
    serializer_class = CategoryFullSerializer

    def get_object(self):
        cat_id = self.kwargs['pk']
        user = self.request.user

        category = Category.objects.get(id=cat_id)

        # Получаем первый товар без ProductRate от текущего пользователя
        product_without_rate = category.products.exclude(
            rates__user=user  # Здесь используется 'rates', а не 'productrate'
        ).first()

        # Прикрепляем этот товар к категории
        category.filtered_product = product_without_rate

        return category

class ProductAction(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        ProductRate.objects.create(
            product_id=request.data['id'],
        user =request.user,
        comment=request.data['comment'],
        like_it=request.data['like'],
        )
        return Response(status=200)