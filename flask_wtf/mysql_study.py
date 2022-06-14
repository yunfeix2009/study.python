import pymysql
#
#
# def get_conn(db):
#     # 连接函数
#     # db:database
#     conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
#     cur = conn.cursor()
#     return cur,conn
#
# def insert(sql,cur,conn):
#     # 插入
#     # sql：插入的sql语句
#     # db:database
#     # conn:链接对象，作为参数传入， 可以关掉
#     result = cur.execute(sql)
#     print(result)
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# if __name__ == '__main__':
#     cur,conn=get_conn("wz")
#     insert("insert into test values(1,2,3)",cur,conn)
#
# # ----------------------------------------------------------------------------------------------
#
#
# def get_conn(db):
#     # 连接函数
#     # db:database
#     conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
#     cur = conn.cursor()
#     return cur,conn
#
# def insert(sql,args,cur,conn):
#     result = cur.execute(sql, args)
#     print(result)
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# if __name__ == '__main__':
#     cur,conn=get_conn('wz')
#     sql = "insert into test values(%s,%s,%s)"
#     insert(sql,(7,8,9),cur,conn)
#
#
# # ----------------------------------------------------------------------------------------------
#
#
#
#
# def get_conn(db):
#     # 连接函数
#     # db:database
#     conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
#     cur = conn.cursor()
#     return cur,conn
#
#
#
# def insert_many(sql,cur,conn,args):
#     #单次插入多条
#     # sql：插入的sql语句
#     # db:database
#     result = cur.executemany(query=sql, args=args)
#     print(result)
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
#
#
# if __name__ == '__main__':
#     cur,conn=get_conn('wz')
#     sql = "insert into test values(%s,%s,%s)"
#     args = [(0,0,0),(60,59,58)]
#     insert_many(sql,cur,conn,args)
#
#
# # ----------------------------------------------------------------------------------------------
#
# def get_conn(db):
#     # 连接函数
#     # db:database
#     conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
#     cur = conn.cursor()
#     return cur,conn
#
#
#
# def insert_many(sql,cur,conn,args):
#     #占位符的方式单次插入多条
#     # sql：插入的sql语句
#     # db:database
#     try:
#         result = cur.executemany(query=sql, args=args)
#         print(result)
#         conn.commit()
#     except:
#         conn.rollback()
#     finally:
#         cur.close()
#         conn.close()
#
#
#
#
# if __name__ == '__main__':
#     cur,conn=get_conn('wz')
#     sql = "insert into books values(%s,%s,%s,%s)"
#     args = [(1,'Evan','mystory',25),(2,'hhh','fun',2)]
#     insert_many(sql,cur,conn,args)
#
# ----------------------------------------------------------------------------------------------

def get_conn(db):
    # 连接函数
    # db:database
    conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
    cur = conn.cursor()
    return cur,conn

def delete(sql,cur,conn,args):
    #删除
    result = cur.execute(sql, args)
    print(result)
    conn.commit()
    cur.close()
    conn.close()



if __name__ == '__main__':
    cur,conn=get_conn('wz')
    sql = "DELETE FROM books WHERE id = %s and price=%s"
    args = (1,25)
    delete(sql,cur,conn,args)
# # ----------------------------------------------------------------------------------------------
#
# def get_conn(db):
#     # 连接函数
#     # db:database
#     conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
#     cur = conn.cursor()
#     return cur,conn
#
# def query(sql,cur,conn,args):
#     #查询
#
#     cur.execute(sql, args)
#     results = cur.fetchall()
#     print(type(results))
#
#     for row in results:
#         print(row)
#         french = row[0]
#         english = row[1]
#         UOI = row[2]
#         print('french:'+str(french)+'english:'+str(english)+'UOI'+str(UOI))
#
#     conn.commit()
#     cur.close()
#     conn.close()
#
#
# if __name__ == '__main__':
#     cur,conn=get_conn('wz')
#     sql = "select * from test"
#     query(sql,cur,conn,None)
#
# # ----------------------------------------------------------------------------------------------