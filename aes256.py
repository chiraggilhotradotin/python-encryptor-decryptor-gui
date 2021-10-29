import base64
from hashlib import md5
from Cryptodome import Random
from Cryptodome.Cipher import AES


BLOCK_SIZE = 16
KEY_LEN = 32
IV_LEN = 16

def encrypt(raw, passphrase):
    salt = Random.new().read(8)
    key, iv = __derive_key_and_iv(passphrase, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return base64.b64encode(b'Salted__' + salt + cipher.encrypt(__pkcs7_padding(raw)))

def decrypt(enc, passphrase):
    ct = base64.b64decode(enc)
    salted = ct[:8]
    if salted != b'Salted__':
        return ""
    salt = ct[8:16]
    key, iv = __derive_key_and_iv(passphrase, salt)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return __pkcs7_trimming(cipher.decrypt(ct[16:]))

def __pkcs7_padding(s):
    s_len = len(s.encode('utf-8'))
    s = s + (BLOCK_SIZE - s_len % BLOCK_SIZE) * chr(BLOCK_SIZE - s_len % BLOCK_SIZE)
    return bytes(s, 'utf-8')

def __pkcs7_trimming(s):
    return s[0:-s[-1]]

def __derive_key_and_iv(password, salt):
    d = d_i = b''
    enc_pass = password.encode('utf-8')
    while len(d) < KEY_LEN + IV_LEN:
        d_i = md5(d_i + enc_pass + salt).digest()
        d += d_i
    return d[:KEY_LEN], d[KEY_LEN:KEY_LEN + IV_LEN]