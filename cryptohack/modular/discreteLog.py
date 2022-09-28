from sympy.ntheory import discrete_log
#finds the number a such that a^b=x(mod p)
#works in O(log(p))
b=15
x=7
p=41
discrete_log(p,b,x)