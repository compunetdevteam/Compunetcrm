from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Customer, SentMail, UploadedImage, ImageTextCordinate
from import_export import resources

admin.site.site_header = '    COMPUNET EMAIL SYSTEM'
admin.site.site_title = "     COMPUNET ENAIL SYSTEM"


class CustomerResource(resources.ModelResource):
    class Meta:
        model = Customer

@admin.register(Customer)
class ApplicantAdmin(ImportExportModelAdmin):
    resource_class = CustomerResource


admin.site.register(UploadedImage)
admin.site.register(SentMail)
admin.site.register(ImageTextCordinate)