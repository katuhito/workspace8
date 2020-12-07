from flask import Flask
# from jinja2 import escape

# Flaskのインスタンスを作成
app = Flask(__name__)

# ルーティングの作成
@app.route('/')
def index():
    return "Hello, World!"

# 実行する
if __name__ == '__main__':
    app.run(host='0.0.0.0')
