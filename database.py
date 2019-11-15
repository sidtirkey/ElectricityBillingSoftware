import sqlite3

def writeOnDatabase(username,password,aadhar,address,radio_button):
    if(radio_button == 1):
        payment = "prepaid"
    

    else:
        payment = "postpaid"
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('Create TABLE IF NOT EXISTS Customer(ID integer PRIMARY KEY AUTOINCREMENT,  Username TEXT,Password TEXT,aadhar_number TEXT,Address TEXT,payment_mode TEXT,Months_due INTEGER,Bill REAL,Fine REAL)')
    cursor.execute('INSERT INTO Customer (Username,Password,aadhar_number,Address,payment_mode) VALUES(?,?,?,?,?)',(username,password,aadhar,address,payment))
    conn.commit()



   

