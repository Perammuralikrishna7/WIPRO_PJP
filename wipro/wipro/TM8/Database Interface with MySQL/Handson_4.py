import mysql.connector
mytb=mysql.connector.connect(host="localhost",user="root",password="MyNewPass",database="pythonexamples")
print("Connection sucessfull")
cur=mytb.cursor()
cur.execute("SELECT * FROM STUDENT")
s=cur.fetchall()
print(s)
print("student data fetched sucessfully")
cur.execute("SELECT * FROM MARKS")
m=cur.fetchall()
print(m)
print("marks data fetched sucessfully")
for i in s:
    for j in m:
        if i[0]==j[0]:
            print(i[1],"->",sum([j[2],j[3],j[4]]))
mytb.commit()
cur.close()
