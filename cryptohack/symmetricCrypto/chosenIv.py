from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
from pwn import *
import requests

cryptohackBaseURL="https://aes.cryptohack.org"
getCookieRoute="/flipping_cookie/get_cookie/"
checkAdminRoute="/flipping_cookie/check_admin/"

def encrypt():
  resp=requests.get(cryptohackBaseURL+getCookieRoute+"/").json()["cookie"]
  iv1=bytes.fromhex(resp[:32])
  cookie=resp[32:]
  expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
  text1 = f"admin=False;expiry={expires_at}".encode()
  text2 = f"admin=True;expiry={expires_at}".encode()
  return cookie,iv1,text1,text2

def decrypt(cookie,iv2):
  r=requests.get(cryptohackBaseURL+checkAdminRoute+"/"+cookie+"/"+iv2.hex()+"/").json()
  print(r)

cookie,iv1,text1,text2=encrypt()
iv2=xor(xor(iv1,text1[:16]),text2[:16])
decrypt(cookie,iv2)