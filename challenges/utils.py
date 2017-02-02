import binascii
from Crypto import Random
from Crypto.Cipher import AES

def raw_to_b64(raw):
    return binascii.b2a_base64(raw).rstrip()

def b64_to_raw(b64_string):
    return binascii.a2b_base64(b64_string)

def raw_to_hex(raw):
    return binascii.hexlify(bytes(raw)).decode('utf-8')

def raw_to_ascii(raw):
    return ''.join([chr(b) for b in raw])

def hex_to_raw(hex_string):
    return binascii.unhexlify(hex_string)

def ascii_to_raw(ascii_string):
    # If ascii_string is aa list it will be joined until it is no longer, e.g.
    # a list of lists of strings will correctly be converted into a string USEFUL IN CHALLENGE 6
    while isinstance(ascii_string, list):
        ascii_string = ''.join([element for element in ascii_string])
    if isinstance(ascii_string, bytes):
        return ascii_string
    return bytes(ascii_string, 'utf-8')

def pad_with_pkcs7(msg, block_size=16):
    msg = ascii_to_raw(msg)
    padding = block_size - (len(msg) % block_size)
    msg = msg + bytes(chr(padding) * padding, 'ascii')
    return msg

def unpad_with_pkcs7(padded_plaintext):
    padded_plaintext = ascii_to_raw(padded_plaintext)
    last_byte = padded_plaintext[-1]
    pad = padded_plaintext[-last_byte:]
    if len(pad) != last_byte or [c for c in pad if c != last_byte]:
        raise ValueError("Bad padding. Last_byte = {}".format(hex(last_byte)))
    
    return padded_plaintext[:-last_byte]

def aes_cbc_encrypt(key, msg, iv=''):
    block_size = len(key)
    msg = pad_with_pkcs7(msg)
    iv = iv or Random.new().read(block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(msg)

def aes_cbc_decrypt(key, cpt, iv=''):
    block_size = len(key)
    if not iv:  # if iv is not given, consider it the first block of cpt
        iv, cpt = cpt[:block_size], cpt[block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    msg = cipher.decrypt(cpt)
    return unpad_with_pkcs7(msg)