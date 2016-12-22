#!/usr/bin/env python3
import challenges
import sys

from flask import Flask, request, make_response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/stream/rc4", methods=['POST', 'GET'])
def rc4():
	return challenges.stream_ciphers.rc4()

@app.route("/len_extension", methods=['GET'])
def len_extension():
	return challenges.signatures.length_extension()

if __name__ == '__main__':
    addr = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    app.run(addr)