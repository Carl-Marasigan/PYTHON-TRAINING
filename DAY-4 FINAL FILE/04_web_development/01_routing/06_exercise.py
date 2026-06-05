"""
Exercise: Build Your Flask Website!

In this exercise, you're going to build a simple Flask application with multiple pages and routes.
Follow the steps below and modify the code to create your personalized website.

Instructions:
1. Create a Basic Flask App:
   Start by creating a basic Flask app that returns "Hello World!" when you visit the homepage.

2. Add a New Page:
   Add a new route `/new` that returns "Welcome to the New Page!".

3. User Profiles:
   Create a dynamic route `/user/<username>` that displays a personalized greeting for any username provided.
   For example, `/user/john` will return "User john".

4. Subpath Handling:
   Add a route `/path/<path:subpath>` that will capture any subpath after `/path/`.
   For example, `/path/page1` will return "Subpath page1".

5. Trailing Slash Challenge:
   Add two routes:
   - `/projects/` should display "The project page".
   - `/about` should display "The about page", but make sure `/about/` leads to a 404 error!

6. Multiple Routes for Home:
   Create multiple routes for the homepage (`/`, `/index/`, `/home/`),
   and make it greet users with their names if provided in the URL (e.g., `/home/john` will say "Hello john").

Testing Your Website:
1. Run your Flask app

2. Visit these pages in your browser:
   - http://127.0.0.1:5000
   - http://127.0.0.1:5000/new
   - http://127.0.0.1:5000/user/<yourname>
   - http://127.0.0.1:5000/path/<somepath>
   - http://127.0.0.1:5000/projects/
   - http://127.0.0.1:5000/about
"""


from flask import Flask


app = Flask(__name__)


@app.route("/")
@app.route("/index/")
@app.route("/home/")
@app.route("/home/<username>")

def home(username=None):
    if username:
        return f"Hello {username}"
    return "Hello World!"


# 2. Page
@app.route("/new")
def new_page():
    return "Welcome to the New Page!"


# 3. User Profiles
@app.route("/user/<username>")
def user_profile(username):
    return f"User {username}"


# 4. Subpath Handling
@app.route("/path/<path:subpath>")
def handle_subpath(subpath):
    return f"Subpath {subpath}"


# 5. Trailing Slash Challenge
@app.route("/projects/")
def projects():
    return "The project page"


#
#  404 error.
@app.route("/about", strict_slashes=True)
def about():
    return "The about page"


if __name__ == "__main__":
    # Runs the application on the local development server
    app.run(debug=True)

app.run()