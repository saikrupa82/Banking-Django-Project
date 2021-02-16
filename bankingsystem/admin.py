from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(bankcustomer)
class bankcustomerAdmin(admin.ModelAdmin):
    list_display=(
        'AccountNumber',
        'firstname',
        'Balance',
    )



@admin.register(transferdetails)
class transferdetailsAdmin(admin.ModelAdmin):
    list_display=(
        'uniqueid',
        'AmountSent',
    )

