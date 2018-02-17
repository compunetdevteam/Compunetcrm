from http.client import HTTPResponse
from django.shortcuts import render, redirect
from compunetcrm.buisnesslogic import send_email
from compunetcrm.forms.imageupload import ImageUploadForm
from compunetcrm.forms.compose_mail import ComposeEmailForm
from compunetcrm.models import UploadedImage, SentMail
import sendgrid
from decouple import config
from sendgrid.helpers.mail import *
sg = sendgrid.SendGridAPIClient(apikey=config('SENDGRID_API_KEY'))





def sendmail_template(request):
    pass


def send_email_form(request):
    if request.method == 'POST':
        form = ComposeEmailForm(request.POST, request.FILES)
        if form.is_valid():
            to = form.cleaned_data['']
            from_email = form.cleaned_data['']
            subject = form.cleaned_data['']
            image_name = form.cleaned_data['']
            body = form.cleaned_data['']

            image_url = UploadedImage.objects.get(image_description=image_name).image_url
            ##send mail
            to_split = to.split(',')
            receipients =[ members for members in to_split]
            for to_email in receipients:
                content = Content("text/html", body)
                mail = Mail(from_email, subject, to_email, content)
                mail.template_id = config('SENDGRID_TEMPLATE_ID')
                response = sg.client.mail.send.post(request_body=mail.get())
                if response.status == 202:
                    status = 'Delivered'
                    SentMail.objects.create(image_address=image_name, subject=subject, body=body, status=status,
                                            from_email=from_email)
                else:
                    SentMail.objects.create(image_address=image_name, subject=subject, body=body, status=response.status,
                                            from_email=from_email)
                    return HTTPResponse('Failed')
            return redirect('home')
    else:
        form = ComposeEmailForm()
    return render(request, 'compose_mail.html', {
        'form': form
    })






def upolad_images(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {
        'form': form
    })


def add_customer_information(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ImageUploadForm()
    return render(request, 'customer_upload.html', {
        'form': form
    })

