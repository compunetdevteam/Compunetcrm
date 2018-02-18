from django.conf.urls import url

from compunetcrm import views

urlpatterns = [
    url(r'correct/$', views.sendmail_template, name='home'),
    url(r'add_customer$', views.add_customer_information, name='add-customer'),
    url(r'upload_image$', views.upolad_images, name='upload-images'),
    url(r'send_mail$', views.send_email_form, name='send-mail'),

]