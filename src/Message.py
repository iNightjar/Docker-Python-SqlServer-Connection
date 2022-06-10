import MySQLdb
db = MySQLdb.connect("mysql-server",``` "User"```,`` "Password"```,`` "DBName"```)
cursor = db.cursor()
cursor.execute("SELECT * FROM `` "Table Name"```")
data = cursor.fetchone()
fname = data[4]
lname = data[4]
print (fname,lname)
db.close()
