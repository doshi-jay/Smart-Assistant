import tkinter as tk
from tkinter import scrolledtext
from tkinter import *

root = tk.Tk()

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, side=tk.TOP)

hello_label = Label(button_frame, text="Welcome User!")
hello_label.configure(font=("Cambria", 12))
help_button = tk.Button(button_frame, text='Help', bg="black", fg="white")

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

hello_label.grid(row=0, column=0, sticky=tk.W, padx=10)
help_button.grid(row=0, column=1, sticky=tk.E+tk.W, padx=10, pady=10)

txt = scrolledtext.ScrolledText(root, width=60,height=10)
txt.insert(tk.INSERT,'Please enter the command!')
txt.pack()
txt.focus()

submit_frame = tk.Frame(root)
submit_frame.pack(fill=tk.X)

submit_frame.columnconfigure(0, weight=1)

submit_button = tk.Button(submit_frame, text='Submit', bg="black", fg="white")
submit_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx = 60, pady=10)

output = scrolledtext.ScrolledText(root, width=60,height=10)
output.insert(tk.INSERT,'Output:\n')
output.pack()

root.mainloop()