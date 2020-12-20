# ログインなどユーザに関する処理をまとめる
from flask import Flask, session, redirect
from functions import wraps

# ユーザーとパスワードの一覧
USER_LOGIN_LIST = {
    'taro': 'aaa',
    'jiro': 'bbb',
    'sabu': 'ccc',
    'siro': 'ddd',
    'goro': 'eee',
    'muro': 'fff',
}

# ログインしているかの確認
def is_login(form):
    return 'login' in session

# ログインを試行する
def try_login(form):
    user = form.get('user', '')
    password = form.get('pw', '')
    # パスワードチェック
    if user not in USER_LOGIN_LIST: return False
    if USER_LOGIN_LIST[user] != password:
        return False
    session['login'] = user
    return True

# ユーザーを得る
def get_id():
    return session['login'] if is_login() else '未ログイン'

# 全ユーザーの情報を得る
def get_allusers():
    return [ u for u in USER_LOGIN_LIST ]

# ログアウトする
def try_logout():
    session.pop('login', None)

# ログイン必須を処理するデコレータを定義
def login_required(func):
    @wraps(func)
    def wrapper(*args, **kargs):
        if not is_login():
            return redirect('/login')
        return func(*args, **kwargs)
    return wrapper
    