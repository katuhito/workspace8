from flask import Flask, request
app = Flask(__name__)

# サーバールートへアクセスがあったとき
@app.route('/')
def index():
    # フォームを表示する
    return """
    <html><body>
    <form action="/hello" method="GET">
        名前：<input type="text" name="name">
        <input type="submit" value="送信">
    </form>
    </body></html>
    """

# /helloへアクセスがあったとき
@app.route('/hello')
def hello():
    # nameのパラメーターを得る
    name = request.args.get('name')
    if name is None: name = '名無し'
    # 自己紹介を自動生成
    return """
    <h1>{0}さん、こんにちは！</h1>
    """.format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    