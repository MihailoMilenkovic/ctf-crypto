from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import requests
from pwn import *
cryptohackBaseURL="https://aes.cryptohack.org"
cryptohackEncryptRoute="/ecbcbcwtf/encrypt_flag/"
cryptohackDecryptRoute="/ecbcbcwtf/decrypt/"

ciphertext="48cc66d39c9b4b6316ceb148329c9cac3881b4398bf1e9a1a0a3e7e87098bc3c331b4854f7934e8f64e871824c3c1c3c"
iv=bytes.fromhex(ciphertext[:32])
ciphertext=ciphertext[32:]
print(ciphertext,len(ciphertext))

ciphertextFirst=ciphertext[:32]
ciphertextSecond=ciphertext[32:64]
resp=requests.get(cryptohackBaseURL+cryptohackDecryptRoute+ciphertextFirst+"/").json()["plaintext"]
print(ciphertextFirst,resp)
flag1=xor(bytes.fromhex(resp),iv).hex()
resp=requests.get(cryptohackBaseURL+cryptohackDecryptRoute+ciphertextSecond+"/").json()["plaintext"]
flag2=xor(bytes.fromhex(resp),bytes.fromhex(ciphertextFirst)).hex()
print(flag1,flag2,bytes.fromhex(flag1+flag2))