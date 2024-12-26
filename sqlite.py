import sqlite3

## Connect to the database
connection = sqlite3.connect("student.db")

## Create a cursor object using the cursor() method to insert record, create table
cursor = connection.cursor()

## create the table
table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""

cursor.execute(table_info)

## Insert the records
cursor.execute("INSERT INTO STUDENT VALUES ('John', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('Smith', 'MLOps', 'B', 85)")
cursor.execute("INSERT INTO STUDENT VALUES ('David', 'Data Science', 'A', 80)")
cursor.execute("INSERT INTO STUDENT VALUES ('John', 'Data Science', 'B', 75)")
cursor.execute("INSERT INTO STUDENT VALUES ('Smith', 'MLOps', 'A', 70)")
cursor.execute("INSERT INTO STUDENT VALUES ('David', 'Data Science', 'B', 65)")

## Display all the records
print("All the records in the table are: ")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

## Commit the changes
connection.commit()
connection.close()