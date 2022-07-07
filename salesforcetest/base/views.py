
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from .models import *
from .serializer import *  # NOQA   
# Create your views here.


def home(request):

    return HttpResponse("Hello the server is working and running")


@api_view(['GET'])
def order (request): 


    orders =Opportunity.objects.all()
    serializer = OppSerializer(orders,  many=True)
    return Response(serializer.data)











@api_view(['GET'])
def user(request):


    orders =User.objects.all()
    serializer = UserSerializer(orders,  many=True)
    return Response(serializer.data)




@api_view(['GET'])

def account(request):   
    orders =Account.objects.all()
    serializer = AccSerializer(orders,  many=True)
    return Response(serializer.data)