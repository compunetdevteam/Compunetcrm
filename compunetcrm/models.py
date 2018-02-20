from django.db import models

# Create your models here.


SEX_CHOICE = (
        ('MALE', "MALE"),
        ('FEMALE', "FEMALE"),
    )

CUSTOMER_TYPE = (
        ('SCHOOL OWNER', "SCHOOL OWNER"),
        ('BSC STUDENT', "BSC STUDENT"),
        ('SIWES STUDENT', "SIWES STUDENT"),
        ('WEEKEND TRAINING', "WEEKEND TRAINING"),
        ('GENERAL ENQUIRIES', "GENERAL ENQUIRIES"),
        ('INTERN', "INTERN"),
        ('COMPUNET STAFF', "COMPUNET STAFF"),
    )

STATE_CHOICE = (('ABIA', 'ABIA'), ('ADAMAWA', 'ADAMAWA'), ('AKWAIBOM', 'AKWAIBOM'), ('ANAMBRA', 'ANAMBRA'),
          ('BAUCHI', 'BAUCHI'), ('BAYELSA', 'BAYELSA'), ('BENUE', 'BENUE'), ('BORNO', 'BORNO'),
          ('CROSSRIVERS', 'CROSSRIVERS'), ('DELTA','DELTA'), ('EBONYI','EBONYI'), ('EDO','EDO'),
          ('EKITI', 'EKITI'), ('ENUGU', 'ENUGU'), ('GOMBE', 'GOMBE'), ('IMO', 'IMO'), ('JIGAWA', 'JIGAWA'),
          ('KADUNA', 'KADUNA'), ('KANO', 'KANO'), ('KATSINA', 'KATSINA'), ('KEBBI', 'KEBBI'), ('KOGI', 'KOGI'),
          ('KWARA', 'KWARA'), ('LAGOS', 'LAGOS'), ('NASARAWA', 'NASARAWA'), ('NIGER', 'NIGER'), ('OGUN', 'OGUN'),
          ('ONDO', 'ONDO'), ('OSUN', 'OSUN' ), ('OYO', 'OYO'), ('PLATEAU', 'PLATEAU'), ('RIVERS', 'RIVERS'),
          ('SOKOTO', 'SOKOTO'), ('TARABA', 'TARABA'), ('YOBE', 'YOBE'), ('ZAMFARA', 'ZAMFARA')
)


class Customer(models.Model):
    first_name = models.CharField(verbose_name='First Name', max_length=40)
    last_name = models.CharField(verbose_name='Surname', max_length=40)
    address = models.CharField(verbose_name='Address', max_length=100)
    state = models.CharField(verbose_name='State', max_length=100, choices=STATE_CHOICE)
    local_government = models.CharField(verbose_name='Local Government', max_length=70)
    sex = models.CharField(verbose_name="Sex", max_length=10, choices=SEX_CHOICE)
    phone_number = models.CharField(verbose_name='Phone Number', max_length=30)
    email = models.EmailField(verbose_name='E-mail', max_length=100)
    communication_means1 = models.NullBooleanField(verbose_name='Use Phone As Prefered Means Of Communication')
    communication_means2 = models.NullBooleanField(verbose_name='Use E-mail As Prefered Means Of Communication')
    customer_type = models.CharField(verbose_name="Customer Type", max_length=80, choices=CUSTOMER_TYPE,blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.customer_type


class UploadedImage(models.Model):
    image = models.FileField(upload_to='documents/')
    image_description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=25)
    image_text_xandy_cordinate = models.CharField(max_length=300)
    image_url = models.CharField(max_length=400)

    def __str__(self):
        return self.image_description


class SentMail(models.Model):
    sent_to = models.CharField(max_length=255, blank=True)
    image_address = models.CharField(max_length=255, blank=True)
    subject = models.CharField(max_length=255, blank=True)
    body = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=255, blank=True)
    from_email = models.CharField(max_length=255, blank=True)


class ImageTextCordinate(models.Model):
    imagelink = models.ForeignKey(UploadedImage, on_delete=models.CASCADE)
    top = models.DecimalField(max_digits=20, decimal_places=7)
    right = models.DecimalField(max_digits=20, decimal_places=7)
    bottom = models.DecimalField(max_digits=20, decimal_places=7)
    left = models.DecimalField(max_digits=20, decimal_places=7)
    link = models.CharField(verbose_name="Image URL", max_length=700, blank=False)
    alt_text = models.CharField(verbose_name="Image Alt Text", max_length=400, blank=False)

    def __str__(self):
        return 'Cordinates For Text Link On' + ' ' + self.imagelink.image_description + ' ' + 'Image'