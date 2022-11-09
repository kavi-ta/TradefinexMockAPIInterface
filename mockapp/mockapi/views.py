from django.shortcuts import render
from .serializers import PoolSerializer, ListPoolAssetSerializer
from .models import Pool , Asset
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
# Create your views here.

class GetPoolByPoolAddress(APIView):
    def get(self, request, *args, **kwargs):
        pool = Pool.objects.filter(address=self.kwargs['address'])
        serializer = PoolSerializer(pool,many=True)
        return Response(serializer.data[0])

class GetPoolAssetsByPoolAddress(APIView):
    def get(self, request, *args, **kwargs):
        assets = Asset.objects.filter(pool__address=self.kwargs['pool'])
        serializer = ListPoolAssetSerializer(assets,many=True)
        return Response( serializer.data)
