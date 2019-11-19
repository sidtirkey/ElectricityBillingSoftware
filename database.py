import sqlite3

def writeOnDatabase(username,password,aadhar,address,radio_button):
    if(radio_button == 1):
        payment = "prepaid"
    

    else:
        payment = "postpaid"
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('Create TABLE IF NOT EXISTS Customer(ID integer PRIMARY KEY AUTOINCREMENT,  Username TEXT,Password TEXT,aadhar_number TEXT,Address TEXT,payment_mode TEXT,Units INTEGER DEFAULT 0,Months_due INTEGER DEFAULT 0,Bill REAL DEFAULT 0.0,Fine REAL DEFAULT 0.0)')
    cursor.execute('INSERT INTO Customer (Username,Password,aadhar_number,Address,payment_mode) VALUES(?,?,?,?,?)',(username,password,aadhar,address,payment))
    conn.commit()


def write_bill(ID,bill,fine):
    ID = (str)(ID)
    bill = (str)(bill)
    fine = (str)(fine)
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()

    #print(ID,bill,fine)
    
    cursor.execute('UPDATE Customer SET Bill = ? WHERE ID = ?',(bill,ID))
    cursor.execute('UPDATE Customer SET Fine = ? WHERE ID = ?',(fine,ID))
    conn.commit()

def set_unit(ID):
    ID = (str)(ID)
  
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()
    cursor.execute('UPDATE Customer SET Units = 0 WHERE ID = ?',(ID))
    cursor.execute('UPDATE Customer SET Months_due = 0 WHERE ID = ?',(ID))

    conn.commit()



def update_customer_admin(ID,username,password,address,units,month):
    id = (str)(ID)
    Units = (str)(units)
    Month = (str)(month)

    
    conn = sqlite3.connect('Form.db')
    with conn:
        cursor = conn.cursor()

    if(len(username)>0):
        cursor.execute('UPDATE Customer SET Username = ? WHERE ID = ?',(username,id))

    if(len(password) > 0):
         cursor.execute('UPDATE Customer SET Password = ? WHERE ID = ?',(password,id))

    if(len(address) > 0):
         cursor.execute('UPDATE Customer SET Address = ? WHERE ID = ?',(address,id))

    if(units > 0):
         cursor.execute('UPDATE Customer SET Units = ? WHERE ID = ?',(Units,id))

    if(month > 0):
         cursor.execute('UPDATE Customer SET Months_due = ? WHERE ID = ?',(Month,id))


    conn.commit()







    
    
