from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
cryptohackBaseURL="https://aes.cryptohack.org"
cryptohackEncryptRoute="/ecb_oracle/encrypt/"

# KEY=bytes.fromhex("addeaddebb666666addeaddebb666666")
# FLAG="crypto{l333tcr1ngestuff}"
# print(FLAG.encode().hex())
# def encrypt(plaintext):
#     plaintext = bytes.fromhex(plaintext)

#     padded = pad(plaintext + FLAG.encode(), 16)
#     cipher = AES.new(KEY, AES.MODE_ECB)
#     try:
#         encrypted = cipher.encrypt(padded)
#     except ValueError as e:
#         return {"error": str(e)}

#     return {"ciphertext": encrypted.hex()}
def encrypt(plaintext):
  r=requests.get(cryptohackBaseURL+cryptohackEncryptRoute+plaintext+"/")
  return r.json()

def toAscii(x):
  return hex(x//16)[2:]+hex(x%16)[2:]  
found_flag_chars=""
# for curr_pos in range(15,-1,-1):
for curr_pos in range(31,-1,-1):
  padding=' '+'00'*curr_pos
  real_hash=encrypt(padding)["ciphertext"][:64]
  print(padding,real_hash)
  for x in range(256):
    padding='00'*curr_pos+found_flag_chars+toAscii(x)
    # print(padding,real_hash)
    curr_hash=encrypt(padding)["ciphertext"][:64]
    if curr_hash==real_hash:
      print("YEP,for x=",x)
      found_flag_chars=found_flag_chars+toAscii(x)
      # print(found_flag_chars)
      break
print("key chars:",found_flag_chars)

flag=bytes.fromhex(found_flag_chars)