#!/usr/bin/env python3
from Crypto.Cipher import ARC4
from flask import request, render_template, redirect, url_for
from . utils import *


KEY = 'ayyyyyyy lmaoooo'
FLAG1 = 'WHAT ARE WE HAVING FOR LUNCH?'
FLAG2 = 'MERRY XMAS :)'
TOKEN = 'username={}&admin=0&flag2='+FLAG2

def level1():

    if request.method == 'POST':

        username = request.form['username']
        cipher = ARC4.new(KEY)
        token = cipher.encrypt(TOKEN.format(username).encode())
        return redirect(url_for('stream_ciphers_level1', token=raw_to_hex(token)))

    elif request.method == 'GET':

        cpt = request.args.get('token', None)

        if cpt is None:
            return render_template('single_input.html', title='RC4 token', msg='Please sign up:', action=url_for('stream_ciphers_level1'), input_msg='Username', input='username')

        else:

            cipher = ARC4.new(KEY)
            msg = cipher.decrypt(hex_to_raw(cpt)).decode()
            d = {parameter.split('=')[0]:parameter.split('=')[1] for parameter in msg.split('&')}

            flag = FLAG1 if d['admin'] == '1' else ''

            return render_template('generic.html', title='RC4 token', msg="Hello {}!".format(d['username']), flag=flag, flag_error="Only admins can see the flag, but you're not an admin are you? (admin=0)")