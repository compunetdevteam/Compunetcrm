
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
	for any in b:
		embed_image = ''
		top = str(any.top)
		right = str(any.right)
		bottom = str(any.bottom)
		left = str(any.left)
		link = str(any.link)

		embed_image += '<area shape="rect" coords="' + top + ',' + right + ',' + bottom + ',' + left + '"' + ' ' + 'href="' + link + '"' + 'alt="Compunet" / >'
		print(embed_image)
		return embed_image