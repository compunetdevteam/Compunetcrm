from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
import sendgrid
from decouple import config
from sendgrid.helpers.mail import *


from compunetcrm.buisnesslogic.getimagesubstituitions import get_text_cordinate_substituitions,get_img_source_substituition
from compunetcrm.buisnesslogic.send_sms import send_sms_api
from compunetcrm.forms.AddCustomerForm import CustomerUploadForm
from compunetcrm.forms.SendSmsForm import ComposeSmsForm
from compunetcrm.forms.imageupload import ImageUploadForm
from compunetcrm.forms.compose_mail import ComposeEmailForm
from compunetcrm.models import UploadedImage, SentMail, Customer, SentSms

sg = sendgrid.SendGridAPIClient(apikey=config('SENDGRID_API_KEY'))



def send_email_form(request):
    if request.method == 'POST':
        form = ComposeEmailForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['to_email']
            sender = form.cleaned_data['from_mail']
            subject = form.cleaned_data['subject']
            image_name = form.cleaned_data['image_name']
            body = form.cleaned_data['body']
            image = UploadedImage.objects.get(id=int(image_name))

            # GET CHOSEN  IMAGE URL
            image_url = image.image_url

            ##GET IMAGE URL SUBSTITUITION

            image_url_substituition = get_img_source_substituition(image_url)

            ##GET IMAGE TEXT CORDINAT SUBSTITUITION

            image_text_cordinate_substituition = get_text_cordinate_substituitions(image)

            ##send mail

            for recipients in to:
                to_email = Email(recipients)
                from_email = Email(sender)
                content = Content("text/html", body)
                ##substituitions
                mail = Mail(from_email,  subject, to_email, content)
                mail.template_id = config('SENDGRID_TEMPLATE_ID')
                mail.personalizations[0].add_substitution(image_url_substituition)
                mail.personalizations[0].add_substitution(image_text_cordinate_substituition)
                print(mail.get())
                response = sg.client.mail.send.post(request_body=mail.get())
                if response.status_code == 202:
                    status = 'Delivered'
                    SentMail.objects.create(sent_to=recipients,image_address=image_name, subject=subject, body=body, status=status,
                                            from_email=sender)
                else:
                    status = 'Failed'
                    SentMail.objects.create(image_address=image_name, subject=subject, body=body, status=response.status,
                                            from_email=from_email)
                    return HttpResponse('Failed')
            return redirect('view_mail')
    else:
        form = ComposeEmailForm()
    return render(request, 'compose_mail.html', {
        'form': form})


def send_sms(request):
    if request.method == 'POST':
        form = ComposeSmsForm(request.POST)
        if form.is_valid():
            to = form.cleaned_data['phone_number']
            message = form.cleaned_data['message_body']
            success = send_sms_api(to=to, message=message)
            if success['status'] == 'Success':
                SentSms.objects.create(sent_to=success['number'],cost=success['cost'],message_id=success['messageId'],status=success['status'])
            return redirect('view-mail')
    else:
        form = ComposeSmsForm()
    return render(request, 'compose_sms.html', {
        'form': form
    })


def upolad_images(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            a = form.save()

            return redirect('view_mail')
    else:
        form = ImageUploadForm()
    return render(request, 'image_upload.html', {
        'form': form
    })


def add_customer_information(request):
    if request.method == 'POST':
        form = CustomerUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CustomerUploadForm()
    return render(request, 'customer_upload.html', {
        'form': form
    })


def view_mails(request):
    sent_mails = SentMail.objects.all().select_related('image_sent')
    return render(request, 'rocket_template/messages.html', {'sent_mail': sent_mails})


def view_mail_inbox(request,pk):
    try:
        view_mail = SentMail.objects.get(id=pk)
    except ObjectDoesNotExist:
        pass
    return render(request, 'rocket_template/view-message.html', {'view_mail': view_mail})

def view_clients(request):
    clients = Customer.objects.all()
    return render(request,'rocket_template/clients.html', {'client':clients})