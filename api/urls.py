from django.urls import path

from .views import BuyAPIView, ItemAPIView

urlpatterns = [
    path('item/<int:pk>/', ItemAPIView.as_view(), name='item'),
    path('buy/<int:pk>/', BuyAPIView.as_view(), name='buy'),
]
