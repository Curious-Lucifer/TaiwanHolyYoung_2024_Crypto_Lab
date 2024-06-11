import logging

from flask import Flask, render_template


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.route('/')
def index():
    return render_template('ascii-bin-dec-hex.html')


@app.route('/encoding')
def encoding():
    return render_template('encoding.html')


@app.route('/get-hash-flag')
def get_hash_flag():
    return render_template('get-hash-flag.html')


@app.route('/aes/aes')
def aes():
    return render_template('aes.html')


@app.route('/aes/aes-ecb-mode')
def aes_ecb_mode():
    return render_template('aes-ecb-mode.html')


@app.route('/aes/xor')
def xor():
    return render_template('xor.html')


@app.route('/aes/aes-cbc-mode')
def aes_cbc_mode():
    return render_template('aes-cbc-mode.html')


@app.route('/rsa/rsa')
def rsa():
    return render_template('rsa.html')


@app.route('/rsa/rsa-signature')
def rsa_signature():
    return render_template('rsa-signature.html')

