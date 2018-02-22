from django import forms

from compunetcrm.models import Customer


class CustomerUploadForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'address', 'customer_type', 'phone_number', 'email')
