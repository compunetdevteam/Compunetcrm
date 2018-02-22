from django import forms
from compunetcrm.forms.MultiEmailFormFieldValidator import CommaSeparatedEmailField
from compunetcrm.models import UploadedImage
from multi_email_field.forms import MultiEmailField


class ComposeEmailForm(forms.Form):
    to_email= CommaSeparatedEmailField(help_text="Please Enter Email Addresses Seperated by  comma ' , ' ")
    from_mail = forms.EmailField(max_length=300, widget=forms.EmailInput, help_text="Enter Approved Official Email")

    subject = forms.CharField(max_length=200, help_text="Enter Email Subject")
    body = forms.CharField(max_length=800, widget=forms.Textarea(attrs={'rows': 10, 'cols': 20}), help_text="Enter Email Subject")
    image_name = forms.ChoiceField(choices=[(choice.pk, choice) for choice in UploadedImage.objects.all()], help_text="Select An Image")