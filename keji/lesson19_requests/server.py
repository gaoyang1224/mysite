"""
开发写的后端接口
"""
import time

from flask import Flask, request

server = Flask(__name__)

@server.route('/')
def index():
    # 获取 token
    token = request.args.get('t', '')
    if not token:
        return {"msg": "login first, get token"}
    user = token.split('@')[0]
    token_start_time = token.split('@')[1]
    if user == 'yw' and time.time() - float(token_start_time) < 600:
        return {"msg": "success", "data": "100wan"}
    return {"msg": "login first, get token"}


@server.route('/login')
def login():
    """返回token给前端"""
    # 获取query string :url 当中的参数
    username = request.args.get('username')
    password = request.args.get("password")

    ts = str(time.time())
    print(ts)

    if username == 'yw' and password == '123456':
        # 数据库
        return {
            "token": username + "@" + ts,
            "id": 1,
            "username": "yuz",
        }
    return {"msg": "username or password is error"}

if __name__ == '__main__':
    server.run(debug=True)

