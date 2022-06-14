import pymysql


def get_conn(db):
    global conn
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
    global cur
    cur = conn.cursor()
    return cur

def close():
    cur.close()
    conn.close()

def normal_ex(sql):
    result = cur.execute(sql)
    print(result)
    conn.commit()

def query(sql):
    cur.execute(sql)
    results = cur.fetchall()
    print(type(results))
    return results

