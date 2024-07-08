import sqlite3
conn = sqlite3.connect('example.db')
print("Opened database successfully")

conn.execute('''CREATE TABLE EMPLOYEE(
ID INT PRIMARY KEY NOT NULL,
FIRSTNAME TEXT NOT NULL,
LASTNAME TEST,
AGE INT,
SALARY REAL)
''')

print("Sucessfully updated database")
conn.close()