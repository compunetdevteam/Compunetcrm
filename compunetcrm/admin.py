from django.contrib import admin
from .models import Customer
# Register your models here.
admin.site.site_header = '    COMPUNET LIMITED CRM'
admin.site.site_title = "     COMPUNET LIMITED CRM"

admin.site.register(Customer)