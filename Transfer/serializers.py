from dataclasses import fields
from rest_framework import serializers
from .models import *
from django.db import transaction

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class TransferSerializer(serializers.Serializer):
    from_account = serializers.IntegerField()
    to_account = serializers.IntegerField()
    amount = serializers.FloatField()


    def create(self, validated_data):
        
        with transaction.atomic():
            from_account = Account.objects.get(validated_data.pop("from_account"))
            amount = validated_data.get("amount")
            #The LOGIC here was INTENTIONAL
            if from_account.balance >= amount:
                from_account.balance -= amount
                from_account.save()

            #Intentionally queried the to account here

            to_account = Account.objects.get(validated_data.pop("to_account"))
            to_account.balance += amount
            to_account.save()
        return super().create(validated_data)

