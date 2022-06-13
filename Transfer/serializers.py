
from rest_framework import serializers
from .models import *
from django.db import transaction
from rest_framework.exceptions import APIException

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = "__all__"

class TransferSerializer(serializers.Serializer):
    from_account = serializers.IntegerField()
    to_account = serializers.IntegerField()
    amount = serializers.FloatField()

    
    def save(self):
        print("Hello World")
        try:
            with transaction.atomic():
                from_account = Account.objects.get(account_num = self.validated_data.get("from_account"))
                amount = self.validated_data.get("amount")
                #The LOGIC here was INTENTIONAL
                if from_account.get_balance() >= amount:
                    from_account.balance -= amount
                    print("Hello")
                    from_account.save()

                #Intentionally queried the for account here
                print(self.validated_data.get("to_account"))
                to_account = Account.objects.get(account_num=self.validated_data.get("to_account"))
                to_account.balance += amount
                to_account.save()
        except Exception as e:
            raise APIException(e)
        validated_data = {}
        

class TransferSerializerWithError(serializers.Serializer):
    from_account = serializers.IntegerField()
    to_account = serializers.IntegerField()
    amount = serializers.FloatField()


    def save(self):
        print("Eror")

        from_account = Account.objects.get(account_num=self.validated_data.get("from_account"))
        amount = self.validated_data.get("amount")
        #The LOGIC here was INTENTIONAL
        try:
            if from_account.balance >= amount:
                from_account.balance -= amount
                print("Hello")
                from_account.save()

            #Intentionally queried the to account here

            to_account = Account.objects.get(account_num=self.validated_data.get("to_account"))
            to_account.balance += amount
            to_account.save()
        except Exception as e:
            raise APIException(e)

        

