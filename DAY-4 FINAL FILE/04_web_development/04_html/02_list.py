from flask import Flask

app = Flask(__name__)

@app.route('/')
def list():
    return '''
        <h1>Lists Example</h1>
        <h2>Unordered List</h2>
        <ul>
            <li>Item 1</li>
            <li>Item 2</li>
            <li>Item 3</li>
        </ul>
        
        <h2>Ordered List</h2>
        <ol>
            <li>First item</li>
            <li>Second item</li>
            <li>Third item</li>
        </ol>
    '''

if __name__ == '__main__':
    app.run(debug=True)
