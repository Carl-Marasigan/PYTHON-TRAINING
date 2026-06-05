from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login')
def login_function():
    return 'Login Page'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s Profile Page'

@app.route('/home/')
def home():
    # Using url_for() which is based on function name
    return f'''
        <h1>Home Page</h1>
        <a href="{url_for('login_function')}">Login</a><br>
        <a href="{url_for('profile', username='John Doe')}">John's Profile</a>
    '''

if __name__ == '__main__':
    app.run()
