#!/usr/bin/env python3
from Crypto.Cipher import AES
from Crypto import Random
from flask import request, render_template, redirect, url_for, abort
from . utils import *


KEY = 'ayyyyyyy lmaoooo'
FLAG1 = 'WHAT ARE WE HAVING FOR LUNCH?'
TOKEN = 'username={}&admin=0&flag1='+FLAG1

def main_page():
    return render_template('single_input.html', title='Padding oracle', msg='Please sign up:',  input_msg='Username', input='username')


def verify_cpt(raw_cpt):
    if raw_cpt is None:
        return main_page()

    else:

        msg = raw_to_ascii(aes_cbc_decrypt(KEY, raw_cpt))
        
        try:

            d = {parameter.split('=')[0]:parameter.split('=')[1] for parameter in msg.split('&')}
            flag = FLAG1 if 'admin' in d and d['admin'] == '1' else ''
            return render_template('generic.html', title='Padding oracle', msg="Hello {}!".format(d['username']), flag=flag, flag_error="Only admins can see the flag, but you're not an admin are you? (admin=0)")

        except Exception:
            return main_page()

def level1():

    if request.method == 'POST':

        username = request.form['username']
        cpt = raw_to_hex(aes_cbc_encrypt(KEY, TOKEN.format(username)))
        return redirect(url_for('padding_oracle_level1', token=cpt))

    elif request.method == 'GET':

        cpt = request.args.get('token', None)
        cpt = hex_to_raw(cpt) if cpt else None
        return verify_cpt(cpt)

def level2():

    if request.method == 'POST':

        username = request.form['username']
        cpt = raw_to_b64(aes_cbc_encrypt(KEY, TOKEN.format(username)))
        return redirect(url_for('padding_oracle_level2', token=cpt))

    elif request.method == 'GET':

        cpt = request.args.get('token', None)
        cpt = b64_to_raw(cpt) if cpt else None
        return verify_cpt(cpt)
