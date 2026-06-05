from flask import Flask
from markupsafe import escape

# The use of __name__ is so that Flasks knows where to look for files
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
app.run()