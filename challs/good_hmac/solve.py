from Crypto.Hash import HMAC, SHA256
from pwn import *

r = remote('rmrfslash.xyz', 8005)
s = r.recvuntil('Choice').decode()
for line in s.split('\n'):
    if 'Key digest' in line:
        digest = line.strip().split(': ')[-1]

# when HMAC key is too long it is hashed... digest is the key!
key = bytes.fromhex(digest)
h = HMAC.new(key, digestmod=SHA256)
token = '|1'
h.update(token.encode())
hmac = h.hexdigest()
token += '|' + hmac

r.sendline('2')
r.recvuntil('Token')
r.sendline(token)
r.recvuntil('Choice')
r.sendline('1')
print(r.recvuntil('Choice').decode())
r.sendline('2')
