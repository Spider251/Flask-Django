import os
import datetime
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/01-file', methods=['GET', 'POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        # 处理上传的文件
        # 1.得到上传的文件
        f = request.files['uimg']
        # 2.将文件保存进指定的目录处[相对路径]
        # print('文件名' + f.filename)
        # f.save('static/' + f.filename)
        # 3.将文件保存进指定的目录[绝对路径]
        # 获取当前目录的所在目录名
        basedir = os.path.dirname(__file__)
        # print('当前文件所在目录的绝对路径:'+basedir)
        # 获取当前的时间拼成字符串,再拼上扩展名
        fttime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        # 获取文件扩展名(xxx.jpg)
        ext = f.filename.split('.')[1]
        filename = fttime + "." + ext
        upload_path = os.path.join(basedir, 'static', filename)
        # print("完整的上传路径"+upload_path)
        f.save(upload_path)
        return "Save Ok"


if __name__ == '__main__':
    app.run(debug=True)
