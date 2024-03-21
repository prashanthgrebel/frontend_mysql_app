import mysql.connector

connection = mysql.connector.connect (host='192.168.1.120',port='3308',database='registration',user='root',password='Pgr@9902#wer')
cursor = connection.cursor()

cursor.execute("select * from People")

for i in cursor:
  print(i)


