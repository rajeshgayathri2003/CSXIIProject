from django.contrib import admin
from vaccines.models import Vaccines, Availability, Vaccines_payment

# Register your models here.

admin.site.register(Vaccines)
admin.site.register(Availability)
admin.site.register(Vaccines_payment)