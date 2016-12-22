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