from django.contrib import admin

# Register your models here.
from .models import AtUser, Loan, Equipment, Provider, AtCategory

admin.site.register(AtUser)
admin.site.register(Loan)
admin.site.register(Equipment)
admin.site.register(Provider)
admin.site.register(AtCategory)
