from tkinter import*
from tkinter import ttk, messagebox
import csv

def writetocsv(data):
    with open('data.csv','a',newline='')as f:
        fw = csv.writer(f)
        fw.writerow(data)
        print('csv was writen')

def Addproduct():
    calculate = int (Price.get()) * int (Quantity.get())
    text = "Product Name:{}\nPrice:{}\nQuantity:{}\n Total:{}".format(Name.get(),Price.get(),Quantity.get(),calculate)
    datatocsv = [Name.get(),Price.get(),Quantity.get(),calculate]
    print(text)
    Res.set(text)
    writetocsv(datatocsv)
    messagebox.showinfo('Adding..','Product was added')


GUI = Tk()
GUI.title('Jiranicha Shop')
GUI.geometry('700x500')

#Label and Entry
#------------------Row0------------------------------
LName = ttk.Label(GUI, text='Product Name ',font=(None,18))
LName.grid(row=0,column=0,padx=10,pady=10)

Name = StringVar()

EName = ttk.Entry(GUI, textvariable=Name,font=(None,18))
EName.grid(row=0,column=1,padx=10,pady=10)
#------------------Row1------------------------------
LPrice = ttk.Label(GUI, text='Price',font=(None,18))
LPrice.grid(row=1,column=0,padx=10,pady=10)

Price = StringVar()

EPrice = ttk.Entry(GUI, textvariable=Price,font=(None,18))
EPrice.grid(row=1,column=1,padx=10,pady=10)
#------------------Row2------------------------------
LQuantity = ttk.Label(GUI, text='Quantity',font=(None,18))
LQuantity.grid(row=2,column=0,padx=10,pady=10)

Quantity = StringVar()

EQuantity = ttk.Entry(GUI, textvariable=Quantity,font=(None,18))
EQuantity.grid(row=2,column=1,padx=10,pady=10)
#------------------Row3------------------------------
# This is Button
Badd = ttk.Button(GUI, text='Add',command=Addproduct)
Badd.grid(row=3,column=1,padx=10,pady=10)

#Create Result Label
Res = StringVar()
Res.set('Result')

#fg is foreground fg for Label not ttk.Label
RLRes = ttk.Label(GUI, textvariable=Res,font=(None,18,'bold'),foreground='green')  
RLRes.grid(row=4,column=1,padx=10,pady=10)

GUI.mainloop()
