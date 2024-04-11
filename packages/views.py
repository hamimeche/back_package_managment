from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Package
from .serializers import PackageFullSerializer, PackageShortSerializer


class PackageViewset(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = (IsAuthenticated,)
    lookup_field = "code"

    def get_serializer_class(self):
        if self.action == "list":
            return PackageShortSerializer
        else:
            return PackageFullSerializer

    def get_queryset(self):
        queryset = Package.objects.filter(logistician_id=self.request.user.id)
        return self.get_serializer_class().setup_eager_loading(queryset).order_by("-id")
