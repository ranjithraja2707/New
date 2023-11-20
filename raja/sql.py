import sqlite3
con = sqlite3.connect('database.db')
cursor = con.cursor()
create_table = '''
    CREATE TABLE IF NOT EXISTS employee ( id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER)
    '''
cursor.execute(create_table)
insert = '''
    INSERT INTO employee (name,age) VALUES (?,?)
'''
employee = [('ranjith',22),('raja',23),('lokesh',30)]
cursor.executemany(inserth,employee)
con.commit()
con.close()

con = sqlite3.connect('database.db')
cursor = con.cursor()

select_table = '''
    SELECT * FROM employee
'''
cursor.execute(select_table)

i = cursor.fetchall()

for row in i:
    print(row)