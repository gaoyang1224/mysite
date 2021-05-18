"""
开发写的后端接口
"""
import time

# SECRET_KEY = 'FFSFSF'


from flask import Flask, request, session

server = Flask(__name__)
server.config['SECRET_KEY'] = 'FFSFSF'

# users = []

@server.route('/')
def index():
    user = session.get('user', '')
    if  user == 'yw':
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
        # users.append(username)
        session['user'] = username
        # 数据库
        return {
            "msg": "login success"
        }
    return {"msg": "username or password is error"}

if __name__ == '__main__':
    server.run(debug=True)

