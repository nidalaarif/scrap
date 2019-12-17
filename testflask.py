from flask import Flask


from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Nidal!'

@app.route('/about')
def about():
    return 'Hello, this is about page!'


if __name__ == '__main__':
    app.run()
