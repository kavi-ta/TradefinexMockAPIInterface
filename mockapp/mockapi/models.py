from django.db import models

# Create your models here.
from django.db import models

# Create your models here.

from django.db import models
import uuid

class Pool(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    name = models.CharField(max_length = 258, null=True , unique =True)
    address = models.CharField(max_length = 1000)
    current_supply = models.IntegerField(null=True)
    nav = models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True )
    tenure = models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True)
    issue_size = models.BigIntegerField(null=True)
    senior_apy = models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True)
    junior_apy = models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True)
    token_price = models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True)
    senior_tranche = models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True)
    junior_tranche =  models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True)
    is_active = models.BooleanField(null= True , default= True)
    reward_rate = models.DecimalField(max_digits=25, decimal_places=4, default=0.00, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add =True)
    def __str__(self):
        return f"{self.name}"
        
class Asset(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable=False)
    pool = models.ForeignKey(
        Pool, on_delete=models.PROTECT, null=False, related_name="pool")
    asset_address = models.CharField(max_length = 50, blank=True,default= None, null= True)
    asset_name= models.CharField(max_length = 50, null = False)
    asset_type = models.CharField(max_length = 50, null=False)
    financing_date = models.DateField(null=False)
    maturity_date = models.DateField(null=False)
    financing_fee = models.DecimalField(max_digits=25, decimal_places = 4, default=0.00, null=True, blank=True)
    amount_invested = models.BigIntegerField(null=False , default = 0)
    currency = models.CharField(max_length = 50, null=True)
    last_updated = models.DateTimeField(auto_now_add = True)
    
    def __str__(self):
        return f"{self.asset_name} {self.pool}"

    class Meta:
        verbose_name = "Pool-Asset Map"
        verbose_name_plural = "Pool-Asset Maps"
        unique_together = ('pool', 'asset_name',)
    

