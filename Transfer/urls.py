from django.contrib import admin
from django.urls import path, re_path, include
from Transfer.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path("transfer/", TransferAPIView.as_view(), name="transfer"),
]