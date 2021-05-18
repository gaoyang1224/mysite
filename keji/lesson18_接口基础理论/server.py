"""
开发写的后端接口
"""
from flask import Flask

server = Flask(__name__)

@server.route('/')
def index():
    return {"msg": "success", "data": "welecome to py36"}

@server.route('/login')
def login():
    return """<p style="color:red">login</p>"""

if __name__ == '__main__':
    server.run(debug=True)

