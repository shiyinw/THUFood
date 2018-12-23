from flask import Flask, render_template, request, json, url_for, redirect
from backend import *

dbms = DBMS("166.111.71.220", "1521", "dbta")
dbms.login(user="s2016011246", password="19980211")

app = Flask(__name__, static_url_path='/templates')

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/data_admin/<admin_id>', methods=['POST', 'GET'])
def data_admin(admin_id):
    output = ""
    if request.method=="POST":
        try:
            output = dbms.sql(request.form["sql"]).fetchall()
            dbms.conn.commit()
        except Exception as e:
            output = "*"*20+'\n' + "Error:" + request.form["sql"] + '\n' + str(e) + '\n' + "*" * 20
    cook = dbms.sql("SELECT * FROM Cook").fetchall()
    customer = dbms.sql("SELECT * FROM Customer").fetchall()
    waiter = dbms.sql("SELECT * FROM Waiter").fetchall()
    dish = dbms.sql("SELECT * FROM Dish").fetchall()
    orders = dbms.sql("SELECT * FROM Orders").fetchall()
    cookfood = dbms.sql("SELECT * FROM CookFood").fetchall()
    comments = dbms.sql("SELECT * FROM Comments").fetchall()
    pw = dbms.sql("SELECT * FROM Password").fetchall()

    return render_template("admin.html", output=output, thisid=admin_id, cook=cook, customer=customer, waiter=waiter, dish=dish, orders=orders, cookfood=cookfood, comments=comments, pw=pw)


@app.route('/data_cook/<cook_id>', methods=['POST', 'GET'])
def data_cook(cook_id):
    if request.method=="POST":
        dish_id = request.form['dishid']
        order_id = request.form['orderid']
        dbms.action_cook(dish_id, order_id)
    identity, dishes = dbms.query_cook(cook_id)
    ident = identity[1]
    return render_template("cook.html", identity=ident, dishes=dishes, thisid=cook_id)

@app.route('/data_customer/<customer_id>', methods=['POST', 'GET'])
def data_customer(customer_id):
    dishes = dbms.sql("SELECT * FROM Dish").fetchall()
    return render_template('customer.html', thisid=customer_id, dishes=dishes)

@app.route('/customer_confirm/<customer_id>', methods=["POST"])
def confirm(customer_id):
    ordered = request.form["text"].split()
    cart = []
    totalprice = 0
    store = ""
    for i in ordered:
        item = dbms.sql("SELECT * FROM Dish WHERE dishNo='{}'".format(i)).fetchone()
        if(len(item)==4):
            cart.append(item)
            totalprice += int(item[2])
            store += str(item[0]) + "&"
    return render_template("confirm.html", store=store, cart=cart, totalprice=totalprice, order="order"+str(customer_id[8:]), thisid=customer_id)

@app.route('/data_waiter/<waiter_id>', methods=['POST', 'GET'])
def data_waiter(waiter_id):
    if request.method=="POST":
        if(request.form["customerid"]!="" and request.form["customername"]!=""):
            if(request.form["birthday"]!=""):
                try:
                    dbms.insert_customer(customerNo=request.form["customerid"], customerName=request.form["customername"],
                            birthday=request.form["birthday"], phone=request.form["phone"], email=request.form["email"])
                except:
                    pass
            else:
                try:
                    dbms.insert_customer(customerNo=request.form["customerid"], customerName=request.form["customername"],
                                     phone=request.form["phone"], email=request.form["email"])
                except:
                    pass
        if(request.form["delete"]!=""):
            try:
                dbms.delete_order(request.form["delete"])
            except:
                pass
        dish_id = request.form['dishid']
        order_id = request.form['orderid']
        dbms.action_waiter(dish_id, order_id)
    identity, dishes = dbms.query_waiter(waiter_id)
    ident = identity[1]
    return render_template("waiter.html", identity=ident, dishes=dishes, thisid=waiter_id)

@app.route('/cook', methods=['POST', 'GET'])
def login_cook():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=10 and len(pw)<=20):
            if(dbms.validate(id, pw, "c")):
                print("Login with cook: ", id)
                identity, dishes = dbms.query_cook(id)
                return render_template('cook.html', thisid=id, identity=identity[1], dishes=dishes)
        return render_template('login_cook.html', error=True)
    return render_template("login_cook.html")

@app.route("/comment/<customer_id>/<cart>/<price>", methods=["POST"])
def comment(customer_id, cart, price):

    orderid = "order_"+str(customer_id)
    if request.method == "POST":
        dbms.insert_order(orderNo=orderid, customerNo=customer_id, totalPrice=price)
        for i in cart.split("&")[:-1]:
            dbms.insert_cookfood(cookNo="cook0", dishNo=i, orderNo=orderid, status="A")

    dishes = dbms.sql("SELECT Dish.dishNo, dishName, cookName, dishPrice, CookFood.status FROM CookFood, Dish, Cook WHERE Cook.cookNo=CookFood.cookNo AND orderNo='{}' AND Dish.dishNo=CookFood.dishNo ORDER BY Dish.dishNo".format(orderid)).fetchall()
    print(dishes)
    return render_template("comment.html", thisid=customer_id, dishes=dishes)

@app.route("/track/<customer_id>", methods=["POST"])
def track(customer_id):
    orderid = "order_"+str(customer_id)
    dishes = dbms.sql("SELECT Dish.dishNo, dishName, cookName, dishPrice, CookFood.status FROM CookFood, Dish, Cook WHERE Cook.cookNo=CookFood.cookNo AND orderNo='{}' AND Dish.dishNo=CookFood.dishNo ORDER BY Dish.dishNo".format(orderid)).fetchall()
    return render_template("comment.html", thisid=customer_id, dishes=dishes)


@app.route('/customer', methods=['POST', 'GET'])
def login_customer():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=20 and len(pw)<=20):
            if(dbms.validate(id, pw, "x")):
                print("Login with customer: ", id)
                dishes = dbms.sql("SELECT * FROM Dish").fetchall()
                return render_template('customer.html', thisid=id, dishes=dishes)
        return render_template('login_customer.html', error=True)
    return render_template("login_customer.html", error=False)


@app.route('/waiter', methods=['POST', 'GET'])
def login_waiter():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=10 and len(pw)<=20):
            if(dbms.validate(id, pw, "w")):
                print("Login with waiter: ", id)
                identity, dishes = dbms.query_waiter(id)
                return render_template('waiter.html', thisid=id, dishes=dishes)
        return render_template('login_waiter.html', error=True)
    return render_template("login_waiter.html", error=False)

@app.route('/admin', methods=['POST', 'GET'])
def login_admin():
    if request.method=="POST":
        id = request.form['id']
        pw = request.form['pw']
        if(len(id)<=10 and len(pw)<=20):
            if(dbms.validate(id, pw, "a")):
                print("Login with admin: ", id)
                cook = dbms.sql("SELECT * FROM Cook").fetchall()
                customer = dbms.sql("SELECT * FROM Customer").fetchall()
                waiter = dbms.sql("SELECT * FROM Waiter").fetchall()
                dish = dbms.sql("SELECT * FROM Dish").fetchall()
                orders = dbms.sql("SELECT * FROM Orders").fetchall()
                cookfood = dbms.sql("SELECT * FROM CookFood").fetchall()
                comments = dbms.sql("SELECT * FROM Comments").fetchall()
                pw = dbms.sql("SELECT * FROM Password").fetchall()

                return render_template("admin.html", thisid=id, cook=cook, customer=customer, waiter=waiter,
                                       dish=dish, orders=orders, cookfood=cookfood, comments=comments, pw=pw)

        return render_template('login_admin.html', error=True)
    return render_template("login_admin.html", error=False)

@app.route('/test')
def show_test():
    return render_template('menu.html')


if __name__ == '__main__':
    app.run(debug=True)
