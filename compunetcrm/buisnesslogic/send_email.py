import sendgrid
from decouple import config
from sendgrid.helpers.mail import *


#global variables
sg = sendgrid.SendGridAPIClient(apikey=config('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
to_email = Email("test@example.com")


def send_email(request):
    subject = "Seasons Greetings From Compunet"
    content = Content("text/html", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    mail.template_id = config('SENDGRID_TEMPLATE_ID')
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)


def send_email(request):
    subject = "Sending with SendGrid is Fun"
    content = Content("text/html", "and easy to do anywhere, even with Python")
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    print(response.status_code)
    print(response.body)
    print(response.headers)
