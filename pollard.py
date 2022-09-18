'''
Python code for pollard rho and p-1 algorithms for integer factorization
Pollard rho factorizes a number n in O(sqrt(p)), where p is the smallest prime factor of n
Pollard p-1 factorizes a number by finding a factor p for which all prime factors of p-1 are <=B for some B.
The complexity of this algorithm is O(log^2(n)*B*log(B))
'''

from math import gcd

def f(x):
	""" function for pollard's rho """
	return x**2 + 1

def factor(n,b):
	""" Factor using Pollard's p-1 method """

	a = 2;
	for j in range(2,b):
		a = a**j % n
	
	d = gcd(a-1,n);
	if 1 < d < n: return d;
	else: return -1;

def factorRho(n,x_1):
	""" Factor using pollard's rho method """
	
	x = x_1;
	xp = f(x) % n
	p = gcd(x - xp,n)

	while p == 1:
		# in the ith iteration x = x_i and x' = x_2i
		x = f(x) % n
		xp = f(xp) % n
		xp = f(xp) % n
		p = gcd(x-xp,n)


	if p == n: return -1
	else: return p

def testFactor():
	n = 132581598603049565570445277814735679644260013355471715821821624295948191014423226525651922904323847557647508479482845917721905137712312456116268480934743641779359150476059151920719032701681187493616123890637958351366432272254306175274942017083214904069977598799908566948743285896804802443914589397939268106787
	s = 2
	d = -1


	while s < n and d == -1:
		s +=1
		d = factor(n,s)

	return d

def testFactorRho():

	n = 132581598603049565570445277814735679644260013355471715821821624295948191014423226525651922904323847557647508479482845917721905137712312456116268480934743641779359150476059151920719032701681187493616123890637958351366432272254306175274942017083214904069977598799908566948743285896804802443914589397939268106787
	x_1 = 150

	
	p = factorRho(n,x_1)
	return p

d=testFactor();
print(d)