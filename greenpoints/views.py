from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from rest_framework import viewsets, permissions

from greenpoints.models import GreenPoint
from greenpoints.forms import GreenPointForm
from greenpoints.serializers import GreenPointSerializer


class GreenPointViewSet(viewsets.ModelViewSet):
    queryset = GreenPoint.objects.all()
    serializer_class = GreenPointSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class GreenPointCreateView(CreateView):
    model = GreenPoint
    form_class = GreenPointForm
    template_name = 'greenpoints/greenpoint_form.html'
    success_url = '/map/'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
