from flask import Flask, render_template, request, json, url_for
from backend import DBMS

dbms = DBMS("166.111.71.220", "1521", "dbta")
dbms.login(user="s2016011246", password="19980211")

app = Flask(__name__, static_url_path='/templates')

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/login_cook')
def login_cook():
    return render_template("login_cook.html")

@app.route('/handle_login_cook', methods=['POST', 'GET'])
def handle_data():
    print("------- handle_cook login data")
    if request.method == "POST":
        id = request.form['id']
        pw = request.form['pw']
        print(id, pw)
    return render_template('menu.html')

@app.route('/test')
def show_test():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)
