import os

import stripe
from django.http import HttpResponseRedirect
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Item

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


class ItemAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_detail.html'

    def get(self, request, pk):
        queryset = Item.objects.get(pk=pk)

        return Response({'item': queryset})


class BuyAPIView(APIView):

    def get(self, request, pk):
        session = stripe.checkout.Session.create(
            success_url='http://0.0.0.0:8000/success/',
            cancel_url='http://0.0.0.0:8000/cancel/',
            line_items=[
                {
                    'price': pk,
                    'quantity': 1,
                },
            ],
            mode='payment',
        )
        return HttpResponseRedirect(session.url)
