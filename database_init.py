from backend import DBMS

dbms = DBMS("166.111.71.220", "1521", "dbta")
dbms.login(user="s2016011246", password="19980211")

init_password = "CREATE TABLE Password (username  char(10) NOT NULL, password char(20) NOT NULL, type char(1) NOT NULL, PRIMARY KEY (username, password))"
init_cook = "CREATE TABLE Cook (customerNo char(20) NOT NULL, customName varchar2(10), birthday date, phone number(11, 0), email varchar2(50), PRIMARY KEY(customerNo))"


# dbms.sql(init_password)
# dbms.sql(init_cook)

dbms.insert_user("cook_0", "cook_0 pw", "c")
dbms.insert_user("waiter_0", "waiter_0 pw", "w")

print(dbms.validate("cook_0", "cook_0 pw", "c"))