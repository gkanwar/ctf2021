from Crypto.Hash import HMAC, SHA256
import flag
import random

key = random.getrandbits(1024).to_bytes(1024//8, 'big')
hk = SHA256.new()
hk.update(key)
key_digest = hk.hexdigest()

pastes = {
    ('flag', 1): flag.flag,
    ('hello', 0): 'Hello, world!',
    ('to_be', 0): '''To be, or not to be, that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune,
Or to take arms against a sea of troubles
And by opposing end them.''',
    ('quine', 0): '''exec(s:='print("exec(s:=%r)"%s)')'''
}
login = None

def parse_login(token):
    try:
        nonce, is_admin, hmac = token.split('|')
        s = nonce + '|' + is_admin
        h = HMAC.new(key, digestmod=SHA256)
        h.update(s.encode())
        if h.hexdigest() != hmac:
            print('Bad HMAC')
            return None
        return (nonce, int(is_admin))
    except:
        print('Ill-formatted token')
        return None

def generate_token():
    nonce = random.getrandbits(128).to_bytes(128//8, 'big').hex()
    is_admin = 0
    s = nonce + '|' + str(is_admin)
    h = HMAC.new(key, digestmod=SHA256)
    h.update(s.encode())
    hmac = h.hexdigest()
    return s + '|' + hmac


print('Welcome to PastePad.\n')
print(f'''== Info ==
 - Version: v13.3.7
 - Key digest: {key_digest}
''')
while True:
    if login is None:
        print('\nNot logged in. Options:')
        print('[1] Generate guest login token.')
        print('[2] Login.')
        print('[3] Quit.')
        i = input('Choice: ')
        try:
            i = int(i)
            if i == 1:
                print(generate_token())
            elif i == 2:
                token = input('Token: ').strip()
                login = parse_login(token)
                if login is None:
                    print('Login failed.')
            elif i == 3:
                print('Goodbye')
                break
            else:
                print('Invalid choice.')
        except:
            print('Invalid choice.')
    else:
        print(f'\nLogged in with token {login}. Options:')
        print('[1] Show pastes.')
        print('[2] Quit.')
        i = input('Choice: ')
        try:
            i = int(i)
            if i == 1:
                for p,text in pastes.items():
                    if login[1] >= p[1]:
                        print(f'== {p[0]} ==')
                        print(text)
                        print()
            elif i == 2:
                print('Goodbye')
                break
            else:
                print('Invalid choice.')
        except:
            print('Invalid choice.')
            
