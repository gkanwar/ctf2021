from Crypto.PublicKey import RSA

with open('flag.txt', 'r') as f:
    flag = f.readline().strip().encode()

key = RSA.generate(2048, e=3)
m = int.from_bytes(flag, 'big')
c = pow(m, key.e, key.n) # m^e % n

with open('big_primes.txt', 'wb') as f:
    f.write(key.publickey().export_key('PEM') + b'\n')
    f.write(b'c = ' + str(c).encode() + b'\n')
