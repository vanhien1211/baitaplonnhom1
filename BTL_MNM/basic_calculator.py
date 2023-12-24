import tkinter as tk
from tkinter import messagebox, scrolledtext
from tkinter import filedialog
from docx import Document


def open_word_file():
    file_path = filedialog.askopenfilename(filetypes=[("Word Files", "*.docx"), ("All Files", "*.*")])
    if file_path:
        if not file_path.endswith(".docx"):
            messagebox.showinfo("Cảnh báo", "Vui lòng chỉ chọn tệp Word (định dạng .docx).")
            return

        # Xóa nội dung hiện có trong text widget
        text_widget.delete("1.0", "end")

        # Đọc nội dung từ tệp Word
        doc = Document(file_path)
        content = [paragraph.text for paragraph in doc.paragraphs]
        # Hiển thị nội dung lên giao diện
        for line in content:
            text_widget.insert(tk.END, line + "\n")
        return content
    else:
        messagebox.showinfo("Cảnh báo", "Vui lòng chọn một tệp Word.")

def process_word(content):
    # Lưu trữ kết quả phép tính
    results = []

    for line in content:
    # Kiểm tra nếu dòng là phép tính
        if "+" in line:
            # Phép tính cộng
            operands = line.split("+")
            num1 = float(operands[0].strip())
            num2 = float(operands[1].strip())
            result = num1 + num2
            results.append(f"{num1} + {num2} = {result}")
        elif "-" in line:
            # Phép tính trừ
            operands = line.split("-")
            num1 = float(operands[0].strip())
            num2 = float(operands[1].strip())
            result = num1 - num2
            results.append(f"{num1} - {num2} = {result}")
        elif "*" in line:
            # Phép tính nhân
            operands = line.split("*")
            num1 = float(operands[0].strip())
            num2 = float(operands[1].strip())
            result = num1 * num2
            results.append(f"{num1} * {num2} = {result}")
        elif "/" in line:
            # Phép tính chia
            operands = line.split("/")
            num1 = float(operands[0].strip())
            num2 = float(operands[1].strip())
            result = num1 / num2
            results.append(f"{num1} / {num2} = {result}")
    return results

def save_word_file():
    if text_widget.get("1.0", "end-1c") == "":
        messagebox.showinfo("Cảnh báo", "Không có dữ liệu từ file Word.")
        return

    file_path = filedialog.asksaveasfilename(defaultextension=".docx", filetypes=[("Word Files", "*.docx")])
    if file_path:
        if not file_path.endswith(".docx"):
            messagebox.showinfo("Cảnh báo", "Vui lòng chỉ lưu vào tệp Word (định dạng .docx).")
            return

        content = text_widget.get("1.0", "end-1c").split("\n")
        results = process_word(content)

        # Tạo một tài liệu Word mới
        doc = Document()
        for result in results:
            paragraph = doc.add_paragraph()
            run = paragraph.add_run(result)

        # Lưu tài liệu Word mới
        doc.save(file_path)


def add():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showinfo("Thông báo", "Hãy nhập dữ liệu số")
        return
    result = num1 + num2
    label_result.config(text=f"Kết quả: {result}")


def subtract():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showinfo("Thông báo", "Hãy nhập dữ liệu số")
        return
    result = num1 - num2
    label_result.config(text=f"Kết quả: {result}")


def multiply():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showinfo("Thông báo", "Hãy nhập dữ liệu số")
        return
    result = num1 * num2
    label_result.config(text=f"Kết quả: {result}")


def divide():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showinfo("Thông báo", "Hãy nhập dữ liệu số")
        return
    result = num1 / num2
    label_result.config(text=f"Kết quả: {result}")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Máy tính cơ bản")

# Tạo các thành phần giao diện
label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0)
entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0)
entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

button_open_file = tk.Button(root, text="Chọn tệp Word", command=open_word_file)
button_open_file.grid(row=0, column=2)
button_open_file = tk.Button(root, text="Tính toán Word", command=save_word_file)
button_open_file.grid(row=1, column=2)

button_add = tk.Button(root, text="Cộng", command=add)
button_add.grid(row=2, column=0)

button_subtract = tk.Button(root, text="Trừ ", command=subtract)
button_subtract.grid(row=2, column=1)

button_multiply = tk.Button(root, text="Nhân", command=multiply)
button_multiply.grid(row=3, column=0)

button_divide = tk.Button(root, text="Chia", command=divide)
button_divide.grid(row=3, column=1)

label_result = tk.Label(root, text="Kết quả: ")
label_result.grid(row=4, column=0, columnspan=2)

label_word = tk.Label(root, text="Dữ liệu từ file word:")
label_word.grid(row=5, column=0, columnspan=2)

text_widget = scrolledtext.ScrolledText(root, width=40, height=10)
text_widget.grid(row=6, column=0, columnspan=3)

# Chạy giao diện
root.mainloop()
