"""
Note: Files are expected to be in `./templates/`
"""

from flask import render_template, Flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/variable')
def home():
    name = "Universe"
    return render_template('variable.html', name=name)

@app.route('/status')
def status():
    logged_in = True
    return render_template('conditional.html', logged_in=logged_in)

@app.route('/items')
def items():
    items = ['Apple', 'Banana', 'Cherry']
    return render_template('items.html', items=items)

@app.route('/profile')
def profile():
    user_info = {
        'name': 'Carl',
        'location': 'Calamba'
    }
    return render_template('profile.html', user=user_info)

app.run()