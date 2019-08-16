from django.shortcuts import render, HttpResponse
from django.utils import timezone

from .models import *
import hashlib

# Create your views here.


def home(request):
    data = BlockChain.objects.all()
    return render(request, 'app_home/home.html', {'data': data})


def create_block(request):
    data = request.POST['data']
    timestamp = timezone.now()
    previous_block = BlockChain.objects.latest('id')
    previousHash = previous_block.hash
    stri = str(data) + str(timestamp)
    encrypt = hashlib.sha256(stri.encode())
    hash = encrypt.hexdigest()
    e = BlockChain.objects.create(data=data, timestamp=timestamp, previousHash=previousHash, hash=hash)
    e.save()
    return HttpResponse("created " + str(data))


def hack_block(request):
    e = BlockChain.objects.get(id=request.POST['id'])
    data = request.POST['data']
    timestamp = timezone.now()
    stri = str(data) + str(timestamp)
    encrypt = hashlib.sha256(stri.encode())
    hash = encrypt.hexdigest()
    if hash == e.hash and BlockChain.objects.latest('id').hash == e.previousHash:
        return HttpResponse("Non Hacking attempt")
    else:
        return HttpResponse("HACKING ATTEMPT - chain broken")
