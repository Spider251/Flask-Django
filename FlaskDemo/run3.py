from flask import Flask, render_template

app = Flask(__name__)


@app.route('/01-temp')
def temp():
    # 渲染01-temp.html模板并响应给客户端
    str = render_template('01-temp.html', name='Rapwang', age=35)
    print(str)
    return str


@app.route('/homework')
def homework():
    # 渲染01-temp.html模板并响应给客户端
    str = render_template('01-homework.html', song='<<绿光>>', write='宝强', zuoqu='乃亮', singer='羽凡')
    return str


if __name__ == "__main__":
    app.run(debug=True)
