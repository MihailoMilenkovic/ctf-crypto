import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def inverse(x,mod):
  return pow(x,mod-2,mod)
  

#Montogomery curve - a curve with the form By2 = x3 + Ax2 + x
def find_y_montogamery(x,a,b,mod):
  y_squared = (x**3 + a*x**2 + x)*inverse(b,mod)%mod
  if(mod+1)%4==0:
    y = pow(y_squared,(mod+1)//4,mod)
  elif((mod+3)%8==0):
    k=(mod-5)//8
    assert(pow(y_squared,(mod-1)//4,mod)==1 or pow(y_squared,(mod-1)//4,mod)==mod-1)
    if pow(y_squared,(mod-1)//4,mod)==1:
      y = pow(y_squared,k+1,mod)
    else:
      y = pow(2,2*k+1,mod)*pow(y_squared,k+1,mod)%mod
  else:
    assert False
  assert(pow(y,2,mod)==y_squared)
  return y

# Addition formula for Montgomery Curve (Affine)

# Input: P, Q in E(Fp) with P != Q
# Output: R = (P + Q) in E(Fp)

# α = (y2 - y1) / (x2 - x1 )
# x3 = Bα2 - A - x1 - x2
# y3 = α(x1 - x3) - y1
def addMontgomery(p,q,a,b,mod):
  if (p == [0,0]):
    return q
  elif (q == [0,0]):
    return p
  elif (p[0] == q[0] and p[1] == -q[1]):
    return [0,0]
  else:
    lam = ((q[1] - p[1]) * inverse(q[0] - p[0],mod))%mod
    x3 = (b*(lam ** 2) - a - p[0] - q[0])%mod
    y3 = (lam * (p[0] - x3) - p[1])%mod
    return [x3,y3]

# Doubling formula for Montgomery Curve (Affine)

# Input: P in E(Fp)
# Output: R = [2]P in E(Fp)

# α = (3x21 + 2Ax1 + 1) / (2By1)
# x3 = Bα2 - A - 2x1
# y3 = α(x1 - x3) - y1
def doubleMontogomery(p,a,b,mod):
  lam = (((3 * (p[0] ** 2)) + (2*a*p[0])+1) *inverse(2 *b* p[1],mod))%mod
  x3 = (b*(lam ** 2) - a - 2*p[0])%mod
  y3 = (lam * (p[0] - x3) - p[1])%mod
  return [x3,y3]

# Montogomery’s binary algorithm using addition and doubling for montgomery curves
def montogomeryRecommended(p,k,a,b,mod):
  R0 = p
  R1 = doubleMontogomery(p,a,b,mod)
  for i in range(k.bit_length()-2,-1,-1):
    if (k>>i)%2 == 0:
      R0 = doubleMontogomery(R0,a,b,mod)
      R1 = addMontgomery(R0,R1,a,b,mod)
    else:
      R0 = addMontgomery(R0,R1,a,b,mod)
      R1 = doubleMontogomery(R1,a,b,mod)
  return R0

b=1
a=486662
p=2**255-19
G=[9,find_y_montogamery(9,a,b,p)]
assert(doubleMontogomery(G,a,b,p)==addMontgomery(G,G,a,b,p))
qx=0x1337c0decafe

print(montogomeryRecommended(G,qx,a,b,p))