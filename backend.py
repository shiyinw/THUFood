import cx_Oracle

class DBMS(object):
    def __init__(self, addr, port, name):
        self.dsnStr = cx_Oracle.makedsn(addr, port, name)
    def login(self, user, password):
        assert self.dsnStr, "Connection Error"
        self.conn = cx_Oracle.connect(user, password, dsn=self.dsnStr)
        self.c = self.conn.cursor()

    def exec(self, sql):
        return self.c.execute(sql)

if __name__ == "__main__":
    dbms = DBMS("166.111.71.220", "1521", "dbta")
    dbms.login(user="s2016011246", password="19980211")
    x = dbms.exec('select * from CLASS')
    for i in x:
        print(i)