import tkinter as tk
from tkinter import scrolledtext
from tkinter import *

# Importing the controller for interaction
from controller import Controller

ENTER_COMMAND = "Please enter the command:"
OUTPUT = "Output:\n"
TITLE = "Smart Assistant!"
WELCOME_TEXT = "Welcome User!"


def get_help_heading(help_window):
	help_heading_frame = tk.Frame(help_window)
	help_heading_frame.pack(fill=tk.X)

	help_heading_frame.columnconfigure(0, weight=1)

	help_heading_label = Label(help_heading_frame, text='----------   HELP   ----------')
	help_heading_label.configure(font=("Cambria", 14))
	help_heading_label.grid(row=0, column=0, sticky=tk.W+tk.E, padx = 60, pady=10)

def open_help():
	help_window = tk.Toplevel(root)

	get_help_heading(help_window)

	calculator_frame = tk.Frame(help_window)
	calculator_frame.pack(fill=tk.X)
	
	calculator_key = Label(calculator_frame, text = "> To perform arithmetic calculations    |")
	calculator_value = Label(calculator_frame, text="Calculator: <operand> <operator> <operand>")

	calculator_frame.columnconfigure(0, weight=1)	
	calculator_frame.columnconfigure(1, weight=1)

	calculator_key.grid(row=0, column=0, sticky=tk.W, padx=10)
	calculator_value.grid(row=0, column=1, sticky=tk.E+tk.W, padx=10, pady=10)


def process_input(input_text):
	# This is where the call to the controller must be made
	controller = Controller()
	return controller.interface(input_text.lower())


def control():
	input_text = txt.get(1.0, END)
	if input_text.split(ENTER_COMMAND)[0] != "":
		result = "Please enter the command in the proper format!"
	else:		
		input_text = "".join(input_text.split(ENTER_COMMAND)[1:]).lstrip()
		result = process_input(input_text)
	update_output(input_text, result)
	refresh_input_box()
	

def update_output(input_text, result):
	output_text = "User: " + input_text + "\n" + "SAss: " + str(result) + "\n"
	output.configure(state=tk.NORMAL)
	output.insert(tk.INSERT, "User: " + input_text.rstrip() + "\n", "input")
	output.insert(tk.INSERT, "SAss: " + str(result).rstrip() + "\n", "output")
	output.tag_config('input', foreground='darkblue')
	output.tag_config('output', foreground='green')
	output.configure(state=tk.DISABLED)


def refresh_input_box():
	txt.delete(1.0, END)
	txt.insert(tk.INSERT,ENTER_COMMAND)



root = tk.Tk()
root.title(TITLE)

button_frame = tk.Frame(root)
button_frame.pack(fill=tk.X, side=tk.TOP)

hello_label = Label(button_frame, text=WELCOME_TEXT)
hello_label.configure(font=("Cambria", 11))
help_button = tk.Button(button_frame, text='Help', bg="black", fg="white", command = open_help)

button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)

hello_label.grid(row=0, column=0, sticky=tk.W, padx=10)
help_button.grid(row=0, column=1, sticky=tk.E+tk.W, padx=10, pady=10)

txt = scrolledtext.ScrolledText(root,height=10)
txt.insert(tk.INSERT, ENTER_COMMAND)
txt.focus()
txt.pack()

submit_frame = tk.Frame(root)
submit_frame.pack(fill=tk.X)

submit_frame.columnconfigure(0, weight=1)

submit_button = tk.Button(submit_frame, text='Submit', bg="black", fg="white", command = control)
submit_button.grid(row=0, column=0, sticky=tk.W+tk.E, padx = 60, pady=10)

output = scrolledtext.ScrolledText(root, height=15)
output.insert(tk.INSERT, OUTPUT)
output.configure(state=tk.DISABLED, bg="#d9dbdd")
output.pack()

root.mainloop()