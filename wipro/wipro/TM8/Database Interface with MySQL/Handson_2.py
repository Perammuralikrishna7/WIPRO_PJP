import mysql.connector
mytb=mysql.connector.connect(host="localhost",user="root",password="MyNewPass",database="pythonexamples")
print("Connection sucessfull")
cur=mytb.cursor()
cur.execute("INSERT INTO STUDENT VALUES(1,\"SAGAR\",\"DELHI\")")
cur.execute("INSERT INTO STUDENT VALUES(4,\"swamy\",\"hyd\")")
cur.executemany("""INSERT INTO STUDENT(ROOLNO,NAME,ADRESS) VALUES(%s,%s,%s)""",[(2,"SURESH","BANGLORE"),(3,"SWATI","CHENNAI")])
print("inserted sucessfully")
cur.executemany("""INSERT INTO MARKS(EXAMID,ROLLNO,M1,M2,M3) VALUES(%s,%s,%s,%s,%s)""",[(1,1,12,23,23),(2,2,23,34,34),(3,3,23,12,34),(4,4,21,31,21)])
print("insertion sucessfull into marks")
mytb.commit()
cur.close()