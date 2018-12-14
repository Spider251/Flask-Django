import os
import datetime
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/01-file', methods=['GET', 'POST'])
def file_views():
    if request.method == 'GET':
        return render_template('01-file.html')
    else:
        f = request.files['uimg']
        basedir = os.path.dirname(__file__)
        fttime = datetime.datetime.now().strftime("%Y%m%d%H%M%S%f")
        ext = f.filename.split('.')[1]
        filename = fttime + "." + ext
        upload_path = os.path.join(basedir, 'static/upload', filename)
        f.save(upload_path)
        return "Save Ok"


if __name__ == '__main__':
    app.run(debug=True)
