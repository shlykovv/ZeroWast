from rest_framework import viewsets, permissions

from greenpoints.models import GreenPoint
from greenpoints.serializers import GreenPointSerializer


class GreenPointViewSet(viewsets.ModelViewSet):
    queryset = GreenPoint.objects.all()
    serializer_class = GreenPointSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
