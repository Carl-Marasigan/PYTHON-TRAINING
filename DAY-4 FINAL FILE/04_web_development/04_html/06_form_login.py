from flask import Flask, request

app = Flask(__name__)

@app.get('/login')
def login_get():
    return '''
        <form method="post" action="/login">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" required><br>
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" required><br>
            <label for="email">Email:</label>  <!-- Added email field -->
            <input type="email" id="email" name="email" required><br>
            <input type="submit" value="Login">
        </form>
    '''

@app.post('/login')
def do_the_login():
    # Here you would handle the login logic, e.g., checking credentials
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']

    # Check if the credentials are correct
    if not (username == "carl" and password == "carl" and email == "cjmarasigan@gmail.com"):
        return 'Invalid username or password!', 401

    return 'Login successful!'

if __name__ == '__main__':
    app.run()
