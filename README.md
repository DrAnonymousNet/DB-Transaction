# DB-Transaction

This is a github repository where implemented a simple API to demostrate the use of Database Transaction

I implemented 2 serializers to handle the cash transfer view. Using URL based versioning, I can pick in between the two serializers.

In one of the serializers, I enabled Atomic Transaction to ensure that whenever there is an error, The state of the database is not affected.
In the other serializer, No Atomic transaction is enable. Any error generated during the read-write operation of the database, will affect the state of the database.

## Installation

1. Clone the Repository

2. Ceate a virtual environment:

```
$ python3 -m venv venv
```

3. Activate Virtual Environment
```
$ source venv/bin/activate
```

4. Install the Required Packages

```
$ pip install -r requirements.txt
```

5. Change directory into the `DB-Transaction/TransactionAPI`

6. Run `python manage.py makemigrations` and then `python manage.py migrate` 

7. Run the development server

```
$ python manage.py runserver
```

## Test

> python manage.py test


## ENDPOINTS

`Method`                  `URL`                   `DESCRIPTION`
  
`GET`                   `accounts/`               `List all available accounts`

`POST`                  `accounts/`               `Create new account`

`POST`               `v1/accounts/transfer/`      `Transfer Money (Database Transaction Enabled)`

`POST`                `v2/accounts/transfer/`     `Transfer Money (Database Transaction NOT Enabled)`


