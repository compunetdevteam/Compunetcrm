from sendgrid.helpers.mail import Substitution

from compunetcrm.models import UploadedImage, ImageTextCordinate



def get_text_cordinate_substituitions(a):
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

    links = ''.join(embed_image)
    sub = Substitution('--textlink--', links)

    return sub


def get_img_source_substituition(subvalue):
    sub = Substitution('--imgurl--', subvalue)
    return sub