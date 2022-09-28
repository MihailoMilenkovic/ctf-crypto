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

# Algorithm for the addition of two points: P + Q

# (a) If P = O, then P + Q = Q.
# (b) Otherwise, if Q = O, then P + Q = P.
# (c) Otherwise, write P = (x1, y1) and Q = (x2, y2).
# (d) If x1 = x2 and y1 = −y2, then P + Q = O.
# (e) Otherwise:
#   (e1) if P ≠ Q: λ = (y2 - y1) / (x2 - x1)
#   (e2) if P = Q: λ = (3x12 + a) / 2y1
# (f) x3 = λ2 − x1 − x2,     y3 = λ(x1 −x3) − y1
# (g) P + Q = (x3, y3)
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

X = (5323, 5438)
# print(multiply(X,1337,a,mod))

p= (2339, 2213)
print(multiply(p,7863,a,mod))