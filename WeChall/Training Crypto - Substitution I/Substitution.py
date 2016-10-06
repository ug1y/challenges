'''
Substitution.py

Oh dear, I guess you have cracked the two caesar cryptos...
This one is more difficult. Although a simple substitution is easily cracked...
Again the characters are limited to A-Z... But I think I can come up with a 256 version again.

Enjoy!

reference：http://www.quipqiup.com
'''
s='DU CZA SEGYWZCU WKL UKJ HSV NASL CZYB GU TNYAVL Y SG YGRNABBAL XANU PAEE LKVA UKJN BKEJCYKV IAU YB ENYNGRLALVTS CZYB EYCCEA HZSEEAVWA PSB VKC CKK ZSNL PSB YC'

d={
'A':'E',
'B':'S',
'C':'T',
'D':'B',
'E':'L',

'G':'M',
'H':'C',
'I':'K',
'J':'U',
'K':'O',
'L':'D',

'N':'R',

'P':'W',

'R':'P',
'S':'A',
'T':'F',
'U':'Y',
'V':'N',
'W':'G',
'X':'V',
'Y':'I',
'Z':'H',
}

def substitute(s,d):
	return "".join([d[c] if c in d.keys() else c for c in s])

if __name__ == '__main__':
	print substitute(s,d)