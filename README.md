# employee.db creating steps
# open the terminal and write python and enter
import sqlite3

# Create/connect to a database
conn = sqlite3.connect('employee.db')
# enter
cursor = conn.cursor()

# Create a table for employees if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        employee_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        gender TEXT,
        position TEXT,
        employeeid INTEGER
    )
''')

# Commit the changes and close the connection
conn.commit()
# enter
conn.close()

# project by md_shemil