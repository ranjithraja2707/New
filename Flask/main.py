from flask import Flask, render_template, request
import sqlite3
import pandas as pd

app = Flask(__name__)

# Moved database connection and cursor initialization outside of the routes
conn = sqlite3.connect('user.db')
cursor = conn.cursor()
create_table = '''
CREATE TABLE IF NOT EXISTS data (id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username VARCHAR,
                                password VARCHAR)'''
cursor.execute(create_table)
conn.commit()

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        enter = request.form.get('enter')
        pass1 = request.form.get('pass1')

        # Use the 'with' statement for better connection handling
        with sqlite3.connect('user.db') as conn:
            cursor = conn.cursor()

            # Provide values as a tuple
            insert_data = '''INSERT INTO data (username, password) VALUES (?, ?)'''
            cursor.execute(insert_data, (enter, pass1))
            conn.commit()

    return render_template('home.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Use the 'with' statement for better connection handling
        with sqlite3.connect('user.db') as conn:
            cursor = conn.cursor()

            # Provide values as a tuple
            insert_data = '''INSERT INTO data (username, password) VALUES (?, ?)'''
            cursor.execute(insert_data, (username, password))
            conn.commit()

    return render_template('log.html')

@app.route('/sign', methods=['POST', 'GET'])
def sign():
    return render_template('sign.html')

@app.route('/display', methods=['POST', 'GET'])
def display():
    with sqlite3.connect('user.db') as conn:
        cursor = conn.cursor()
        select_data = '''SELECT * FROM data'''
        cursor.execute(select_data)
        data = cursor.fetchall()

        # Convert the fetched data to a Pandas DataFrame
        df = pd.DataFrame(data, columns=['ID', 'Username', 'Password'])

        # Save the DataFrame to an Excel file
        df.to_excel('raja.xlsx', index=False, engine='openpyxl')

    return render_template("display.html", data=data)

if __name__ == '__main__':
    app.run(debug=True)
