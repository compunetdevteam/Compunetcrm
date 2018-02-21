from django import forms
from compunetcrm.models import UploadedImage


class ComposeEmailForm(forms.Form):
    to_email = forms.CharField(max_length=200)
    from_mail = forms.CharField(max_length=300)
    subject = forms.CharField(max_length=200)
    body = forms.CharField(max_length=800, widget=forms.Textarea(attrs={'rows': 10, 'cols': 20}))
    image_name = forms.ChoiceField(choices=[(choice.pk, choice) for choice in UploadedImage.objects.all()])