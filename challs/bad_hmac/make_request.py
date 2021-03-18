from Crypto.Hash import SHA256
import requests
import time

# our test account keys
api_key = 'b4a62ea61b142a5f98fa5990fcb7bae2259d3e18f40f4f265a3044e5e7337495'
enc_key = bytes.fromhex('b80c0227d8d934f881367980eb29770fc8220a65058bf89013ffbdd596ae0757')

query = f'timestamp={int(time.time())}&action=read&api_key={api_key}'
h = SHA256.new()
h.update(enc_key + query.encode())
hmac = h.hexdigest()

query += f'&hmac={hmac}'

r = requests.get(f'http://rmrfslash.xyz:8003/api/v1/secrets?{query}')
print(r.status_code)
print(r.json())
