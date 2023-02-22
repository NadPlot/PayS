from django.urls import path
from .views import ItemAPIView, BuyAPIView


urlpatterns = [
    path('item/<int:pk>/', ItemAPIView.as_view()),
    path('buy/<int:pk>/', BuyAPIView.as_view()),
]
