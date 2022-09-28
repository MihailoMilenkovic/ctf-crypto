from Crypto.Cipher import AES
import requests
from PIL import Image
from pwn import *
cryptohackBaseURL="https://aes.cryptohack.org"
encryptRoute="/bean_counter/encrypt/"
ciphertext=requests.get(cryptohackBaseURL+encryptRoute).json()["encrypted"]

#png header as bytes
png_hdr = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])
xor_key=xor(bytes.fromhex(ciphertext[:32]),png_hdr)

bytes=bytearray()
for i in range(0,len(ciphertext),32):
  bytes+=xor(bytes.fromhex(ciphertext[i:i+32]),xor_key)
with open('bean_counter.png', 'wb') as fd:
    fd.write(bytes)