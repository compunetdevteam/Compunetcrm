
###add personalization to mail
for t in range(4):
	id = 'rhythym'+t.__str__()
	real = '--'+id+'--'
	sub = ''
	sub = sub+id
	sub = Substitution(real,'https://marketing-image-production.s3.amazonaws.com/uploads/2a274fc32af72b861183bb762301b979660bab5345af6083dfff79847b0dd28dc19c7fd6b08861a6700d20926ead7d21dfb02ae3fb2ecf208b0e182038d24126.jpg')
	mail.personalizations[0].add_substitution(sub)


##generate TEXT LINK PLACEMENT CORDINATE
textlinkcount = int
top = str(3)
right=str(3)
bottom = str(3)
left = str(3)
link =str(3)
a = '<area shape="rect" coords="' + top  + ',' + right  + ',' + bottom +  ',' + left + '"' + ' ' + 'href="' + link + '"' + 'alt="Compunet" / >'