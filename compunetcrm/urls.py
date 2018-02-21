import asyncio
import concurrent
from concurrent.futures import ThreadPoolExecutor

from django.conf.urls import url
from django.db.migrations import executor

from compunetcrm import views

urlpatterns = [
    url(r'correct/$', views.sendmail_template, name='home'),
    url(r'add_customer$', views.add_customer_information, name='add-customer'),
    url(r'upload_image$', views.upolad_images, name='upload-images'),
    url(r'send_mail$', views.send_email_form, name='send-mail'),
    url(r'mails$', views.view_mails, name='view-mail'),
    url(r'mails_open/(?P<pk>\d+)$', views.view_mail_inbox, name='view-mail-inbox'),
    url(r'view_clients$', views.view_mail_inbox, name='view-clients'),
]
