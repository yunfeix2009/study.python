import pymysql

# def get_conn(db):
#     # 连接函数
#     # db:database
#     conn=pymysql.connect(host='localhost',port=3306,user='root',password='123456',database=db)
#     cur = conn.cursor()
#     return cur,conn
#
# def create(sql,cur,conn):
#     # 建表
#     # sql：建表的sql语句
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
#     create('Create table student ( SID varchar(20) primary key not null, SName varchar(20), SAge int, SSex char(1), STel char(13) null default "-" );',cur,conn)


# --------------------------------------------------------------------

db = pymysql.Connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='wz',
    charset='utf8'
)

cursor = db.cursor()

try:
    ins_sql = "INSERT INTO student (SID, SName, SAge, SSex, STel) VALUES ('2', 'Aaro', 13, '1', '12343211234');"
    r=cursor.execute(ins_sql)
    if r==1:
        db.commit()
        print('插入成功')
    # que_sql = "select * from student where SID>=3"
    que_sql = "select SName,SAge from student"
    cursor.execute(que_sql)
    result = cursor.fetchall()
    print('查询结果：')
    if result==():
        print('None')
    else:
        for row in result:
            print(row)

    upd_sql = "UPDATE student SET STel = 12312341234 WHERE SID=1;"
    cursor.execute(upd_sql)
    db.commit()
    print('更新成功')
    que_sql = "select * from student"
    cursor.execute(que_sql)
    result = cursor.fetchall()
    print('更新结果：')
    if result==():
        print('None')
    else:
        for row in result:
            print(row)


    del_sql = "DELETE FROM student WHERE SID='2'"
    cursor.execute(del_sql)
    db.commit()
    print('删除成功')
    que_sql = "select * from student"
    cursor.execute(que_sql)
    result = cursor.fetchall()
    print('删除结果：')
    if result==():
        print('None')
    else:
        for row in result:
            print(row)


finally:
    pass
    sql = "DROP TABLE `wz`.`student`"
    cursor.execute(sql)
    db.commit()
    print('表删除成功')

cursor.close()
db.close()