import hashlib
def inverse(x,mod):
  return pow(x,mod-2,mod)
def add(p,q,a,mod):
  if (p == [0,0]):
    return q
  elif (q == [0,0]):
    return p
  elif (p[0] == q[0] and p[1] == -q[1]):
    return [0,0]
  else:
    if (p != q):
      lam = ((q[1] - p[1]) * inverse(q[0] - p[0],mod))%mod
    else:
      lam = ((3 * p[0] ** 2 + a) *inverse(2 * p[1],mod))%mod
    x3 = (lam ** 2 - p[0] - q[0])%mod
    y3 = (lam * (p[0] - x3) - p[1])%mod
    return [x3,y3]

def multiply(p,n,a,mod):
  if (n == 0):
    return [0,0]
  elif (n == 1):
    return p
  else:
    q = multiply(p,n//2,a,mod)
    q = add(q,q,a,mod)
    if (n%2 == 1):
      q = add(q,p,a,mod)
    return q

a=497
b=1768
mod=9739
G=(1804,5368)
#QA is G*na
QA = (815, 3190)
#nb is our private key
nB = 1829
#our shared secret is G*na*nb - not reversible due to the hardness of the elliptic curve discrete log problem
shared_secret=multiply(QA,nB,a,mod)
print(hashlib.sha1(str(shared_secret[0]).encode()).hexdigest())