from backend import DBMS

dbms = DBMS("166.111.71.220", "1521", "dbta")
dbms.login(user="s2016011246", password="19980211")

# dbms.sql("DROP TABLE Password")
# dbms.sql("DROP TABLE Cook")

init_password = "CREATE TABLE Password (username  varchar2(10) NOT NULL, password varchar2(20) NOT NULL, type char(1) NOT NULL, PRIMARY KEY (username, password))"

init_customer = "CREATE TABLE Customer (customerNo varchar2(20) NOT NULL, customName varchar2(10), birthday date, phone number(11, 0), email varchar2(50), PRIMARY KEY(customerNo))"
init_cook = "CREATE TABLE Cook (cookNo varchar2(20) NOT NULL, cookName varchar2(10), date date, PRIMARY KEY(cookNo))"
init_waiter = "CREATE TABLE Waiter (waiterNo varchar2(20) NOT NULL, waiterName varchar2(10), date date, PRIMARY KEY(waiterNo))"

init_dish = "CREATE TABLE Waiter (waiterNo varchar2(20) NOT NULL, waiterName varchar2(10), date date, PRIMARY KEY(waiterNo))"

init_cookfood = "CREATE TABLE CookFood (dishNo varchar2(10) NOT NULL, cookNo varchar2(10) NOT NULL, time timestamp, PRIMARY KEY(dishNo, cookNo))"

# dbms.sql(init_password)
# dbms.sql(init_cookfood)

dbms.conn.commit()


# dbms.insert_user("cook0", "cook0", "c")
# dbms.insert_user("waiter0", "waiter0", "w")
# dbms.insert_user("admin", "admin", "a")
# dbms.insert_user("customer0", "customer0", "x")

print(dbms.validate("cook0", "cook0", "c"))

res = dbms.sql("SELECT * FROM Password")
print(res.fetchall())