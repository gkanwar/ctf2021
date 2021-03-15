from Crypto.Cipher import AES
import random

key = random.getrandbits(128).to_bytes(16, 'big')
cipher = AES.new(key, AES.MODE_ECB)
with open('flag.bin', 'rb') as f:
    framebuffer = f.read()
c = cipher.encrypt(framebuffer)
with open('flag.enc', 'wb') as f:
    f.write(c)
