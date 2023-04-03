from django.contrib import admin

# Register your models here.
from .models import User, Loan, Equipment, Provider, AtCategory

admin.site.register(User)
admin.site.register(Loan)
admin.site.register(Equipment)
admin.site.register(Provider)
admin.site.register(AtCategory)
