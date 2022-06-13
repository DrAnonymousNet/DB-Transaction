from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from django.db import transaction
from .models import Account
from .serializers import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class AccountCreateSerializer(generics.ListCreateAPIView):
    pass


class TransferAPIView(APIView):
    serializer_class = TransferSerializer
    @csrf_exempt
    def post(self, request, **kwargs):
        serializer = TransferSerializer(data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data= serializer.data, status=status.HTTP_200_OK)




