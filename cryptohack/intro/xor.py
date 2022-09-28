from pwn import *
string="label"
num=[ord(c) for c in string]
flag="".join([chr(13^d) for d in num])
print(flag)

print(xor(bytes(string,"ascii"),13))