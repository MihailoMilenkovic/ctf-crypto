import hashlib
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

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

def find_y(x,a,b,mod):
  return pow((pow(x,3,mod)+a*x+b)%mod,(mod+1)//4,mod)

def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


a=497
b=1768
mod=9739
G=(1804,5368)
qx=4726

#QA is G*na (we only need to send x, since we can caluculate y from it)
QA = (qx, find_y(qx,a,b,mod))
#nb is our private key
nB = 6534
#our shared secret is the x coordinateG*na*nb - not reversible due to the hardness of the elliptic curve discrete log problem
shared_secret=multiply(QA,nB,a,mod)[0]
iv="cd9da9f1c60925922377ea952afc212c"
ciphertext="febcbe3a3414a730b125931dccf912d2239f3e969c4334d95ed0ec86f6449ad8"
print(decrypt_flag(shared_secret, iv, ciphertext))