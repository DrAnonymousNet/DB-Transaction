from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from django.db import transaction
from .models import Account
from .serializers import *
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.versioning import NamespaceVersioning
# Create your views here.

class AccountCreateListAPIView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = Account.objects.all()



class TransferAPIView(APIView):
    serializer_class = TransferSerializer
    versioning_class = NamespaceVersioning

    @csrf_exempt
    def post(self, request, **kwargs):
        TransferSerializerChoice = self.get_serializer_class()
        serializer = TransferSerializerChoice(data= request.data, context={"request":request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data= serializer.data, status=status.HTTP_200_OK)

    def get_serializer_class(self):
        print(self.request.version)
        if self.request.version == 'v1':

            return TransferSerializer
        return TransferSerializerWithError

        




