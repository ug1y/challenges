'''
Programming.py

When you visit this link you receive a message.
Submit the same message back to http://www.wechall.net/challenge/training/programming1/index.php?answer=the_message
Your timelimit is 1.337 seconds
'''
import requests
url="http://www.wechall.net/challenge/training/programming1/index.php"
cookies={'WC':'9104130-20548-78ImmmmnARsYDJCr'}
msg=requests.get(url,params={'action':'request'},cookies=cookies).text
ans=requests.get(url,params={'answer':msg},cookies=cookies).content
print ans
