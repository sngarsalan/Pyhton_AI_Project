import mysql.connector
from pyparsing import dblSlashComment

dbs=mysql.connector.connect(host="localhost",user="root",password="", database="sindhbiz")

print(dbs)

#mycursor=sindhbiz.cursor()

#mycursor.execute("SELECT * from info")

#query="INSERT INTO info (Name,Phone,Address) VALUES (%s,%s,%s)"

#val=[("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),("Sangi","032122909","Hyderbad"),]

query="SELECT * from info "
cur=dbs.cursor()

cur.execute(query)

for row in cur:
    print(row)

dbs.commit()


#print(cur.rowcount, "Updated")




