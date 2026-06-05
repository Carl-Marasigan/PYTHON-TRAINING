
from flask import Flask

# The use of __name__ is so that Flasks knows where to look for files
app = Flask(__name__)

@app.route("/")
@app.route('/index/')
@app.route('/home/')
@app.route('/home/<name>')
@app.route('/index/<name>')
def index(name=None):
    return f"Hello {name}"

app.run()