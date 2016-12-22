#!/usr/bin/env python3
import binascii
from flask import request, render_template
import hashlib
from . utils import *

KEY = b'ayyyyyyyyyyy lmaao'
FLAG = 'Y SO SECRET?'

def sign(msg):
    return hashlib.sha1(KEY + msg).hexdigest()

def length_extension():

    msg = request.args.get('msg')
    tag = request.args.get('tag')

    if msg is None or tag is None:

        msg = b"username=User1&admin=False"
        hexmsg = raw_to_hex(msg)
        tag = sign(msg)
        return render_template('generic.html',
            title='Length extension',
            msg="You seem to have no SSO token. To authenticate, click here",
            links=[('?tag={}&msg={}'.format(tag, hexmsg), msg.decode())],)

    else:

        msg = hex_to_raw(msg)
        d = {parameter.split('=')[0]:parameter.split('=')[1] for parameter in raw_to_ascii(msg).split('&')}

        if tag == sign(msg):
            print(d['admin'])
            flag = FLAG if d['admin'] == "True" else ""

            return render_template('generic.html',
                title='Length extension',
                msg="Hello {}!".format(d['username']), 
                flag=flag, 
                flag_error="Only admins can see the flag, but you're not an admin are you? (admin=False)",)

        return render_template('generic.html', title='Signature does not match'), 500
