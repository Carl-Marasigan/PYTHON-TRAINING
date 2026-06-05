from flask import Flask
from markupsafe import escape

# The use of __name__ is so that Flasks knows where to look for files
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

app.run()