from django.contrib import admin
from .models import Account, Lot, AccountLot

admin.site.register(Account)
admin.site.register(Lot)
admin.site.register(AccountLot)
