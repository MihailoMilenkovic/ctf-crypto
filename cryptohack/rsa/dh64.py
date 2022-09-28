import pwn
import json
import hashlib
from Crypto.Cipher import AES
from sympy.ntheory import discrete_log

host = "socket.cryptohack.org"
port = 13379


def exploit():
    pr = pwn.connect(host, port)
    try:
        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())

        payload = json.dumps({"supported":["DH64"]})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())

        payload = json.dumps({"chosen":"DH64"})
        print(payload, len(payload))
        pr.sendlineafter(": ", payload)

        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        p=int(line["p"][2:],16)
        g=int(line["g"][2:],16)
        A=int(line["A"][2:],16)
        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        B=int(line["B"][2:],16)
        print(line,B)
        pr.readuntil(": ")
        line = json.loads(pr.readline().strip().decode())
        iv=bytes.fromhex(line["iv"])
        encrypted_flag=bytes.fromhex(line["encrypted_flag"])
        print(line,iv,encrypted_flag)

        sha1 = hashlib.sha1()
        a=discrete_log(p,A,g)
        secret = pow(B,a,p)
        sha1.update(str(secret).encode())
        key = sha1.digest()[:16]
        aes = AES.new(key, AES.MODE_CBC, iv)
        print(aes.decrypt(encrypted_flag))
    finally:
        pr.close()

exploit()