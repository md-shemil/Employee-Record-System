"""
Employee Record System by md_shemil
"""
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM employees')
    employees = cursor.fetchall()
    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    position = request.form['position']
    employeeid = request.form['employeeid']

    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO employees (name, age, gender, position, employeeid) VALUES (?, ?, ?, ?, ?)', (name, age, gender, position, employeeid))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/delete/<int:employee_id>')
def delete_employee(employee_id):
    conn = sqlite3.connect('employee.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM employees WHERE employee_id = ?', (employee_id,))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)


