from flask import Flask, render_template
app = Flask(__name__)



@app.route('/<username>')
def hello_user(username):
    return render_template('index.html', user=username)

@app.route('/about')
def about():
    return 'This is about page'

@app.route('/contact')
def contact():
    return 'This is contact page'



if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0')