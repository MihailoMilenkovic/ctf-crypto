#import gcd
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
def order(a, n):
    if gcd(a, n) != 1:
        return 0
    else:
        k = 1
        while pow(a, k, n) != 1:
            k += 1
        return k
p=28151
for i in range(28151):
    if order(i, 28151) == 28150:
        print(i)
        exit()