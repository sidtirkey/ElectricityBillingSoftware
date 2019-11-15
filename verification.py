
import sqlite3

def login_verify(username,aadhar,password):
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.excecute('SELECT Username,Password,aadhar_number FROM Customer')
    records = cursor.fetchall()
    for row in records:
        print(row[1])

