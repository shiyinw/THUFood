from flask import Flask, render_template, request, json, url_for, redirect
from backend import *

dbms = DBMS("166.111.71.220", "1521", "dbta")
dbms.login(user="s2016011246", password="19980211")

app = Flask(__name__, static_url_path='/templates')


cook_id = None
waiter_id = None
customer_id = None
admin_id = None

@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/data_cook', methods=['POST', 'GET'])
def data_cook():
    if request.method=="POST":
        dish_id = request.form['id']
        dish_state = request.form['state']
        print(dish_id, dish_state)
    dishes = dbms.query_cook_dishes(cook_id)
    print(dishes)
    return render_template("cook.html", dishes=dishes)

@app.route('/cook', methods=['POST', 'GET'])
def login_cook():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=10 and len(pw)<=20):
            if(dbms.validate(id, pw, "c")):
                cook_id = id
                print("Login with cook: ", cook_id)
                return render_template('cook.html', id=id)
        return render_template('login_cook.html', error=True)
    return render_template("login_cook.html")

@app.route('/customer', methods=['POST', 'GET'])
def login_customer():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=20 and len(pw)<=20):
            if(dbms.validate(id, pw, "x")):
                customer_id = id
                print("Login with customer: ", customer_id)
                return render_template('customer.html')
        return render_template('login_customer.html', error=True)
    return render_template("login_customer.html", error=False)


@app.route('/waiter', methods=['POST', 'GET'])
def login_waiter():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=10 and len(pw)<=20):
            if(dbms.validate(id, pw, "w")):
                waiter_id = id
                print("Login with waiter: ", waiter_id)
                return render_template('waiter.html')
        return render_template('login_waiter.html', error=True)
    return render_template("login_waiter.html", error=False)

@app.route('/admin', methods=['POST', 'GET'])
def login_admin():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=10 and len(pw)<=20):
            if(dbms.validate(id, pw, "a")):
                admin_id = id
                print("Login with admin: ", admin_id)
                return render_template('admin.html')
        return render_template('login_admin.html', error=True)
    return render_template("login_admin.html", error=False)

@app.route('/test')
def show_test():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)
