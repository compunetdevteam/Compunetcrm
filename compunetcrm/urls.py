from django.conf.urls import url
from compunetcrm import views

urlpatterns = [
    url(r'add_customer$', views.add_customer_information, name='add-customer'),
    url(r'upload_image$', views.upolad_images, name='upload-images'),
    url(r'send_mail$', views.send_email_form, name='send-mail'),
    url(r'mails$', views.view_mails, name='view-mail'),
    url(r'mails_open/(?P<pk>\d+)$', views.view_mail_inbox, name='view-mail-inbox'),
    url(r'view_clients$', views.view_mail_inbox, name='view-clients'),
    url(r'send_sms$', views.send_sms, name='send_sms'),
    url(r'sms$', views.view_sms, name='view-sms'),
    url(r'sms_open/(?P<pk>\d+)$', views.view_sms_inbox, name='view-sms-inbox'),
]
