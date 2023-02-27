from django.urls import path

from .views import BuyAPIView, ItemAPIView

urlpatterns = [
    path('item/<str:pk>/', ItemAPIView.as_view(), name='item'),
    path('buy/<str:pk>/', BuyAPIView.as_view(), name='buy'),
]
