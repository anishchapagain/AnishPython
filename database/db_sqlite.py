import sqlite3
connection = sqlite3.connect('database.db')

connection.execute('drop table if exists staff')
print("Table staff Exists/Drop")
#creating Table
connection.execute('create table staff(ID int,Name text,Age int,Gender text)')
print("Table staff Created")
#insert Values
connection.execute('insert into staff(ID,Name,Age,Gender) values(0001,"Name 1",21,"M")')
connection.execute('insert into staff(ID,Name,Age,Gender) values(0002,"Name 2",28,"F")')
connection.execute('insert into staff(ID,Name,Age,Gender) values(0003,"Name 3",26,"M")')

connection.commit()
print("Rows are inserted in Table staff Created")

cursor = connection.cursor()

print("Displaying staff Created")
#cursor.execute('select * from staff')
#result = cursor.fetchall()
#result= cursor.fetchone()

result = connection.execute('select * from staff')
for rows in result:
    print(rows)
