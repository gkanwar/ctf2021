from Crypto.PublicKey import RSA

END_MARKER = b'-----END PUBLIC KEY-----'

with open('big_primes.txt', 'rb') as f:
    key_text, c_text = f.read().split(END_MARKER)
    key_text += END_MARKER
key = RSA.import_key(key_text)
c = int(c_text.split(b' = ')[-1].strip())

# floating-point cube roots should fail here, but binary search works
def cube_root(c):
    m_low = 0
    m_high = c
    while True:
        m_mid = (m_low + m_high) // 2
        check = m_mid**3
        if check > c:
            m_high = m_mid
        elif check < c:
            m_low = m_mid
        else:
            return m_mid
m = cube_root(c)

print(m.to_bytes(256, 'big'))
