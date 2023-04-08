from django.contrib import admin

# Register your models here.
from .models import AtUser, LoanInstance, Equipment, Provider, AtCategory

admin.site.register(AtUser)
admin.site.register(LoanInstance)
admin.site.register(Equipment)
admin.site.register(Provider)
admin.site.register(AtCategory)
