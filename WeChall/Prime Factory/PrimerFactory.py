'''
PrimerFactory.py

Your task is simple:
Find the first two primes above 1 million, whose separate digit sums are also prime.
As example take 23, which is a prime whose digit sum, 5, is also prime.
The solution is the concatination of the two numbers,
Example: If the first number is 1,234,567
and the second is 8,765,432,
your solution is 12345678765432
'''
import shelve,math

class PrimerFactory():

	def __init__(self,file):
		'''load primer list to var'''
		self.file = file
		try:
			db = shelve.open(self.file,'c')
			if not db.has_key('pset'):
				db['pset'] = [2]
			self.pset = db['pset'][:]
		finally:
			db.close()

	def checkNum(self,num):
		'''compute if the num is primer'''
		if num < 2:
			return False 
		half = math.ceil(num ** 0.5)
		for p in self.pset:
			if p <= half and num % p == 0:
				return False
		else:
			return True

	def showAns(self,nMin,nMax):
		'''display primers in [min,max]'''
		res = []
		for p in self.pset:
			if nMin <= p and p <= nMax:
				res.append(p)
			elif p > nMax:
				break
		print res

	def iterNum(self,nMax):
		'''extend the primer list'''
		if nMax > self.pset[-1]:
			for p in xrange(self.pset[-1],nMax):
				if self.checkNum(p+1):
					self.pset.append(p+1)
			try:
				db = shelve.open(self.file,'c')
				db['pset'] = self.pset
			finally:
				db.close()

	def isPrimer(self,num):
		'''primer or not'''
		self.iterNum(num)
		if num in self.pset:
			return True
		else:
			return False

	def numSum(self,num):
		'''get the separate digit sums of number'''
		ans = 0
		while num:
			ans = ans + num % 10
			num = num // 10
		return ans

	def getChall(self):
		flag = 0
		start = 1000000
		while True:
			start = start + 1
			if self.isPrimer(start) and self.isPrimer(self.numSum(start)):
				print start
				flag = flag + 1
			if flag > 1:
				break

if __name__ == '__main__':
	c = PrimerFactory('db.dat')
	c.iterNum(1001000)
	c.getChall()