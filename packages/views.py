# Create your views here.

from rest_framework import generics
from rest_framework.response import Response
from .models import Package
from items.models import Item
from logisticians.models import LogisticianUser
from .serializers import PackageSerializer, ItemSerializer


class ListPackage(generics.ListAPIView):

    serializer_class = PackageSerializer

    def list(self, request):

        user = request.user
        logistician_user = LogisticianUser.objects.get(user=user)
        package_list = Package.objects.filter(
            logistician_id=logistician_user.logistician_infos.id
        )
        serializer = PackageSerializer(package_list, many=True)

        return Response(data=serializer.data)


class GetPackage(generics.RetrieveAPIView):

    serializer_class = PackageSerializer

    def get(self, request, package_code):

        user = request.user
        logistician_user = LogisticianUser.objects.get(user=user)
        package_list = Package.objects.filter(
            code=package_code, logistician_id=logistician_user.logistician_infos.id
        )
        serializer = PackageSerializer(package_list, many=True)

        return Response(data=serializer.data)
