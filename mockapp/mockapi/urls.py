from django.urls import include, path
from rest_framework import routers
from .views import  GetPoolByPoolAddress, GetPoolAssetsByPoolAddress

urlpatterns = [
    path('get-pool-by-pool-address/<str:address>/', GetPoolByPoolAddress.as_view(), name="get-pool"),
    path('get-assets-by-pool-address/<str:pool>/', GetPoolAssetsByPoolAddress.as_view(), name='list_assets'),
]