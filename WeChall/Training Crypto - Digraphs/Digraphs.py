'''
Digraphs.py

This time I am using a digraph crypto scheme to encrypt one letter into two characters.
With only 26 different letters I am able to encrypt up to 26*26 different characters.
The big problem again is sharing the key, but the cipher is easily broken anyway.
The message is in the current language, is written with correct case and punctuation. There are no line breaks.

Good luck!
'''

s='bdqwgmkguoomfxootromfxjuqwgmgxeu nfqwoo ojtkbkuoecjmfxtkoj fxxjjugx umtkgxgxomkgtk gxoobkbktkgxgxdlootrtreceu ofomgx gmqwfx fxqwqw ojjudldljubkootrfx tkjufxxjtkuovx voomgx jufxes oftktrtrvx kgqwqwoj fyqwweeu uigmfxtkuo fxxjjugx kqtkecvoqwuooj omgx gxqwtroofxjuqwgmdg kgqwgxgxdlgmbkjuwebkomuoeu'

d={
	'bd':'c',
	'qw':'o',
	'gm':'n',
	'kg':'g',
	'uo':'r',
	'om':'a',
	'fx':'t',
	'oo':'u',
	'tr':'l',
	'om':'a',
	'fx':'t',
	'ju':'i',
	'qw':'o',
	'gm':'n',
	'gx':'s',
	'eu':'!',
	'nf':'y',
	'dg':'s',
	'of':'w',
	'oj':'d',
	'dl':'f',
	'bk':'c',
	'tk':'e',
	'ec':'y',
	'xj':'h',
	'um':'m',
	'jm':'p',
	'kq':'k',
	'vo':'w',
	'fy':'j',
	'we':'b',
}
# successful
def slice(s,n):
	return [s[i*n:(i+1)*n] for i in range(len(s)/n)]

def separate(s):
	return [slice(c,2) for c in s.split(' ')]

def instead(l,d):
	f=lambda x:[d[i] if i in d.keys() else i for i in x]
	return [f(c) for c in l]

def merge(l):
	f=lambda x:"".join(x)
	return " ".join([f(c) for c in l])

if __name__ == '__main__':
	a=s.split(' ')
	b=merge(instead(separate(s),d)).split(' ')
	for i in range(len(a)):
		print len(b[i])-len(a[i])/2 ,b[i],a[i]
	# print s.split(' ')
	# print merge(instead(separate(s),d)).split(' ')