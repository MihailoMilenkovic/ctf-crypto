from re import A


def gcd(a,b):
  if b==0:
    return a
  return gcd(b,a%b)

a = 288260533169915
p = 1007621497415251
print(gcd(a,p))