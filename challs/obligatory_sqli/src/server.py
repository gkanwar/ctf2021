from flask import Flask, request
import flag
import psycopg2
import re
import sys
import time

app = Flask(__name__)

@app.route('/flag', methods=['GET'])
def get_secrets():
    if 'username' not in request.args:
        return 'Missing required parameter "username"', 400
    if 'password' not in request.args:
        return 'Missing required parameter "password"', 400
    username, password = request.args['username'], request.args['password']
    if '--' in username or '--' in password:
        return 'Bad character sequence "--" not allowed!', 403
    
    conn = psycopg2.connect(database="postgres", user="web", password="dummypassword", host="db")
    with conn.cursor() as cur:
        try:
            cur.execute(f"SELECT id FROM users WHERE username='{username}' AND password='{password}'")
            i = cur.fetchone()
            if i is None:
                return 'User not found or wrong password'
            if i[0] == 1:
                return f'Welcome admin, have a flag: {flag.flag}'
            else:
                return f'Dont know how you logged in as another user, but nothing to see here...'
        except Exception as e:
            return f'SQL query failed with error {e}', 500

@app.route('/', methods=['GET'])
def index():
    return '''
<html>
<head><title>Flag Store Server</title></head>
</html>
<body>
<div style="margin:auto;width:450px">
<p>Welcome to the Flag Store Server. If you have an account with us, please log in to access your flags.<p>

<form action="/flag" method="get">
<div>Username: <input type="text" name="username"/></div>
<div>Password: <input type="password" name="password"/></div>
<div style="margin:auto;width:100px">
<input type="submit" name="submit"/>
</div>
</form>
</div>
</body>
</html>
'''



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
