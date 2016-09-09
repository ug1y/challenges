'''
ASCII.py

In a computer, you can only work with numbers.
In this challenge you have to decode the following message, which is in ASCII.
'''
a=[84, 104, 101, 32, 115, 111, 108, 117, 116, 105, 111, 110, 32, 105, 115, 58, 32, 104, 108, 98, 98, 110, 105, 110, 114, 108, 114, 109, 103]
print "".join([chr(i) for i in a])