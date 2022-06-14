import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database = "school"
)

cur = mydb.cursor()
cur.execute('SELECT * FROM school.stu_sc')
print(cur.fetchall())