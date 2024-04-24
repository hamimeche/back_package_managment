# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from packages.models import Package
from .models import Item
from logisticians.models import LogisticianUser
from .serializers import ItemSerializer


class GetItemsFromPackage(generics.ListAPIView):

    serializer_class = ItemSerializer

    def get(self, request, package_code):

        user = request.user
        logistician_user = LogisticianUser.objects.get(user=user)
        package = Package.objects.filter(
            code=package_code, logistician_id=logistician_user.logistician_infos.id
        ).get()
        item_list = Item.objects.filter(package=package)
        serializer = ItemSerializer(item_list, many=True)

        return Response(data=serializer.data)
