from pwn import *

# t=bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")
t=bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")

print(xor(t,"myXORkey"))