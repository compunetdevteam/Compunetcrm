from django import forms
from compunetcrm.models import UploadedImage,Customer


class ComposeEmailForm(forms.Form):
    to_email = forms.CharField(max_length=200)
    from_mail = forms.CharField(max_length=300)
    subject = forms.Charfield(max_length=200)
    body = forms.CharField(max_length=800)
    image_name = forms.ModelChoiceField(queryset=UploadedImage.objects.values('image_description'))