# encoding=utf8

from backend import DBMS

dbms = DBMS("166.111.71.220", "1521", "dbta")
dbms.login(user="s2016011246", password="19980211")

# Password
if True:
    try:
        dbms.sql("DROP TABLE Password")
    except Exception as e:
        print(e)
    init_password = "CREATE TABLE Password (username  varchar2(10) NOT NULL, password varchar2(20) NOT NULL, type char(1) NOT NULL)"
    dbms.sql(init_password)
    dbms.insert_user("cook0", "cook0", "c")
    dbms.insert_user("waiter0", "waiter0", "w")
    dbms.insert_user("admin", "admin", "a")
    dbms.insert_user("customer0", "customer0", "x")

# Cook
if True:
    try:
        dbms.sql("DROP TABLE Cook")
    except:
        pass
    init_cook = "CREATE TABLE Cook (cookNo varchar2(10) NOT NULL, cookName varchar2(10), workdate date, PRIMARY KEY(cookNo))"
    dbms.sql(init_cook)
    dbms.insert_cook("cook0", "Hellen", "2018-01-01")

# Waiter
if True:
    try:
        dbms.sql("DROP TABLE Waiter")
    except Exception as e:
        print(e)
        pass
    init_waiter = "CREATE TABLE Waiter (waiterNo varchar2(10) NOT NULL, waiterName varchar2(10), workdate date, PRIMARY KEY(waiterNo))"
    dbms.sql(init_waiter)
    dbms.insert_waiter("waiter0", "Julia", "2016-06-13")

# Customer
if True:
    try:
        dbms.sql("DROP TABLE Customer")
    except Exception as e:
        print(e)
        pass
    init_customer = "CREATE TABLE Customer (customerNo varchar2(20) NOT NULL, customName varchar2(50), birthday date, phone number(11, 0), email varchar2(50), PRIMARY KEY(customerNo))"
    dbms.sql(init_customer)
    dbms.insert_customer("customer0", "Lily", "1996-07-13", "18800000000", "xxx@126.com")


if True:
    try:
        dbms.sql("DROP TABLE Dish")
    except Exception as e:
        print(e)
        pass
    init_dish = "CREATE TABLE Dish (dishNo varchar2(20) NOT NULL, dishName varchar2(20) NOT NULL, dishPrice number(5) NOT NULL, dishDescription varchar2(100), PRIMARY KEY(dishNo))"
    dbms.sql(init_dish)
    dbms.insert_dish(dishNo="burger1", dishName="鲜虾汉堡", dishPrice=23, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="burger2", dishName="单层牛肉汉堡", dishPrice=23, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="burger3", dishName="蔬菜牛肉汉堡", dishPrice=26, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="burger4", dishName="西红柿奶酪汉堡", dishPrice=26, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="burger5", dishName="香辣炸鸡汉堡", dishPrice=24, dishDescription="Good! Perfect!")

    dbms.insert_dish(dishNo="drink1", dishName="可口可乐", dishPrice=6, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="drink2", dishName="雪碧", dishPrice=6, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="drink3", dishName="热巧克力", dishPrice=8, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="drink4", dishName="雪顶咖啡", dishPrice=12, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="drink5", dishName="热带果汁", dishPrice=10, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="drink6", dishName="鲜榨橙汁", dishPrice=16, dishDescription="Good! Perfect!")

    dbms.insert_dish(dishNo="sider1", dishName="薯条", dishPrice=16, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="sider2", dishName="蛋挞", dishPrice=5, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="sider3", dishName="芝士条", dishPrice=18, dishDescription="Good! Perfect!")
    dbms.insert_dish(dishNo="sider4", dishName="炸鸡翅", dishPrice=16, dishDescription="Good! Perfect!")


if True:
    try:
        dbms.sql("DROP TABLE Orders")
    except Exception as e:
        print(e)
        pass
    init_order = "CREATE TABLE Orders (orderNo varchar2(20) NOT NULL, customerNo varchar2(20) NOT NULL, ordertime timestamp, totalPrice number(5), PRIMARY KEY(orderNo))"
    dbms.sql(init_order)
    dbms.insert_order(orderNo="order0", customerNo="customer0", ordertime="2018-12-31  12:05:34", totalPrice=198)


if True:
    try:
        dbms.sql("DROP TABLE CookFood")
    except:
        pass
    init_cookfood = "CREATE TABLE CookFood (dishNo varchar2(10), cookNo varchar2(10), orderNo varchar2(20), cookfoodtime timestamp, status char(1) NOT NULL)"
    dbms.sql(init_cookfood)
    dbms.insert_cookfood(dishNo="burger1", cookNo="cook0", orderNo="order0", cookfoodtime="2018-12-31  12:05:34", status="A")

if True:
    try:
        dbms.sql("DROP TABLE Comments")
    except:
        pass
    init_comment = "CREATE TABLE Comments (dishNo varchar2(20), customerNo varchar2(20), content varchar2(1000), PRIMARY KEY(dishNo, customerNo))"
    dbms.sql(init_comment)
    dbms.insert_comment(dishNo="burger1", customerNo="customer0", content="Not bad.")


# dbms.sql("DROP TABLE Comment")
# dbms.sql("DROP TABLE Include")
# dbms.sql("DROP TABLE Mention")


print(dbms.validate("cook0", "cook0", "c"))

res = dbms.sql("SELECT * FROM Password")
print(res.fetchall())