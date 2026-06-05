"""
Exercise: Create Your Own API Endpoints!

In this exercise, you'll build a simple Flask application with several API endpoints. The goal is to practice returning JSON responses and basic routing.

Instructions:

1. Basic Homepage:
   Create a route (`/`) that returns a simple text message "Hello World".

2. Create an API for "Me":
   Create a route `/me` that returns a JSON object with two fields:
   - "username": The string "username example"
   - "theme": The string "theme example"

3. Create an API for "Users":
   Create a route `/users` that returns a list of users in JSON format. The list should contain at least three names (e.g., "John", "Fezz", "Kilma").

Bonus Challenge:
- Add another route `/users/<username>` that returns the username of the user if it exists in the list. If the user is not found, return a 404 error with a message like "User not found".

Testing Your API:
1. Run your Flask app using the command:
   python app.py

2. Visit these endpoints in your browser or through a tool like Postman:
   - http://127.0.0.1:5000
   - http://127.0.0.1:5000/me
   - http://127.0.0.1:5000/users
   - http://127.0.0.1:5000/users/<username> (Test with different usernames like "John", "Fezz", and "Kilma")
"""

from flask import Flask, abort

app = Flask(__name__)

# Moved the list here so both routes can access it
users = ["John", "Fezz", "Kilma"]


@app.route("/")
def index():
    return "Hello Carl"


@app.route("/me")
def me_api():
    return {
        "username": "username example",
        "theme": "theme example",
    }


@app.route("/users")
def users_api():
    return [user for user in users]


# BONUS CHALLENGE
@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return f"User: {username}"
    print(f"User not found: {username}")
    return None
    # abort(404)


app.run()