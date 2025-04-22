import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)"""

cursor.execute(table_info)

cursor.execute('''INSERT INTO STUDENT values('Yash','NLP','C',90)''')
cursor.execute('''INSERT into STUDENT values('Pranav','NLP','C',70)''')

print('The inserted records are')

data=cursor.execute('''SELECT * from STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()

