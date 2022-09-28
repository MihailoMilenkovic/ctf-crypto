from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from datetime import datetime, timedelta
from pwn import *
import requests

cryptohackBaseURL="https://aes.cryptohack.org"
encryptChooseRoute="/symmetry/encrypt/"
encryptFlagRoute="/symmetry/encrypt_flag/"

def encryptChoose(plaintext,iv):
  ciphertext=requests.get(cryptohackBaseURL+encryptChooseRoute+"/"+plaintext+"/"+iv).json()["ciphertext"]
  return ciphertext

def encryptFlag():
  resp=requests.get(cryptohackBaseURL+encryptFlagRoute).json()["ciphertext"]
  iv=resp[:32]
  ciphertext=resp[32:]
  return iv,ciphertext

iv,ciphertext=encryptFlag()
encZeroes=encryptChoose("00"*48,iv)
plaintext=xor(bytes.fromhex(encZeroes),bytes.fromhex(ciphertext))
print(plaintext)
