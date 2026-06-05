from flask import Flask

app = Flask(__name__)

@app.route('/')
def paragraphs():
    return '''
        <h1>Paragraphs Example</h1>
        <p>This is a simple paragraph.</p>
        <p>This paragraph contains <strong>bold</strong> text and <em>italic</em> text.</p>
    '''



@app.route('/about')
def about():
    return '''
    <h1>About Page</h1>
    '''
if __name__ == '__main__':
    app.run(debug=True)
