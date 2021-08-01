import mysql.connector


mydb = mysql.connector.connect(host="c300.mysql.database.azure.com", user="default@c300", password="@Republic1")

print(mydb)

mycursor=mydb.cursor()

mycursor.execute("select * from integration.user")
result = mycursor.fetchall()

for i in result:
    print(i)