from pwn import *
import json
conn = remote('socket.cryptohack.org',13371)

alice_msg=conn.recvline()
print(alice_msg)
#remove everything except between the curly braces
alice_msg=alice_msg[alice_msg.find(b'{'):alice_msg.find(b'}')+1]
#convert from json to python object
alice_msg=json.loads(alice_msg)
alice_msg["A"]="0x1"

conn.sendline(json.dumps(alice_msg).encode())

bob_msg=conn.recvline()
print(bob_msg)
#remove everything except between the curly braces
bob_msg=bob_msg[bob_msg.find(b'{'):bob_msg.find(b'}')+1]
#convert from json to python object
bob_msg=json.loads(bob_msg)
bob_msg["B"]="0x1"

conn.sendline(json.dumps(bob_msg).encode())


