import tkinter as tk
import subprocess

def open_basic_calculator():
    # Chạy mã code giao diện máy tính cơ bản từ một tệp riêng
    subprocess.call(["python", "basic_calculator.py"])

def open_analysis_app():
    # Chạy mã code giao diện ứng dụng hỗ trợ giải tích từ một tệp riêng
    subprocess.call(["python", "analysis_app.py"])

def open_geometry_app():
    # Chạy mã code giao diện ứng dụng hỗ trợ hình học từ một tệp riêng
    subprocess.call(["python", "geometry_app.py"])

# Tạo cửa sổ chính
root = tk.Tk()
root.config(bg='lightblue')
# Thiết lập giao diện chính
label = tk.Label(root, text="Chọn ứng dụng:",bg='lightgreen')
label.pack()

# Tạo các nút lựa chọn
button_basic_calculator = tk.Button(root, text="Máy tính cơ bản", command=open_basic_calculator,bg='yellow')
button_basic_calculator.pack()

button_analysis_app = tk.Button(root, text="Ứng dụng hỗ trợ giải tích", command=open_analysis_app,bg='yellow')
button_analysis_app.pack()

button_geometry_app = tk.Button(root, text="Ứng dụng hỗ trợ hình học", command=open_geometry_app,bg='yellow')
button_geometry_app.pack()

# Chạy giao diện
root.mainloop()
