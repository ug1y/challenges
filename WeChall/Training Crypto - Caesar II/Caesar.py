'''
Caesar.py

I guess you are done with Caesar I, aren't you?
The big problem with caesar is that it does not allow digits or other characters.
I have fixed this, and now I can use any ascii character in the plaintext.
The keyspace has increased from 26 to 128 too. \o/

Enjoy!
'''

b='3A 62 62 57 20 5D 62 55 1F 20 6C 62 68 20 66 62 \
5F 69 58 57 20 62 61 58 20 60 62 65 58 20 56 5B \
54 5F 5F 58 61 5A 58 20 5C 61 20 6C 62 68 65 20 \
5D 62 68 65 61 58 6C 21 20 47 5B 5C 66 20 62 61 \
58 20 6A 54 66 20 59 54 5C 65 5F 6C 20 58 54 66 \
6C 20 67 62 20 56 65 54 56 5E 21 20 4A 54 66 61 \
1A 67 20 5C 67 32 20 24 25 2B 20 5E 58 6C 66 20 \
5C 66 20 54 20 64 68 5C 67 58 20 66 60 54 5F 5F \
20 5E 58 6C 66 63 54 56 58 1F 20 66 62 20 5C 67 \
20 66 5B 62 68 5F 57 61 1A 67 20 5B 54 69 58 20 \
67 54 5E 58 61 20 6C 62 68 20 67 62 62 20 5F 62 \
61 5A 20 67 62 20 57 58 56 65 6C 63 67 20 67 5B \
5C 66 20 60 58 66 66 54 5A 58 21 20 4A 58 5F 5F \
20 57 62 61 58 1F 20 6C 62 68 65 20 66 62 5F 68 \
67 5C 62 61 20 5C 66 20 56 59 5A 57 57 65 5B 63 \
5B 5B 55 65 21'

def trans(b,off):
	return "".join([chr((int(c,16)+off)%256) for c in b.split(' ')])

if __name__ == '__main__':
	for i in range(256):
		print i,trans(b,i)