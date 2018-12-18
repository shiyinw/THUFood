import cx_Oracle

class DBMS(object):
    def __init__(self, addr, port, name):
        self.dsnStr = cx_Oracle.makedsn(addr, port, name)
    def login(self, user, password):
        assert self.dsnStr, "Connection Error"
        self.conn = cx_Oracle.connect(user, password, dsn=self.dsnStr)
        self.c = self.conn.cursor()

    def sql(self, sql):
        print("SQL:", sql)
        return self.c.execute(sql)

    def query_waiter(self, id):
        sql = "SELECT * FROM Waiter WHERE waiterNo='{}'".format(id)
        return self.sql(sql).fetchall()

    def query_customer(self, id):
        sql = "SELECT * FROM Customer WHERE customerNo='{}'".format(id)
        return self.sql(sql).fetchall()

    def query_cook(self, id):
        sql = "SELECT * FROM Cook WHERE cookNo='{}'".format(id)
        return self.sql(sql).fetchall()

    def query_dish(self, id):
        sql = "SELECT * FROM Dish WHERE dishNo='{}'".format(id)
        return self.sql(sql).fetchall()

    def query_order(self, id):
        sql = "SELECT * FROM Order WHERE orderNo='{}'".format(id)
        return self.sql(sql).fetchall()

    def query_cook_dishes(self, cookid):
        sql = "SELECT * FROM CookFood WHERE cookNo='{}'".format(cookid)
        return self.sql(sql).fetchall()

    def query_include(self, dishid, orderid):
        sql = "SELECT * FROM Include WHERE dishNo='{}' AND orderNo={}".format(dishid, orderid)
        return self.sql(sql).fetchall()

    def validate(self, username, password, type):
        sql = "SELECT * FROM Password WHERE username='{}' AND password='{}' AND type='{}'".format(username, password, type)
        return (len(self.sql(sql).fetchall())>0)

    def insert_user(self, username, password, type):
        sql = "INSERT INTO Password VALUES ('{}', '{}', '{}')".format(username, password, type)
        self.sql(sql)
        self.conn.commit()

    def insert_cook(self, cookNo, cookName, date):
        sql = "INSERT INTO Cook VALUES ('{}', '{}', DATE '{}')".format(cookNo, cookName, date)
        self.sql(sql)
        self.conn.commit()

    def insert_waiter(self, waiterNo, waiterName, date):
        sql = "INSERT INTO Waiter VALUES ('{}', '{}', DATE '{}')".format(waiterNo, waiterName, date)
        self.sql(sql)
        self.conn.commit()

    def insert_customer(self, customerNo, customerName, birthday, phone, email):
        sql = "INSERT INTO Customer VALUES ('{}', '{}', DATE '{}', {}, '{}')".format(customerNo, customerName, birthday, phone, email)
        self.sql(sql)
        self.conn.commit()

    def insert_dish(self, dishNo, dishName, dishPrice, dishDescription="", photo='NULL'):
        sql = "INSERT INTO Dish VALUES ('{}', '{}', {}, '{}', {})".format(dishNo, dishName, dishPrice, dishDescription, photo)
        self.sql(sql)
        self.conn.commit()

    def insert_order(self, orderNo, customerNo, waiterNo, ordertime, totalPrice, status):
        sql = "INSERT INTO Orders VALUES ('{}', '{}', '{}', TIMESTAMP '{}', {}, '{}')".format(orderNo, customerNo, waiterNo, ordertime, totalPrice, status)
        self.sql(sql)
        self.conn.commit()

    def insert_cookfood(self, dishNo, cookNo, cookfoodtime):
        sql = "INSERT INTO CookFood VALUES('{}', '{}', TIMESTAMP '{}')".format(dishNo, cookNo, cookfoodtime)
        self.sql(sql)
        self.conn.commit()

if __name__ == "__main__":
    dbms = DBMS("166.111.71.220", "1521", "dbta")
    dbms.login(user="s2016011246", password="19980211")
    x = dbms.sql("SELECT * FROM CLASS WHERE CLASSNO='CP0801'")
    print(x.description)

    for i in x:
        print(i)

    x = dbms.sql("SELECT owner, table_name FROM dba_tables")
    print(x.description)

    for i in x:
        print(i)

