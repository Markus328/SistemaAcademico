import mysql.connector

database : mysql.connector.connection.MySQLConnection
cursor : mysql.connector.cursor.MySQLCursor

def print_data():
    for x in cursor:
        print(x)

def fetchall():
    af = cursor.fetchall()
    for i in range(len(af)):
        af[i] = af[i][0]

    return af

def connect(db_name): 
    global cursor
    global database
    database = mysql.connector.connect(host="localhost", user="root",database=db_name)
    cursor = database.cursor()


def __get_sql(sql, where, *args):
    sql = sql % args 
    if where:
        sql += " WHERE %s" % (where)
    return sql


def insert(table,values,columns=""):
    cursor.execute("INSERT INTO %s %s VALUES %s" % (table, str(columns), str(values)))
    database.commit()

def update(table, sets, where=None):
    sql = __get_sql("UPDATE %s SET %s", where, table, sets)
    cursor.execute(sql)
    database.commit()

def select(table, select, where=None):
    sql = __get_sql("SELECT %s FROM %s",where,select,table)
    cursor.execute(sql)

def delete(table, where=None):
    sql = __get_sql("DELETE FROM %s",where,table)
    cursor.execute(sql)
    database.commit()
