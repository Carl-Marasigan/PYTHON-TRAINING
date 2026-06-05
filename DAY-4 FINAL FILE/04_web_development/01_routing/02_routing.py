from flask import Flask

# The use of __name__ is so that Flasks knows where to look for files
app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route('/new')
def hello():
    return 'New Page!'

app.run()