from tkinter import *

# Global variables for calculation
first_number = second_number = operator = None

def get_digit(digit):
    """Handles number input and updates display."""
    current = result_label['text']
    if current == "0" or current == "Error":  
        current = ""  
    new = current + str(digit)
    result_label.config(text=new)

def clear():
    """Clears the display."""
    result_label.config(text="0")

def get_operator(op):
    """Handles operator selection."""
    global first_number, operator
    try:
        first_number = int(result_label['text'])
        operator = op
        result_label.config(text="")
    except ValueError:
        result_label.config(text="Error")

def get_result():
    """Performs calculation and displays result."""
    global first_number, second_number, operator
    try:
        second_number = int(result_label['text'])
        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            result = "Error" if second_number == 0 else round(first_number / second_number, 2)
        else:
            result = "Error"
        
        result_label.config(text=str(result))
    except (ValueError, TypeError):
        result_label.config(text="Error")

# Initialize Tkinter window
root = Tk()
root.title('Calculator')
root.geometry('280x380')
root.resizable(0, 0)
root.configure(background='black')

# Display Label
result_label = Label(root, text="0", bg="black", fg='white', anchor='e', padx=10)
result_label.grid(row=0, column=0, columnspan=4, pady=(20, 10), sticky="ew")
result_label.config(font=('Verdana', 30, 'bold'))

# Button Configuration
button_config = {
    "width": 5, "height": 2, "font": ('Verdana', 14),
}

buttons = [
    ('7', 1, 0, '#32CD32'), ('8', 1, 1, '#32CD32'), ('9', 1, 2, '#32CD32'), ('+', 1, 3, '#FF6347'),
    ('4', 2, 0, '#32CD32'), ('5', 2, 1, '#32CD32'), ('6', 2, 2, '#32CD32'), ('-', 2, 3, '#FF6347'),
    ('1', 3, 0, '#32CD32'), ('2', 3, 1, '#32CD32'), ('3', 3, 2, '#32CD32'), ('*', 3, 3, '#FF6347'),
    ('C', 4, 0, '#DC143C'), ('0', 4, 1, '#32CD32'), ('=', 4, 2, '#1E90FF'), ('/', 4, 3, '#FF6347')
]

for text, row, col, color in buttons:
    if text in "+-*/=":
        btn = Button(root, text=text, bg=color, fg='white', command=lambda t=text: get_operator(t) if t != "=" else get_result(), **button_config)
    elif text == "C":
        btn = Button(root, text=text, bg=color, fg='white', command=clear, **button_config)
    else:
        btn = Button(root, text=text, bg=color, fg='white', command=lambda t=text: get_digit(t), **button_config)

    btn.grid(row=row, column=col)

root.mainloop()