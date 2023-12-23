import tkinter as tk

def add():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 + num2
    label_result.config(text=f"Result: {result}")

def subtract():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 - num2
    label_result.config(text=f"Result: {result}")

def multiply():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 * num2
    label_result.config(text=f"Result: {result}")

def divide():
    num1 = float(entry_num1.get())
    num2 = float(entry_num2.get())
    result = num1 / num2
    label_result.config(text=f"Result: {result}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Basic Calculator")

# Tạo các thành phần giao diện
label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

button_add = tk.Button(root, text="Add", command=add)
button_add.grid(row=2, column=0)

button_subtract = tk.Button(root, text="Subtract", command=subtract)
button_subtract.grid(row=2, column=1)

button_multiply = tk.Button(root, text="Multiply", command=multiply)
button_multiply.grid(row=3, column=0)

button_divide = tk.Button(root, text="Divide", command=divide)
button_divide.grid(row=3, column=1)

label_result = tk.Label(root, text="Result: ")
label_result.grid(row=4, column=0, columnspan=2)

# Chạy giao diện
root.mainloop()