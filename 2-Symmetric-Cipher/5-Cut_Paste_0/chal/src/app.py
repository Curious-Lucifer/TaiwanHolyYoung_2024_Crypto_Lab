"""Cut & Paste 的後端."""

import logging

from flask import Flask, render_template, request, redirect, make_response
import secret  # pylint: disable=import-error
import utils


app = Flask(__name__)
logging.getLogger('werkzeug').setLevel(logging.ERROR)


@app.get('/')
def index():
    """確認是否已經登入，如果已經登入就重導向到 /dashboard，沒有的話就顯示登入介面."""

    token = request.cookies.get('token')
    if token is not None:
        return redirect('/dashboard')
    return render_template('index.html')


@app.post('/login')
def login():
    """處理登入."""

    token = request.cookies.get('token')
    if token is not None:
        return redirect('/dashboard')

    username = request.form.get('username')
    if (username is None) or (not username):
        return redirect('/')

    token = utils.userdata2token({'username': username, 'money': 100})

    response = make_response(redirect('/dashboard'))
    response.set_cookie('token', token, max_age=60 * 60 * 24)
    return response


@app.get('/dashboard')
def dashboard():
    """顯示目前使用者的相關資料."""

    token = request.cookies.get('token')
    if token is None:
        return redirect('/')

    try:
        userdata = utils.token2userdata(token)
    except ValueError:
        response = make_response('Invalid token')
        response.set_cookie('token', '', expires=0)
        return response

    return render_template('dashboard.html', userdata=userdata)


@app.get('/get-flag')
def get_flag():
    """處理購買 flag 的邏輯."""

    token = request.cookies.get('token')
    if token is None:
        return redirect('/')

    try:
        userdata = utils.token2userdata(token)
    except ValueError:
        response = make_response({'status': 'failed',
                                  'msg': 'Invalid token'})
        response.set_cookie('token', '', expires=0)
        return response

    if userdata['money'] < 10000:
        return {'status': 'success',
                'msg': 'Your money is not enough to buy the flag !'}
    return {'status': 'success', 'msg': f'Flag : <code>{secret.FLAG}</code>'}


@app.get('/logout')
def logout():
    """登出."""

    token = request.cookies.get('token')
    if token is None:
        return redirect('/')

    response = redirect('/')
    response.set_cookie('token', '', expires=0)
    return response
