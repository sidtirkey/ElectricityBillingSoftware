from tkinter import *
from database import *
from verification import *

#pylint: disable-msg=R0913



def register_user():
    c = 0
    username_info = username.get()
    password_info = password.get()
    address_info = address.get()
    aadhar_info = aadhar.get()
    radiobutton_info = var.get()
    print(radiobutton_info)

    if( len(username_info)>0  and len(password_info)>0 and len(address_info)>0  and len(aadhar_info)>0  and radiobutton_info !=0):

        if(len(password_info)<8):
            invalid_password_register()
        else:
            c = 1
        

        if(len(str(aadhar_info))!=12):
            invalid_aadhar_register()
        else:
            c = 1

        if(c == 1):
            
            writeOnDatabase(username_info,password_info,aadhar_info,address_info,radiobutton_info)
            #print("registeration success")
            register_success()

    else:
        enter_all_details()
        

def enter_all_details():
    global enter_all_details_screen
    enter_all_details_screen = Toplevel(register_screen)
    enter_all_details_screen.title("Unscuccessful")
    enter_all_details_screen.geometry("300x100")
    Label(enter_all_details_screen,text = "Enter all fields.").pack()
    Button(enter_all_details_screen,text = "OK",command = delete_enter_all_details_screen).pack()

def delete_enter_all_details_screen():
    enter_all_details_screen.destroy()



def register_success():
    global register_success_screen
    register_success_screen = Toplevel(register_screen)
    register_success_screen.title("Success!!!")
    register_success_screen.geometry("300x100")
    Label(register_success_screen,text = "Registration successful,You can login NOW!").pack()
    Button(register_success_screen,text = "OK",command = delete_register_success_screen).pack()


def delete_register_success_screen():
    register_success_screen.destroy()
    register_screen.destroy()





    

def invalid_aadhar_register():
    global invalid_aadhar_screen
    invalid_aadhar_screen = Toplevel(register_screen)
    invalid_aadhar_screen.title("Unscuccessful")
    invalid_aadhar_screen.geometry("300x100")
    Label(invalid_aadhar_screen,text = "Enter valid UID").pack()
    Button(invalid_aadhar_screen,text = "OK",command = delete_invalid_aadhar_register).pack()

def delete_invalid_aadhar_register():
    invalid_aadhar_screen.destroy()


        
       

def invalid_password_register():
    global invalid_password_screen
    invalid_password_screen = Toplevel(register_screen)
    invalid_password_screen.title("Unsuccessful")
    invalid_password_screen.geometry("300x100")
    Label(invalid_password_screen,text = "Minimum 8 character password").pack()
    Button(invalid_password_screen,text = "OK",command = delete_invalid_password_register).pack()


def delete_invalid_password_register():
    invalid_password_screen.destroy()

    



def register():
    global register_screen
    register_screen = Toplevel(main_screen) 
    register_screen.title("Register")
    register_screen.geometry("500x500")
 
# Set text variables
    global username
    username = StringVar()
    global password 
    password = StringVar()
    global address 
    address = StringVar()
    global aadhar 
    aadhar = StringVar()

 
# Set label for user's instruction
    Label(register_screen, text="Please enter details below", bg="#fcb603").pack()
    Label(register_screen, text="").pack()
    
# Set username label
    username_lable = Label(register_screen, text="Username ")
    username_lable.pack()
 
# Set username entry
# The Entry widget is a standard Tkinter widget used to enter or display a single line of text.
    
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
   
# Set password label
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    
# Set password entry
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()


#  set address label
    address_lable = Label(register_screen,text = "Billing Address")
    address_lable.pack()


#set address entry
    address_entry = Entry(register_screen,textvariable=address)
    address_entry.pack()


#set Aadhar label
    aadhar_lable = Label(register_screen,text = "Aadhar Number")
    aadhar_lable.pack()

#set Aadhar entry
    aadhar_entry = Entry(register_screen,textvariable=aadhar)
    aadhar_entry.pack()


#set radio button and label
    set_radioButton()

    
    Label(register_screen, text="").pack()
    
    # Set register button
    Button(register_screen, text="Register", width=10, height=1, bg="#fcb603",command = register_user).pack()


def set_radioButton():
    global var
    var = IntVar()

    Label(register_screen,text = "Enter Payment mode")
    R1 = Radiobutton(register_screen, text="Prepaid", variable=var, value=1)
    R1.pack()
    R2 = Radiobutton(register_screen, text="Postpaid", variable=var, value=2)
    R2.pack()




def login_verification():
    username = username_verify.get()
    password = password_verify.get()
    aadhar_number = aadhar_verify.get()

    if(len(username)>0 or len(password)>0 and len(aadhar_number)>0):
        login_verify(username,aadhar_number,password)



    else:
        login_verify_failed()




def login_verify_failed():
    global login_verify_failed_screen
    login_verify_failed_screen = Toplevel(login_screen)
    login_verify_failed_screen.title(" Login Unscuccessful")
    login_verify_failed_screen.geometry("300x100")
    Label(login_verify_failed_screen,text = "Enter login details correctly!").pack()
    Button(login_verify_failed_screen,text = "OK",command = delete_login_verify_failed_screen).pack()

def delete_login_verify_failed_screen():
    login_verify_failed_screen.destroy()

        







# define login function
def login_screen():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x300")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="Enter Username or Aadhar number").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
    global aadhar_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
    aadhar_verify = StringVar()
 
   
    Label(login_screen, text="Username ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()

    Label(login_screen, text="Aadhar number ").pack()
    aadhar_login_entry = Entry(login_screen, textvariable=aadhar_verify)
    aadhar_login_entry.pack()



    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password__login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password__login_entry.pack()

    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command=login_verification).pack()




def main_account_screen():
    global main_screen
 
# add command=register in button widget
 
    
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("main_screen")
 
    # create a Form label 
    Label(text="Vssut Electricity Billing system", bg="#fcb603", width="300", height="2", font=("Calibri", 13)).pack() 
    Label(text="").pack() 
    
    # create Login Button 
    Button(text="Login", height="2", width="30", command = login_screen).pack()
    Label(text="").pack() 
    
   



    Button(text="Register", height="2", width="30", command=register).pack()
    
    
    main_screen.mainloop()
 
main_account_screen()


