from django_filters import rest_framework as filters
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Item
from .serializers import ItemSerializer


class ItemFilter(filters.FilterSet):
    class Meta:
        model = Item
        fields = ["package"]


class ItemViewset(
    mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet
):
    filterset_class = ItemFilter
    permission_classes = (IsAuthenticated,)
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.filter(package__logistician_id=self.request.user.id)
        return self.get_serializer_class().setup_eager_loading(queryset).order_by("-id")
