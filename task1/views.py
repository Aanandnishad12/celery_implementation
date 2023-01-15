from django.shortcuts import render
from .task import add
from django.http import HttpResponse
# Create your views here.


def myhellow(request):
    delta = add.delay(3,4)
    print(delta.id)
    return HttpResponse("hello")