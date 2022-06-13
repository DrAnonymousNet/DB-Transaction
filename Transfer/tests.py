import json
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from Transfer.models import Account
from Transfer.serializers import AccountSerializer

# Create your tests here.


class CreateNewAccountTest(APITestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.valid_payload = {
            'account_num': 2209871478,
            'balance': 33000.0
        }

        self.valid_payload_2 = {
            'account_num': 22098714768,
            'balance': 30000.0
        }

        

    def test_create_valid_account(self):
        response = self.client.post(
            reverse('account-create-list'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        response = self.client.post(
            reverse('account-create-list'),
            data=json.dumps(self.valid_payload_2),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        

 
class GetAllAccount(APITestCase):
    """ Test module for GET all Task API """

    def setUp(self):
        Account.objects.create(account_num=2209871478, balance=30000.0)
        Account.objects.create(account_num= 2209232313, balance =1200.0)

    def test_get_all_account(self):
        # get API response
        response = self.client.get(reverse('account-create-list'))
        # get data from db
        acc = Account.objects.all()
        serializer = AccountSerializer(acc, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)



class TransferSuccessTest(APITestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.acc_1 = Account.objects.create(account_num=2209871478, balance=30000.0)
        self.acc_2 = Account.objects.create(account_num= 2209232313, balance =1200.0)

        self.valid_payload = {
            "from_account":2209871478,
            "to_account":2209232313,
            "amount":2000.0
        }
        self.in_valid_payload = {
            "from_account":2209871478,
            "to_account":2209232313,
            "amount":2000.0
        }

        

    def test_transfer_account(self):
        response = self.client.post(
            reverse('v1:transfer'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.acc_1.refresh_from_db()
        self.acc_2.refresh_from_db()
        self.assertEqual(self.acc_1.get_balance(), 28000.0)
        self.assertEqual(self.acc_2.get_balance(), 3200.0)


    def test_transfer_accountE(self):
        response = self.client.post(
            reverse('v2:transfer'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.acc_1.refresh_from_db()
        self.acc_2.refresh_from_db()
        self.assertEqual(self.acc_1.get_balance(), 28000.0)
        self.assertEqual(self.acc_2.get_balance(), 3200.0)



class TestTransferFail(APITestCase):
    """ Test module for inserting a new puppy """

    def setUp(self):
        self.acc_1 = Account.objects.create(account_num=2209871478, balance=30000.0)
        self.acc_2 = Account.objects.create(account_num= 2209232313, balance =1200.0)

      
        self.in_valid_payload = {
            "from_account":2209871478,
            "to_account":22092323134,
            "amount":2000.0
        }

        

    def test_transfer_account(self):
        response = self.client.post(
            reverse('v1:transfer'),
            data=json.dumps(self.in_valid_payload),
            content_type='application/json'
        )
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.acc_1.refresh_from_db()
        self.acc_2.refresh_from_db()
        self.assertEqual(self.acc_1.get_balance(), 30000.0)
        self.assertEqual(self.acc_2.get_balance(), 1200.0)


    def test_transfer_accountE(self):
        response = self.client.post(
            reverse('v2:transfer'),
            data=json.dumps(self.in_valid_payload),
            content_type='application/json'
        )
        print(response.data)

        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

        self.acc_1.refresh_from_db()
        self.acc_2.refresh_from_db()
        self.assertEqual(self.acc_1.get_balance(), 28000.0)
        self.assertEqual(self.acc_2.get_balance(), 1200.0)