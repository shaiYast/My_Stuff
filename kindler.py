import tkinter as tk
from tkinter import ttk
from tkinter import *

#

root = tk.Tk()
root.title('V0.0.2')
Height = 700
Width = 800

canvas = tk.Canvas(root, width = Width, height = Height)
canvas.pack()

married= IntVar()

frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=50, rely=10, relwidth=0.75, relheight=1, anchor='n')

button = tk.Button(root, text = "Calculate", bg = 'white', fg = 'black')
button.place(rely=0.3, relx=0.5)

statelabel = tk.Label(root, text = "Which state?", bg = 'white', fg = 'black')
statelabel.place(relwidth = .2, relheight = .05, relx = 0.1, rely = 0.1)

statebox = ttk.Combobox(root)
statebox['values']=('NY','NJ','CT','Other')
statebox.place(relwidth = .2, relheight = .05, relx = 0.3, rely = 0.1)

incomelabel = tk.Label(root, text = "What income?", bg = 'white', fg = 'black')
incomelabel.place(relwidth = .2, relheight = .05, relx = 0.51, rely = 0.1)

incomeentry = tk.Entry(root, font = "Calibri 30", bg = "white", border = 1)
incomeentry.place(relwidth = .2, relheight = .05, relx = 0.71, rely = 0.1)

citylabel = tk.Label(root, text = "Which city?", bg = 'white', fg = 'black')
citylabel.place(relwidth = .2, relheight = .05, relx = 0.1, rely = 0.21)

cityentry = tk.Entry(root, font = "Calibri 30", bg = "white")
cityentry.place(relwidth = .2, relheight = .05, relx = 0.3, rely = 0.21)

marriedlabel = tk.Label(root, text = "Married?", bg = 'white', fg = 'black')
marriedlabel.place(relwidth = .2, relheight = .05, relx = 0.51, rely = 0.21)

marriedcheck = tk.Checkbutton(root, variable = married)
marriedcheck.place(relx = 0.73, rely = 0.22)


root.mainloop()

