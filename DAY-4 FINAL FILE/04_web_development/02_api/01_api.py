from flask import  Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World"

@app.route("/me")
def me_api():
    return {
        "username": "username example",
        "theme": "theme example",
    }

@app.route("/users")
def users_api():
    users = ["John", "Fezz", 'Kilma']
    return [user for user in users]

app.run()