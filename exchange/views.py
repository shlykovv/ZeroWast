from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from exchange.models import ExchangeItem, Category
from exchange.serializers import ExchangeItemSerializer


class ExchangeItemViewSet(viewsets.ModelViewSet):
    queryset = ExchangeItem.objects.all()
    serializer_class = ExchangeItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


def exchange_list(request):
    items = ExchangeItem.objects.filter(is_active=True).order_by('-created_at')

    query = request.GET.get('q')
    category_id = request.GET.get('category')
    status = request.GET.get('status')

    if query:
        items = items.filter(title__icontains=query)

    if category_id:
        items = items.filter(category_id=category_id)

    if status:
        items = items.filter(status=status)

    categories = Category.objects.all()

    context = {
        'items': items,
        'categories': categories
    }
    return render(request, 'exchange_item/exchange_list.html', context)
