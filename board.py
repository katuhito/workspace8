from flask import Flask, request, redirect
import os
app = Flask(__name__)

# データの保存先
DATAFILE = './board-data.txt'

# ルートにアクセスしたとき
@app.route('/')
def index():
    msg = 'まだ書き込みはありません。'
    # 保存データを読み込む
    if os.path.exists(DATAFILE):
        with open(DATAFILE, 'rt') as f:
            msg = f.read()
    # メッセージボードと投稿フォーム
    return """
    <html><body>
    <h1>メッセージボード</h1>
    <div style="background-color:yellow;padding:3em;">
    {0}</div>
    <h3>ボードの内容を更新</h3>
    <form action="/write" method="POST">
        <textarea name="msg" rows="6" cols="60"></textarea><br/>
        <input type="submit" value="書き込み">
    </form>
    </body></html>
    """.format(msg)

# POSTメソッドで/writeにアクセスしたとき
@app.route('/write', methods=['POST'])
def write():
    # データファイルにメッセージを保存
    if 'msg' in request.form:
        msg = str(request.form['msg'])
        with open(DATAFILE, 'wt') as f:
            f.write(msg)
        # ルートページにリダイレクト
        return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    
