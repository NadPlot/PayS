import os

import stripe

from django.db import models

stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


class Item(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=250)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        product = stripe.Product.create(name=self.name)
        price = stripe.Price.create(
            unit_amount=self.price,
            currency='usd',
            product=product.id,
        )
        self.id = price.id
        super(Item, self).save(*args, **kwargs)
