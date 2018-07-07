import tkinter as tk

mainWindow = tk.Tk()

expression = ''
ex1 =''
ex2=''
var1 = 0
var2 = 0
i=0
ans = 0
op = ''
s =''
ind = 0

label1=tk.Label(mainWindow,text ="CALCULATOR")
label1.config(bg = 'white',font=('Castellar',20,'bold'),fg='black')
label1.grid(row = 1,columnspan = 4, padx=100,pady=5,ipadx=5,ipady=5)

def clear():
    global  expression
    expression =''
    labels.config(text=expression)

def asciconvert(op):
    global str
    str = op
    n =[ord(c) for c in op]
    printNo(n[0])

def error():
    labels.config(text='enter values before operator')

def printNo(num):
    global labels
    global expression
    k = 0
    ifs = 0
    list = [42,43,45,47]
    for j in range (0,4):
        if (num == list[j]):
            k = j
            ifs = 99
            break
    if ( ifs == 99):
        s = chr(list[j])
        expression = (expression + s)
    else:
        expression = (expression + '%d' %num)
    labels.config(text=expression)

def equalto():
    global expression
    global var1
    global var2
    global ans
    global ex1
    global ex2
    global i
    global str
    global ind
    i=expression.find(str)
    ex1 = (expression[:i])
    if(ex1 == ''):
        error()
    var1 = int(ex1)
    ex2 = (expression[i+1:])
    var2 = int(ex2)
    expression=''

    if(str == '+'):
        ans = var1 + var2
    elif (str == '*'):
        ans = var1 * var2
    elif (str == '/'):
        if(var2==0):
            ind = 1
        else:
            ans = var1 / var2
    elif (str == '-'):
        ans = var1 - var2

    expression = (expression + '%d' %ans)

    if (ind == 1):
        labels.config(text='Error')
    else:
        labels.config(text=expression)
        expression = ''


labels = tk.Button(mainWindow,height = 2, width = 50,relief ='sunken',borderwidth = 5)
labels.grid(row=2,columnspan = 4,padx=5,pady=5,ipadx=5,ipady=5)

button1 = tk.Button(mainWindow,text = '1',height = 2, width = 5,command = lambda:printNo(1))
button1.grid(row=3,column = 0,padx=5,pady=5,ipadx=5,ipady=5)
button2 = tk.Button(mainWindow,text = '2',height = 2, width = 5,command = lambda:printNo(2))
button2.grid(row=3,column = 1,padx=5,pady=5,ipadx=5,ipady=5)
button3 = tk.Button(mainWindow,text = '3',height = 2, width = 5,command = lambda:printNo(3))
button3.grid(row=3,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
buttonadd = tk.Button(mainWindow,text = '+',height = 2, width = 5, command= lambda: asciconvert('+'))
buttonadd.grid(row=4,column = 3,padx=5,pady=5,ipadx=5,ipady=5)

button4 = tk.Button(mainWindow,text = '4',height = 2, width = 5,command = lambda:printNo(4))
button4.grid(row=4,column = 0,padx=5,pady=5,ipadx=5,ipady=5)
button5 = tk.Button(mainWindow,text = '5',height = 2, width = 5,command = lambda:printNo(5))
button5.grid(row=4,column = 1,padx=5,pady=5,ipadx=5,ipady=5)
button6 = tk.Button(mainWindow,text = '6',height = 2, width = 5,command = lambda:printNo(6))
button6.grid(row=4,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
buttonsub = tk.Button(mainWindow,text = '-',height = 2, width = 5,command= lambda: asciconvert('-'))
buttonsub.grid(row=5,column = 3,padx=5,pady=5,ipadx=5,ipady=5)

button7 = tk.Button(mainWindow,text = '7',height = 2, width = 5,command = lambda:printNo(7))
button7.grid(row=5,column = 0,padx=5,pady=5,ipadx=5,ipady=5)
button8 = tk.Button(mainWindow,text = '8',height = 2, width = 5,command = lambda:printNo(8))
button8.grid(row=5,column = 1,padx=5,pady=5,ipadx=5,ipady=5)
button9 = tk.Button(mainWindow,text = '9',height = 2, width = 5,command = lambda:printNo(9))
button9.grid(row=5,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
buttonmul = tk.Button(mainWindow,text = '*',height = 2, width = 5,command= lambda: asciconvert('*'))
buttonmul.grid(row=6,column = 0,padx=5,pady=5,ipadx=5,ipady=5)

button0 = tk.Button(mainWindow,text = '0',height = 2, width = 5,command = lambda:printNo(0))
button0.grid(row=6,column = 1,padx=5,pady=5,ipadx=5,ipady=5)
buttondiv = tk.Button(mainWindow,text = '/',height = 2, width = 5,command= lambda: asciconvert('/'))
buttondiv.grid(row=6,column = 2,padx=5,pady=5,ipadx=5,ipady=5)
buttonac = tk.Button(mainWindow,text = 'CLR',height = 2, width = 5, command = lambda:clear() )
buttonac.grid(row=3, column= 3, padx=5,pady=5,ipadx=5,ipady=5)
buttonc = tk.Button(mainWindow,text = '=',height = 2, width = 5, command = lambda:equalto() )
buttonc.grid(row=6, column= 3, padx=5,pady=5,ipadx=5,ipady=5)
mainWindow.mainloop()
