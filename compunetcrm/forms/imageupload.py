from django import forms
from compunetcrm.models import UploadedImage,Customer


class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ('image', 'image_description', 'image_text_xandy_cordinate', )


class CustomerUploadForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('first_name','last_name','address','customer_type','phone_number','email')
