from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder="sta", static_url_path="/s")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/list')
def list():
    return render_template('list.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    app.run(debug=True)
