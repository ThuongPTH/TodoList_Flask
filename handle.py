from flask import *
import Function

# tạo 1 biến app
app = Flask(__name__)

data_user = Function.get_data_user()

# tạo đường dẫn url /login
@app.route('/login', methods =['POST', 'GET'])
def login():
    if request.method == 'GET':
        forgot = request.args.get('forgot')
        print(forgot)
        if forgot==1: return redirect(url_for('chang_pass'))
        else: return render_template('login.html') # render file login.html
    else:
        user = request.form['username']
        password = request.form['password']
        if user in data_user and password == data_user[user]:
            return redirect(url_for('home', name = user)) # redirect sang url có def tên home và truyền vào tham số name value = user
        else:
            return redirect(url_for('register'))

@app.route('/change_pass', methods = ['PUT', 'GET'])
def change_pass():
    return render_template('change_pass.html')

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

# truyền biến
@app.route('/home/<name>')
def home(name):
    return f'<h3> hello {str(name)} </h3>'

#handle get request
@app.route('/', methods = ['GET'])
def hello():
    check = request.args.get('check')
    if check =='login': return redirect(url_for('login'))
    elif check == 'register': return redirect(url_for('register'))
    else: return render_template('home.html')

if __name__ == '__main__':
    app.run(port=8080, host = '127.0.0.1', debug=True) # chạy web server

