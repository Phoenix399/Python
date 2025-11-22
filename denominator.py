from tkinter import *
from tkinter import messagebox


#from PIL imort Image , ImageTk

#Setting up main Window
root = Tk()
root.title('Denomination Counter')
root.configure(bg='blue')
root.geometry('650x400')
label1 = Label(root,
               text="Hey User! Welcome to Denomination Counter Application",
               font=('Arial', 20, 'bold'),
               bg='blue',
               fg='white')
label1.place(relx=0.5, y=340, anchor=CENTER)

#Function to display a messagebox and proceed if OK is clicke
def msg():
    MsgBox = messagebox.showinfo("Alert","Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

#Adding a button to main window
button1 = Button(root,text="Lets get started!",command=msg,font=('Arial',15,'bold'),bg='white',fg='blue')
button1.place(x=260,y=360)

#Function for opening new/top window
def topwin():
    top = Toplevel()
    top.title("Denomination Calculator")
    top.configure(bg='blue')
    top.geometry('600x450')

    label1 = Label(top,text="Enter the Amount",font=('Arial',20,'bold'),bg='blue',fg='white')
    entry = Entry(top,font=('Arial',15,'bold'),bg='white',fg='blue')
    lb1 = Label(top,text="Here are the notes for each denomination",font=('Arial',20,'bold'),bg='blue',fg='white')
     
    l1 = Label(top,text="2000 :",font=('Arial',15,'bold'),bg='blue',fg='white')
    l2 = Label(top,text="500  :",font=('Arial',15,'bold'),bg='blue',fg='white')
    l3 = Label(top,text="100  :",font=('Arial',15,'bold'),bg='blue',fg='white')

    t1 = Entry(top,font=('Arial',15,'bold'),bg='white',fg='blue')
    t2 = Entry(top,font=('Arial',15,'bold'),bg='white',fg='blue')
    t3 = Entry(top,font=('Arial',15,'bold'),bg='white',fg='blue')

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            n2000 = amount // 2000
            amount = amount % 2000
            n500 = amount // 500
            amount = amount % 500
            n100 = amount // 100
            
            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(0,str(n2000))
            t2.insert(0,str(n500))
            t3.insert(0,str(n100))
        
        except ValueError:
            messagebox.showerror("Invalid Input","Please enter a valid integer amount")
    btn = Button(top, text="Calculate",command=calculator,font=('Arial',15,'bold'),bg='white',fg='blue')
 
#Centering Widgets in Top Window
    label1.place(x=150,y=80)
    entry.place(x=450,y=80)
    btn.place(x=250,y=130)
    lb1.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)   

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)   

    top.mainloop()
root.mainloop()
