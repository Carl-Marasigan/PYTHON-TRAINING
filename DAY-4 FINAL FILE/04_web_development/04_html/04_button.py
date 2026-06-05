from flask import Flask

app = Flask(__name__)

@app.route('/')
def button():
    return '''
        <h1>Button Example</h1>
        <button>Click Me!</button>
        <a href="/">Back to Home</a>
    '''

if __name__ == '__main__':
    app.run(debug=True)
