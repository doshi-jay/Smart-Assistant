import tkinter as tk
from tkinter import scrolledtext
from tkinter import *

# Importing the controller for interaction
import controller

def process_input(input_text):
	# This is where the call to the controller must be made
	return input_text


def control():
	input_text = txt.get(1.0, END)
	if input_text.split("Please enter the command!")[0] != "":
		result = "Please enter the command in the proper format!"
	else:		
		input_text = "".join(input_text.split('Please enter the command!')[1:]).lstrip()
		result = process_input(input_text)
	update_output(input_text, result)
	refresh_input_box()
	

def update_output(input_text, result):
	output_text = "User: " + input_text + "\n" + "SAss: " + result + "\n"
	output.configure(state=tk.NORMAL)
	output.insert(tk.INSERT, "User: " + input_text.rstrip() + "\n", "input")
	output.insert(tk.INSERT, "SAss: " + result.rstrip() + "\n", "output")
	output.tag_config('input', foreground='darkblue')
	output.tag_config('output', foreground='green')
	output.configure(state=tk.DISABLED)


def refresh_input_box():
	txt.delete(1.0, END)
	txt.insert(tk.INSERT,'Please enter the command!\n')



root = tk.Tk()
root.title("Smart Assistant!")

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, side=tk.TOP)

hello_label = Label(button_frame, text="Welcome User!")
hello_label.configure(font=("Cambria", 11))
help_button = tk.Button(button_frame, text='Help', bg="black", fg="white")

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

hello_label.grid(row=0, column=0, sticky=tk.W, padx=10)
help_button.grid(row=0, column=1, sticky=tk.E+tk.W, padx=10, pady=10)

txt = scrolledtext.ScrolledText(root,height=10)
txt.insert(tk.INSERT,'Please enter the command!\n')
txt.focus()
txt.pack()

submit_frame = tk.Frame(root)
submit_frame.pack(fill=tk.X)

submit_frame.columnconfigure(0, weight=1)

submit_button = tk.Button(submit_frame, text='Submit', bg="black", fg="white", command = control)
submit_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx = 60, pady=10)

output = scrolledtext.ScrolledText(root, height=15)
output.insert(tk.INSERT,'Output:\n')
output.configure(state=tk.DISABLED, bg="#d9dbdd")
output.pack()

root.mainloop()