import mysql.connector
mytb=mysql.connector.connect(host="localhost",user="root",password="MyNewPass",database="pythonexamples")
print("Connection sucessfull")
cur=mytb.cursor()
cur.execute("SELECT * FROM STUDENT")
print("Records in the student table are below:-",*cur.fetchall(),sep="\n")
print("fetched sucessfully")
cur.execute("SELECT * FROM MARKS")
print("Records in the MARKS table are below:-",*cur.fetchall(),sep="\n")
print("fetched sucessfully")
mytb.commit()
cur.close()
