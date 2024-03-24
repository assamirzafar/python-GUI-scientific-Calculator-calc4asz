import tkinter as tk
import math




def square_root():
    try:
        expression = display_label['text']
        result = math.sqrt(eval(expression))
        display_label['text'] = str(result)
    except Exception as e:
        print(e)
        display_label['text'] = 'Error'

# Function to update the display
def update_display(value):
    current_text = display_label['text']
  
    if current_text == '0' or current_text == 'Error':
        display_label['text'] = value
    elif value in ('π', 'e') and current_text[-1].isdigit():
        display_label['text'] += ' * ' + value
    elif value == '^' and current_text[-1].isdigit():
        display_label['text'] += '^'
    elif value == '10^' and current_text[-1].isdigit():
        display_label['text'] += '10^'
    else:
        display_label['text'] += value



# Function to handle keyboard input
def on_key(event):
    key = event.char
    if key.isdigit() or key in ['+', '-', '*', '/', '.', '(', ')','^']:
        update_display(key)
    elif key.lower() == 'p':
        update_display('π')
    elif key.lower() == 'e':
        update_display('e')
    elif key.lower() == 's':
        update_display('sin(')
    elif key.lower() == 'c':
        update_display('cos(')
    elif key.lower() == 't':
        update_display('tan(')
    elif key == '\x08':
        clear()
    elif key == '\r':  # '\r' represents the Enter key
        calculate()

    

# Function to calculate the expression
def calculate():
    try:
        expression = display_label['text']
        expression = expression.replace('π', str(math.pi))
        expression = expression.replace('e', str(math.e))
        
        expression = expression.replace('^', '**')
        expression = expression.replace('10^', "10**")
        
        expression = expression.replace('sin', 'math.sin')
        expression = expression.replace('cos', 'math.cos')
        expression = expression.replace('tan', 'math.tan')
        result = eval(expression)
 

        # Round the result to 10 decimal places
        rounded_result = round(result, 10)
        display_label['text'] = str(rounded_result)
    except Exception as e:
        print(e)
        display_label['text'] = 'Error'

# Function to clear the display
def clear():
    current_text = display_label['text']
    if current_text == 'Error':
        display_label['text'] = '0'
    elif current_text.endswith(('sin(', 'cos(', 'tan(')):
        display_label['text'] = current_text[:-4]
    elif len(current_text) > 1:
        display_label['text'] = current_text[:-1]
    else:
        display_label['text'] = '0'


def trig_function(func):
    try:
        expression = display_label['text']
        if func == 'sin':
            update_display('sin(')
        elif func == 'cos':
            update_display('cos(')
        elif func == 'tan':
            update_display('tan(')
        
    except Exception as e:
        print(e)
        display_label['text'] = 'Error'


def logarithm(base):
    try:
        expression = display_label['text']
        result = math.log(eval(expression), base)
        display_label['text'] = str(result)
    except:
        display_label['text'] = 'Error'

def factorial():
    try:
        expression = display_label['text']
        n = int(eval(expression))
        result = math.factorial(n)
        display_label['text'] = str(result)
    except:
        display_label['text'] = 'Error'

                                                            ### GUI ###                               

root = tk.Tk()
root.title('Scientific Calculator')

root.geometry("485x605")
root.resizable(width=False, height=False)
root.configure(bg="black")

display_label = tk.Label(root, text='0', font=('Helvetica', 24), width=24, height=3, bg='black', fg='white', anchor='e')
display_label.grid(row=0, column=0, columnspan=10)

number_keys = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2),
    ('0', 5, 0), ('.', 5, 1),("10^", 5 , 2)
]

function_keys = [
    ('/', 5, 3), ('*', 4, 3), ('-', 3, 3), ('+', 2, 3),
    ('=', 3, 6), ('C', 2, 6), ('√', 4, 6), ('^', 5, 6), ('sin', 2, 4),
    ('cos', 4, 4), ('tan', 3, 4), ('ln', 2, 5), ('log10', 5, 4),
    ('π', 3, 5), ('e', 4, 5), ('x!', 5, 5)
]

for (text, row, col) in number_keys:
    button = tk.Button(root, text=text, font=('Helvetica', 10), width=8, height=7, bg='black', fg='white', command=lambda value=text: update_display(value))
    button.grid(row=row, column=col)

for (text, row, col) in function_keys:
    if text == '=':
        button = tk.Button(root, text=text, font=('Helvetica', 10), width=7, height=7, bg='blue', fg='white', command=calculate)
        button.grid(row=row, column=col)
    elif text in ('√', '^', 'sin', 'cos', 'tan', 'ln', 'log10', 'x!'):
        button = tk.Button(root, text=text, font=('Helvetica', 10), width=7, height=7, bg='green', fg='white')
        
        if text in ('sin', 'cos', 'tan'):
            button.config(command=lambda func=text: trig_function(func))
        elif text == 'ln':
            button.config(command=lambda base=math.e: logarithm(base))
        elif text == 'log10':
            button.config(command=lambda base=10: logarithm(base))
        elif text == 'x!':
            button.config(command=factorial)
        elif text == '√':
            button.config(command=square_root)
        elif text == "^":
            button.config(command=lambda value=text : update_display(value))
    elif text == 'C':
        button = tk.Button(root, text=text, font=('Helvetica', 10), width=7, height=7, bg='green', fg='white')
        button.config(command=clear)
    elif text == 'π':
        button = tk.Button(root, text=text, font=('Helvetica', 10), width=7, height=7, bg='green', fg='white', command=lambda: update_display('π'))
    elif text == 'e':
        button = tk.Button(root, text=text, font=('Helvetica', 10), width=7, height=7, bg='green', fg='white', command=lambda: update_display('e'))
    elif text == '10^':
        button = tk.Button(root, text=text, font=('Helvetica', 10), width=7, height=7, bg='green', fg='white', command=lambda: update_display('10^'))
        button.config(command=lambda value=text : update_display(value))
    else:
        button = tk.Button(root, text=text, font=('Helvetica', 10), width=7, height=7, bg='green', fg='white', command=lambda val=text: update_display(val))
    button.grid(row=row, column=col)

root.bind('<Key>', on_key)
root.mainloop()
