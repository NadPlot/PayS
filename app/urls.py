from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('success/', TemplateView.as_view(template_name='success.html'), name='success'),
]
