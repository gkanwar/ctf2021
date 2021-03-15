from Crypto.Hash import SHA256
import time

api_key = '62c87a343ba883fbd8be60f82fee50a7a5d04f647866707521b29031ee55db61'
enc_key = bytes.fromhex('1be6ae0b28959a3e95b2d6e419aa7050e63f6b8b6d8d33223b7442aee5718978')

query = f'timestamp={int(time.time())}&action=read&api_key={api_key}'
h = SHA256.new()
h.update(enc_key + query.encode())
hmac = h.hexdigest()

query += f'&hmac={hmac}'

print(query)
