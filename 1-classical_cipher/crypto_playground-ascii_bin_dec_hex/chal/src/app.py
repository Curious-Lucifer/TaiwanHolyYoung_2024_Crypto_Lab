import logging
from hashlib import sha256

from flask import Flask, render_template, request


app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


@app.get('/')
def index():
    return render_template('ascii-bin-dec-hex.html')


@app.get('/encoding')
def encoding():
    return render_template('encoding.html')


@app.get('/get-hash-flag')
def get_hash_flag():
    return render_template('get-hash-flag.html')


@app.get('/aes/aes')
def aes():
    return render_template('aes.html')


@app.get('/aes/aes-ecb-mode')
def aes_ecb_mode():
    return render_template('aes-ecb-mode.html')


@app.get('/aes/xor')
def xor():
    return render_template('xor.html')


@app.get('/aes/aes-cbc-mode')
def aes_cbc_mode():
    return render_template('aes-cbc-mode.html')


@app.get('/rsa/rsa')
def rsa():
    return render_template('rsa.html')


@app.get('/rsa/rsa-signature')
def rsa_signature():
    return render_template('rsa-signature.html')


@app.post('/calc-sha256')
def calc_sha256():
    if request.is_json:
        data = request.json
        if 'msg' not in data:
            return {'status': 'failed', 'msg': 'no `msg`'}
        return {'status': 'success', 'msg': sha256(data['msg'].encode()).hexdigest()}
    return {'status': 'failed', 'msg': 'request no json'}

