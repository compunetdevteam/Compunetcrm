from django.contrib import admin
# from import_export.admin import ImportExportModelAdmin
from .models import Customer
# from import_export import resources
# Register your models here.
#admin.site.site_header = '    COMPUNET LIMITED CRM'
#admin.site.site_title = "     COMPUNET LIMITED CRM"


# class CustomerResource(resources.ModelResource):
#     class Meta:
#         model = Customer
#
# @admin.register(Customer)
# class ApplicantAdmin(ImportExportModelAdmin):
#     resource_class = CustomerResource

admin.site.register(Customer)