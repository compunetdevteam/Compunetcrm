
###add personalization to mail
from sendgrid.helpers.mail import Substitution

from compunetcrm.models import UploadedImage, ImageTextCordinate

def img_source_substituition(subvalue):
	sub = Substitution('--imgurl--',subvalue)
	mail.personalizations[0].add_substitution(sub)
	return sub


##generate TEXT LINK PLACEMENT CORDINATE

def get_image_substituitions(id):
	a = UploadedImage.objects.get(id=id)
	b = a.imagetextcordinate_set.all()
	embed_image = []
	for any in b:
		top = str(any.top)
		right = str(any.right)
		bottom = str(any.bottom)
		left = str(any.left)
		link = str(any.link)
		true = '<area shape="rect" coords="' + top + ',' + right + ',' + bottom + ',' + left + '"' + ' ' + 'href="' + link + '"' + 'alt="Compunet" / >'
		embed_image.append(true)
		embed_image
	return embed_image


