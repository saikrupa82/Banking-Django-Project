from django.urls import path
from .views import *
urlpatterns=[
    path('',index,name='index'),
    path('Transfer/<slug>',transfer,name="Transfer"),
    path('ReviewOfTransfer',reviewoftransfer,name='reviewoftransfer'),
    path('Transaction',Transaction,name="Transaction"),
]