import sqlite3

# Connect to sqlite 
connection = sqlite3.connect("Student.db")

# Create a cursor object to insert record,create table , retrieve
cursor = connection.cursor()

# Create a table 
table_info = '''
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
'''

cursor.execute(table_info)


# Insert some more records 

cursor.execute('''Insert Into STUDENT values('Keanu','Data Science','A',90)''')
cursor.execute('''Insert Into STUDENT values('Orion Pax','Data Science','B',100)''')
cursor.execute('''Insert Into STUDENT values('Bumblebee','Data Science','B',10)''')
cursor.execute('''Insert Into STUDENT values('Severus Snape','Data Science','A',86)''')
cursor.execute('''Insert Into STUDENT values('Max','DEVOPS','A',50)''')
cursor.execute('''Insert Into STUDENT values('Mike','DEVOPS','A',35)''')


# Display all the record
print("The Inserted records are")

data = cursor.execute('''Select * from STUDENT''')

for row in data:
    print(row)


# Close the connection 

connection.commit()
connection.close()