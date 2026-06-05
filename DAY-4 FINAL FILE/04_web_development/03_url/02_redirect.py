from flask import redirect, url_for, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    return "Please login"

app.run()