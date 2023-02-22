from rest_framework.views import APIView
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from app.models import Item
from api.serializers import ItemSerializer


class ItemAPIView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'item_detail.html'

    def get(self, request, pk):
        queryset = Item.objects.get()

        return Response({'item': queryset})


class BuyAPIView(APIView):
    pass
