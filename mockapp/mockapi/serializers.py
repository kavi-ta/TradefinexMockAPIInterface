from rest_framework import serializers
from .models import Pool, Asset

class PoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pool
        fields =  ["current_supply","nav","tenure","issue_size","senior_apy","junior_apy","token_price","senior_tranche","junior_tranche","is_active"]     
        # fields = "__all__"

class ListPoolAssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = ["asset_address","asset_name","asset_type","financing_date","maturity_date","financing_fee","amount_invested","currency"]