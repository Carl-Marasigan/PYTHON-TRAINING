from flask import Flask

# The use of __name__ is so that Flasks knows where to look for files
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

# Removing trailing will allow `/projects` only
@app.route('/projects/')
def projects():
    return 'The project page'

# Adding a trailing '/' will cause 404
@app.route('/about')
def about():
    return 'The about page'

app.run()