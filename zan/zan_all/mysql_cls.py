class Sql_class():
    def get_conn(self):
        import pymysql
        conn = pymysql.connect(host='localhost',port=3306,user='root',password='123456',database='zan')
        cur = conn.cursor()
        return conn, cur

    def close(self, conn,cur):
        cur.close()
        conn.close()

    def normal_ex(self, conn, cur, sql):
        cur.execute(sql)
        conn.commit()

    def query(self, cur, sql):
        cur.execute(sql)
        results = cur.fetchall()
        return results
