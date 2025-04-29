from django.urls import path,include
from . import views


urlpatterns = [
    path('categories', views.GetCategories.as_view()),
    path('category/<pk>', views.GetCategory.as_view()),
    path('action', views.ProductAction.as_view()),

]
