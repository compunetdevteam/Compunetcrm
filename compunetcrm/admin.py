from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Customer, SentMail, UploadedImage, ImageTextCordinate, SentSms
from import_export import resources
from django.contrib.auth.models import Permission

admin.site.site_header = '     EMAIL SYSTEM'
admin.site.site_title = "      EMAIL SYSTEM"


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer

@admin.register(Customer)
class ApplicantAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource

admin.site.register(Permission)
admin.site.register(UploadedImage)
admin.site.register(SentMail)
admin.site.register(ImageTextCordinate)
admin.site.register(SentSms)