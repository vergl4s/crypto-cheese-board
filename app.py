#!/usr/bin/env python3
import challenges
import sys

from flask import Flask, request, make_response, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')

@app.route("/stream/level1", methods=['GET', 'POST'])
def stream_ciphers_level1():
	return challenges.stream_ciphers.level1()

@app.route("/padding_oracle/level1", methods=['GET', 'POST'])
def padding_oracle_level1():
	return challenges.padding_oracles.level1()

@app.route("/padding_oracle/level2", methods=['GET', 'POST'])
def padding_oracle_level2():
	return challenges.padding_oracles.level2()

@app.route("/digital_signatures/level1", methods=['GET'])
def digital_signatures_level1():
	return challenges.signatures.level1()

if __name__ == '__main__':
    addr = sys.argv[1] if len(sys.argv) > 1 else '127.0.0.1'
    app.run(addr)