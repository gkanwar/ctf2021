from Crypto.Hash import SHA256
import requests
import time

# root account keys
api_key = '62c87a343ba883fbd8be60f82fee50a7a5d04f647866707521b29031ee55db61'
enc_key = bytes.fromhex('1be6ae0b28959a3e95b2d6e419aa7050e63f6b8b6d8d33223b7442aee5718978')

query = f'api_key={api_key}&timestamp={int(time.time())}&action=read'
h = SHA256.new()
h.update(enc_key + query.encode())
hmac = h.hexdigest()

query += f'&hmac={hmac}'
path = f'/api/v1/secrets?{query}'

print('Captured request:')
print(path)
r = requests.get(f'http://rmrfslash.xyz:8003{path}')
print(r.status_code)
print(r.json())
