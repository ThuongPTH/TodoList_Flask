from flask import Flask, redirect, url_for, render_template, request
from json import *
import Function

# tạo 1 biến app
app = Flask(__name__)

with open('user.json', 'r',  encoding='utf-8') as f:
    data_user = load(f)

# tạo đường dẫn url /login
@app.route('/login', methods =['POST', 'GET'])
def login():
    if request.method == 'GET':
        return render_template('login.html')# render file login.html
    else:
        user = request.form['username']
        password = request.form['password']
        if user in data_user and password == data_user[user]:
            return redirect(url_for('home', name = user)) # redirect sang url có def tên home và truyền vào tham số name value = user
        else:
            return redirect(url_for('register'))

@app.route('/register', methods =['POST', 'GET'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        user_name = request.form['username']
        passw = request.form['password']
        if Function.register(user_name, passw, data_user):
            return redirect(url_for('login'))
        else: return redirect(url_for('register'))


@app.route('/home/<name>', method = ['GET'])
def home(name):
    return f'<h3> hello {str(name)} </h3>'

# redirect url_for -> redirect sang url khac
@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'POST':
        log = request.form['login']
        re = request.form['register']
        print(log)
    else:
        return render_template('home.html')

if __name__ == '__main__':
    app.run(port=8080, host = '127.0.0.1', debug=True) # chạy web server

