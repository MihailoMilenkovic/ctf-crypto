from pwn import *
import requests
import hashlib
from Crypto.Cipher import AES
def decrypt(ciphertext, password_hash):
  ciphertext = bytes.fromhex(ciphertext)
  key = bytes.fromhex(password_hash)

  cipher = AES.new(key, AES.MODE_ECB)
  try:
    decrypted = cipher.decrypt(ciphertext)
  except ValueError as e:
    return {"error": str(e)}
  return {"plaintext": decrypted.hex()}
  
wordlistURL="https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words"
cryptohackBaseURL="https://aes.cryptohack.org/"
cryptohackEncryptRoute="/passwords_as_keys/encrypt_flag/"
cryptohackDecrptRoute="/passwords_as_keys/decrypt/" #cipertext/password_hash
encrpytedFlag=requests.get(f'{cryptohackBaseURL}{cryptohackEncryptRoute}').json()["ciphertext"]
print(encrpytedFlag)
wordlist=[x.strip() for x in requests.get(wordlistURL).text.split("\n")]

for keyword in wordlist:
  password_hash = hashlib.md5(keyword.encode()).hexdigest()
  # endpoint=f'{cryptohackBaseURL}{cryptohackDecrptRoute}{encrpytedFlag}/{password_hash}'
  # print(endpoint)
  res=decrypt(encrpytedFlag,password_hash)
  byteVal=bytes.fromhex(res["plaintext"])
  try:
    asciiVal=byteVal.decode("ascii")
    print(asciiVal)
  except Exception as e:
    pass
  # resp=requests.get(endpoint).json()["plaintext"]
  # print(bytes.fromhex(resp))