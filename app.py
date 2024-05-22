from flask import Flask, render_template, request, redirect, url_for
import pyodbc

app = Flask(__name__)

# Database connection details
server = 'ikserver13.database.windows.net'
database = 'ikdb'
username = 'ik'
password = 'Ishu@2022'
driver = '{ODBC Driver 17 for SQL Server}'

# Establish connection
conn = pyodbc.connect(f'DRIVER={driver};SERVER={server};PORT=1433;DATABASE={database};UID={username};PWD={password}')

@app.route('/')
def index():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM your_table")
    rows = cursor.fetchall()
    return render_template('index.html', rows=rows)

@app.route('/add', methods=['POST'])
def add():
    name = request.form['name']
    age = request.form['age']
    cursor = conn.cursor()
    cursor.execute("INSERT INTO your_table (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM your_table WHERE id=?", (id,))
    conn.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id>', methods=['POST'])
def edit(id):
    name = request.form['name']
    age = request.form['age']
    cursor = conn.cursor()
    cursor.execute("UPDATE your_table SET name=?, age=? WHERE id=?", (name, age, id))
    conn.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
