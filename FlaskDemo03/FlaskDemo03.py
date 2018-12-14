from flask import Flask, render_template, url_for, request

app = Flask(__name__,
            template_folder='muban')


@app.route('/')
def hello_world():
    return 'Hello World!'

# 访问路径　http://localhost:5000/01-static
@app.route('/01-static')
def static_views():
    url = url_for('static',filename='images/b05.jpg')
    print(url)
    return render_template('01-static.html')
# 访问路径　http://localhost:5000/02-parent
@app.route('/02-parent')
def parent_views():
    return render_template('02-parent.html')

# 访问路径　http://localhost:5000/03-child
@app.route('/03-child')
def child_views():
    return render_template('03-child.html')

# 访问路径　http://localhost:5000/04-request
@app.route('/04-request')
def request_views():
    # print(dir(request))
    # 获取请求方案(协议)
    scheme = request.scheme
    # 获取请求方式
    method = request.method
    # 获取get请求方式的请求数据
    args = request.args
    # 获取post请求方式的请求数据
    form = request.form
    # 获取cookies中的信息
    cookies = request.cookies
    # 获取请求路径(具体资源，不带参数)
    path = request.path
    # 获取请求路径(具体资源，带参数)
    full_path = request.full_path
    # 获取请求路径(完整路径)
    url = request.url
    # 获取所有的请求消息头
    headers = request.headers
    print(headers)
    # 获取　User-Agent 请求消息头信息
    ua = request.headers['User-Agent']
    # 获取　Referer 请求消息头的信息
    referer = request.headers.get('Referer','')
    return render_template('04-request.html',params= locals())


# 访问地址　http://localhost:5000/05-form-get
@app.route('/05-form-get')
def form_get():
    return render_template('05-form-get.html')

#访问地址　http://localhost:5000/06-get
@app.route('/06-get')
def get_views():
    #print(request.args)

    uname = request.args['uname']
    upwd = request.args['upwd']

    print('uname:%s,upwd:%s' % (uname,upwd))

    return "Get Success"

#访问地址　http://localhost:5000/07-form-post
@app.route('/07-form-post',methods=['GET','POST'])
def form_post():
    if request.method == 'GET':
        return render_template('07-post.html')
    else:
        uname = request.form['uname']
        upwd = request.form['upwd']
        uemail = request.form['uemail']
        tname = request.form['tname']
        print("用户名:%s,密码:%s,邮箱:%s,真实姓名:%s" % (uname, upwd, uemail, tname))
        return "Post OK"

#访问地址　http://localhost:5000/07-post
# @app.route('/07-post',methods=['POST'])
# def post_views():
#     uname = request.form['uname']
#     upwd = request.form['upwd']
#     uemail = request.form['uemail']
#     tname = request.form['tname']
#     print("用户名:%s,密码:%s,邮箱:%s,真实姓名:%s" % (uname,upwd,uemail,tname))
#     return "Post OK"

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
