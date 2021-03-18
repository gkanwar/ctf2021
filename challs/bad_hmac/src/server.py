from flask import Flask, request
import json
import psycopg2
import re
import sys
import time
from Crypto.Hash import SHA256

app = Flask(__name__)
conn = psycopg2.connect(database="postgres", user="postgres", password="dummypassword", host="db")

@app.route('/api/v1/secrets', methods=['GET'])
def get_secrets():
    if 'api_key' not in request.args:
        return json.dumps({'error': 'api_key required'})
    if 'hmac' not in request.args:
        return json.dumps({'error': 'hmac required'})
    api_key = request.args['api_key']
    hmac = request.args['hmac']
    with conn.cursor() as cur:
        cur.execute('SELECT id,enc_key FROM users WHERE api_key=%s', [api_key])
        row = cur.fetchone()
        if row is None:
            return json.dumps({'error': f'api_key not found {api_key}'})
        user_id, enc_key = row
        enc_key = bytes.fromhex(enc_key)

    h = SHA256.new()
    remaining_query_string = request.query_string.decode()
    remaining_query_string = re.sub(r'&hmac=[^&]+', '', remaining_query_string)
    remaining_query_string = re.sub(r'hmac=[^&]+&', '', remaining_query_string)
    h.update(enc_key + remaining_query_string.encode())
    server_hmac = h.hexdigest()
    if server_hmac != hmac:
        return json.dumps({'error': 'HMAC mismatch'})
    
    query_string = request.query_string.decode()
    args = {}
    for arg in query_string.split('&'):
        if '=' not in arg:
            return json.dumps({'error': 'Malformatted query string'})
        key, val = arg.split('=', 1)
        args[key] = val

    if 'action' not in args:
        return json.dumps({'error': 'action required'})
    if 'timestamp' not in args:
        return json.dumps({'error': 'timestamp required'})

    try:
        if int(args['timestamp']) < time.time() - 30.0:
            return json.dumps({'error': 'stale request'})
    except:
        return json.dumps({'error': 'timestamp decoding failed'})

    if args['action'] == 'read':
        out = []
        with conn.cursor() as cur:
            cur.execute('SELECT content FROM secrets WHERE user_id=%s', [user_id])
            for record in cur:
                out.append(record[0])
        return json.dumps(out) + '\n'
    else:
        return json.dumps({'error': f'unknown action {args["action"]}'})

@app.route('/', methods=['GET'])
def index():
    return '<p>This is a REST API. Use your API key to access the secured endpoints.</p>'



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
