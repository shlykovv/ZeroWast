from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from exchange.models import ExchangeItem
from exchange.serializers import ExchangeItemSerializer


class ExchangeItemViewSet(viewsets.ModelViewSet):
    queryset = ExchangeItem.objects.all()
    serializer_class = ExchangeItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
