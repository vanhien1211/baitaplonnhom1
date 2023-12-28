import tkinter as tk
import subprocess
from concurrent.futures import ThreadPoolExecutor

def open_basic_calculator():
    subprocess.call(["python", "basic_calculator.py"])

def open_analysis_app():
    subprocess.call(["python", "analysis_app.py"])

def open_app_with_executor(executor, app_function):
    executor.submit(app_function)

window = tk.Tk()
window.resizable(width=False, height=False)

label = tk.Label(window, text="Chọn ứng dụng:")
label.pack()

executor = ThreadPoolExecutor()

button_basic_calculator = tk.Button(window, text="Máy tính cơ bản", command=lambda: open_app_with_executor(executor, open_basic_calculator))
button_basic_calculator.pack()

button_analysis_app = tk.Button(window, text="Ứng dụng hỗ trợ giải tích", command=lambda: open_app_with_executor(executor, open_analysis_app))
button_analysis_app.pack()

window.mainloop()

executor.shutdown()
