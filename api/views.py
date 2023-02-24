import os

import stripe
from django.http import HttpResponseRedirect
from dotenv import load_dotenv
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Item

load_dotenv()

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class ItemAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_detail.html'

    def get(self, request, pk):
        queryset = Item.objects.get(pk=pk)

        return Response({'item': queryset})


class BuyAPIView(APIView):

    def get(self, request, pk):
        queryset = Item.objects.get(pk=pk)

        product = stripe.Product.create(name=queryset.name)
        price = stripe.Price.create(
            unit_amount=queryset.price,
            currency='usd',
            product=product.id,
        )
        session = stripe.checkout.Session.create(
            success_url='http://0.0.0.0:8000/success/',
            line_items=[
                {
                    'price': price.id,
                    'quantity': 1,
                },
            ],
            mode='payment',
        )
        return HttpResponseRedirect(session.url)
