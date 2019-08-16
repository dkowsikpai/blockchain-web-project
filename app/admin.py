from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(BlockChain)
class BlockChainList(admin.ModelAdmin):
    list_display = ['id', 'data', 'timestamp', 'previousHash', 'hash']
