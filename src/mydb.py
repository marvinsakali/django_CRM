import mysql.connector

dataBase = mysql.connector.connect(
	user='root',
	password='M@sakali21',
	host='localhost'
	)
cursor = dataBase.cursor()

cursor.execute('CREATE DATABASE dcrm')
print('Database created successfully!')
