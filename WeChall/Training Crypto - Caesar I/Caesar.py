'''
Caesar.py

As on most challenge sites, there are some beginner cryptos, and often you get started with the good old caesar cipher.
I welcome you to the WeChall style of these training challenges :)

Enjoy!
IWT FJXRZ QGDLC UDM YJBEH DKTG IWT APON SDV DU RPTHPG PCS NDJG JCXFJT HDAJIXDC XH SURBAECEECCS
'''
def rot13(s,offSet=13):
   d={chr(i+c) : chr((i+offSet) % 26 + c) for i in range(26) for c in (65,97)}
   return ''.join([d.get(c, c) for c in s])

def getAns(s):
	for x in xrange(1,26):
		print x,rot13(s,x)

if __name__ == '__main__':
	s='OCZ LPDXF WMJRI AJS EPHKN JQZM OCZ GVUT YJB JA XVZNVM VIY TJPM PIDLPZ NJGPODJI DN YAXHGKIKKIIY'
	getAns(s)