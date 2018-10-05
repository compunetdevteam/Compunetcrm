from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ComposeSmsForm(forms.Form):
    phone_number = forms.CharField(max_length=800, label="Phone Numbers", help_text=" Enter Phone Numbers Seperated by ' , ' ")
    message_body = forms.CharField(max_length=300, label="Compose Message", widget=forms.Textarea, help_text="Enter Approved Official Email")
