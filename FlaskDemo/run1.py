from flask import Flask

app = Flask(__name__)

# ctrl + alt + l
# @app.route('/'):定义Flask中的路由


@app.route('/')
def inex():
    return "My First Flask Demo"


@app.route('/login')
def login():
    return "欢迎访问登录页面"


@app.route('/register')
def register():
    return "欢迎访问注册页面"


# 定义带参数的路由以及视图处理函数


@app.route('/show/<name>')
def show1(name):
    return "<h1>传递进来的参数为:%s</h1>" % name


# 路径:localhost:5000/show/wangwc/25
@app.route('/show/<name>/<age>')
def show2(name, age):
    return "姓名:%s,年龄:%d" % (name, age)



if __name__ == "__main__":
    '''运行Flask应用(启动flask服务)默认会在本机启动
    5000端口,允许使用http://localhost:5000/访问
    Flask的web应用'''
    app.run(debug=True)
