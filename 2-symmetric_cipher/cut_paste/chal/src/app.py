import logging
import os

from Crypto.Cipher import AES
from flask import Flask, render_template, request, redirect, make_response

from secret import FLAG


key = os.urandom(32)

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

def pad(message: bytes):
    return message + b'\0' * (16 - (len(message) % 16))

def unpad(message: bytes):
    return message.rstrip(b'\0')

def encrypt(plain: bytes):
    aes = AES.new(key, AES.MODE_ECB)
    return aes.encrypt(pad(plain))

def decrypt(cipher: bytes):
    aes = AES.new(key, AES.MODE_ECB)
    return unpad(aes.decrypt(cipher))

def is_username_valid(username: str):
    if '=' in username or '&' in username:
        return False
    return True

def userdata2token(userdata: dict[str, str | int]):
    plain_token = '&'.join(f'{key}={value}' for key, value in userdata.items())
    return encrypt(plain_token.encode()).hex()

def token2userdata(token: str):
    try:
        plain_token = decrypt(bytes.fromhex(token)).decode()
    except:
        raise ValueError

    userdata = dict(map(lambda x: x.split('='), plain_token.split('&')))
    return {
        'username': userdata.get('username'), 
        'money': int(userdata.get('money'))
    }

@app.get('/')
def index():
    token = request.cookies.get('token')
    if token is not None:
        return redirect('/dashboard')
    return render_template('index.html')

@app.post('/login')
def login():
    token = request.cookies.get('token')
    if token is not None:
        return redirect('/dashboard')
    
    username = request.form.get('username')
    if (username is None) or (username == ''):
        return redirect('/')
    
    token = userdata2token({
        'username': username, 
        'money': 100
    })

    response = make_response(redirect('/dashboard'))
    response.set_cookie('token', token, max_age=60 * 60 * 24)
    return response

@app.get('/dashboard')
def dashboard():
    token = request.cookies.get('token')
    if token is None:
        return redirect('/')

    try:
        userdata = token2userdata(token)
    except ValueError:
        response = make_response('`token` Value Error')
        response.set_cookie('token', '', expires=0)
        return response

    return render_template('dashboard.html', userdata=userdata)

@app.get('/get-flag')
def get_flag():
    token = request.cookies.get('token')
    if token is None:
        return redirect('/')

    try:
        userdata = token2userdata(token)
    except ValueError:
        response = make_response({
            'status': 'failed', 
            'msg': '`token` Value Error'
        })
        response.set_cookie('token', '', expires=0)
        return response

    if userdata['money'] < 10000:
        return {'status': 'success', 'msg': 'Your money is not enough to be the flag !'}
    else:
        return {'status': 'success', 'msg': f'Flag : <code>{FLAG}</code>'}


@app.get('/logout')
def logout():
    token = request.cookies.get('token')
    if token is None:
        return redirect('/')
    
    response = redirect('/')
    response.set_cookie('token', '', expires=0)
    return response


