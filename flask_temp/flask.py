from flask import Flask, render_template
app = Flask(__name__)



@app.route('/')
def hello_user():
    return 'hello world'

@app.route('/about')
def about():
    return 'This is about page'

@app.route('/contact')
def contact():
    return 'This is contact page'



if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')