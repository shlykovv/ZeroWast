from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from exchange.models import ExchangeItem, Category
from exchange.forms import ExchangeItemForm
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

    paginator = Paginator(items, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'items': items,
        'categories': categories,
        'page_obj': page_obj
    }
    return render(request, 'exchange_item/exchange_list.html', context)


def item_detail(request, pk):
    item = get_object_or_404(ExchangeItem, pk=pk)
    context = {
        'title': f'Товар - {item.title}',
        'item': item
    }
    return render(request, 'exchange_item/item_detail.html', context)


def item_create(request):
    if request.method == 'POST':
        form = ExchangeItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            item.user = request.user
            item.save()
            return redirect('exchange:item_detail', pk=item.pk)
    else:
        form = ExchangeItemForm()

    context = {
        'title': 'Добавление товара',
        'form': form
    }

    return render(request, 'exchange_item/item_create.html', context)
