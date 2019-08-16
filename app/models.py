from django.db import models

# Create your models here.
from django.utils import timezone


class BlockChain(models.Model):
    data = models.CharField(max_length=200, blank=False)
    previousHash = models.CharField(max_length=300, blank=False)
    hash = models.CharField(max_length=300, blank=False)
    timestamp = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return str(self.id)
