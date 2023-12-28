import tkinter as tk
import subprocess

def open_basic_calculator():
    # Chạy mã code giao diện máy tính cơ bản từ một tệp riêng
    subprocess.call(["python", "basic_calculator.py"])

def open_analysis_app():
    # Chạy mã code giao diện ứng dụng hỗ trợ giải tích từ một tệp riêng
    subprocess.call(["python", "analysis_app.py"])

# Tạo cửa sổ chính
window = tk.Tk()
window.config(bg='lightblue')
# Thiết lập giao diện chính
label = tk.Label(window, text="Chọn ứng dụng:",bg='lightgreen')
label.pack()

# Tạo các nút lựa chọn
button_basic_calculator = tk.Button(window, text="Máy tính cơ bản", command=open_basic_calculator,bg='yellow')
button_basic_calculator.pack()

button_analysis_app = tk.Button(window, text="Ứng dụng hỗ trợ giải tích", command=open_analysis_app,bg='yellow')
button_analysis_app.pack()

# Chạy giao diện
window.mainloop()
