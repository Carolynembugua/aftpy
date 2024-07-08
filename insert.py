import sqlite3
conn = sqlite3.connect('example.db')
print("Opened database successfully")


conn.execute("INSERT INTO EMPLOYEE VALUES (1,'Mary','Kamau',45,45000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (2,'Jane','Kelly',30,30000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (3,'Max','Cline',23,65000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (4,'Meli','Kimani',45,45000.00)")
conn.execute("INSERT INTO EMPLOYEE VALUES (5,'Mary','KARL',42,45300.00)")

conn.commit()

print("Successfully added records")
conn.close()