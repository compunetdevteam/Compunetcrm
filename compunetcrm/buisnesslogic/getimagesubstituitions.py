from sendgrid.helpers.mail import Substitution

from compunetcrm.models import UploadedImage, ImageTextCordinate


def get_text_cordinate_substituitions(a):
    b = a.imagetextcordinate_set.all()
    for any in b:
        embed_image = ''
        top = str(any.top)
        right = str(any.right)
        bottom = str(any.bottom)
        left = str(any.left)
        link = str(any.link)
        embed_image += '<area shape="rect" coords="' + top + ',' + right + ',' + bottom + ',' + left + '"' + ' ' + 'href="' + link + '"' + 'alt="Compunet" / >'
        sub = Substitution('--rhythym0--', embed_image)
        return sub

def get_img_source_substituition(subvalue):
    sub = Substitution('--rhythym2--',subvalue)
    return sub