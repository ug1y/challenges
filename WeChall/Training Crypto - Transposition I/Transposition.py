'''
Transposition.py

It seems that the simple substitution ciphers are too easy for you.
From my own experience I can tell that transposition ciphers are more difficult to attack.
However, in this training challenge you should have not much problems to reveal the plaintext.
'''
s='oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wi rpsmderebp.b'

def split(str,n):
	return [list(str[i*n:(i+1)*n]) for i in range(len(str)/n)]

def merge(l):
	return "".join(["".join(s) for s in l])

def transpos(mat,key):
	return [[x[key[i]] for i in range(len(key))] for x in mat]

def Transpose(mat):
	return [[mat[x][i] for x in range(len(mat))] for i in range(len(mat[0]))]

if __name__ == '__main__':
	print merge(transpos(split(s,4),[1,0,3,2]))
	print merge(transpos(split(s,2),[1,0]))