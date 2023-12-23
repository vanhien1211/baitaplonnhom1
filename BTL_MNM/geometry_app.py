import tkinter as tk
from tkinter import messagebox
import math

entry_chieu_dai = None
entry_chieu_rong = None
entry_canh_hinh_vuong = None
entry_canh_hinh_tron = None
entry_dai = None
entry_rong = None
entry_cao = None
label_ket_qua = None


def hien_cua_so_hinh_chu_nhat():
    global entry_chieu_dai, entry_chieu_rong, label_ket_qua

    cua_so_hinh_chu_nhat = tk.Toplevel(root)
    cua_so_hinh_chu_nhat.title("Tính Diện Tích và Chu Vi Hình Chữ Nhật")

    label_chieu_dai = tk.Label(cua_so_hinh_chu_nhat, text="Chiều Dài:")
    label_chieu_rong = tk.Label(cua_so_hinh_chu_nhat, text="Chiều Rộng:")
    entry_chieu_dai = tk.Entry(cua_so_hinh_chu_nhat)
    entry_chieu_rong = tk.Entry(cua_so_hinh_chu_nhat)
    button_tinh_dien_tich = tk.Button(cua_so_hinh_chu_nhat, text="Tính Diện Tích", command=lambda: tinh_dien_tich("hình chữ nhật"))
    button_tinh_chu_vi = tk.Button(cua_so_hinh_chu_nhat, text="Tính Chu Vi", command=lambda: tinh_chu_vi("hình chữ nhật"))
    label_ket_qua = tk.Label(cua_so_hinh_chu_nhat, text="Kết Quả: ")

    label_chieu_dai.grid(row=0, column=0)
    entry_chieu_dai.grid(row=0, column=1)
    label_chieu_rong.grid(row=1, column=0)
    entry_chieu_rong.grid(row=1, column=1)
    button_tinh_dien_tich.grid(row=2, column=0, columnspan=2)
    button_tinh_chu_vi.grid(row=3, column=0, columnspan=2)
    label_ket_qua.grid(row=4, column=0, columnspan=2)

    # Hiển thị công thức
    label_cong_thuc_dien_tich = tk.Label(cua_so_hinh_chu_nhat, text="Diện tích (S) = Chiều Dài * Chiều Rộng")
    label_cong_thuc_chu_vi = tk.Label(cua_so_hinh_chu_nhat, text="Chu vi (P) = 2 * (Chiều Dài + Chiều Rộng)")

    label_cong_thuc_dien_tich.grid(row=5, column=0, columnspan=2)
    label_cong_thuc_chu_vi.grid(row=6, column=0, columnspan=2)
def hien_cua_so_hinh_hop_chu_nhat():
    global entry_dai, entry_rong,entry_cao, label_ket_qua

    cua_so_hinh_hop_chu_nhat = tk.Toplevel(root)
    cua_so_hinh_hop_chu_nhat.title("Tính Diện Tích và Thể Tích Hình Hộp Chữ Nhật")

    label_dai = tk.Label(cua_so_hinh_hop_chu_nhat, text="Chiều Dài (a):")
    label_rong = tk.Label(cua_so_hinh_hop_chu_nhat, text="Chiều Rộng (b):")
    label_cao = tk.Label(cua_so_hinh_hop_chu_nhat, text="Chiều Cao (h):")
    entry_dai = tk.Entry(cua_so_hinh_hop_chu_nhat)
    entry_rong = tk.Entry(cua_so_hinh_hop_chu_nhat)
    entry_cao = tk.Entry(cua_so_hinh_hop_chu_nhat)
    button_tinh_dien_tich = tk.Button(cua_so_hinh_hop_chu_nhat, text="Tính Diện Tích", command=lambda: tinh_dien_tich("hình hộp chữ nhật"))
    button_tinh_the_tich= tk.Button(cua_so_hinh_hop_chu_nhat, text="Tính Thể Tích", command=lambda: tinh_chu_vi("hình hộp chữ nhật"))
    label_ket_qua = tk.Label(cua_so_hinh_hop_chu_nhat, text="Kết Quả: ")

    label_dai.grid(row=0, column=0)
    entry_dai.grid(row=0, column=1)
    label_rong.grid(row=1, column=0)
    entry_rong.grid(row=1, column=1)
    label_cao.grid(row=2, column=0)
    entry_cao.grid(row=2, column=1)
    button_tinh_dien_tich.grid(row=3, column=0, columnspan=2)
    button_tinh_the_tich.grid(row=4, column=0, columnspan=2)
    label_ket_qua.grid(row=5, column=0, columnspan=2)

    # Hiển thị công thức
    label_cong_thuc_dien_tich_xq = tk.Label(cua_so_hinh_hop_chu_nhat,
                                            text="Diện tích Xung Quanh (S) = 2h * (a + b) ")
    label_cong_thuc_dien_tich_tp = tk.Label(cua_so_hinh_hop_chu_nhat,
                                            text="Diện tích Toàn Phần (S) = 2h * (a + b) + 2ab ")
    label_cong_thuc_the_tich = tk.Label(cua_so_hinh_hop_chu_nhat,
                                        text="Thể Tích (V) = a * b * h")

    label_cong_thuc_dien_tich_xq.grid(row=6, column=0, columnspan=2)
    label_cong_thuc_dien_tich_tp.grid(row=7, column=0, columnspan=2)
    label_cong_thuc_the_tich.grid(row=8, column=0, columnspan=2)
def hien_cua_so_hinh_vuong():
    global entry_canh_hinh_vuong, label_ket_qua

    cua_so_hinh_vuong = tk.Toplevel(root)
    cua_so_hinh_vuong.title("Tính Diện Tích và Chu Vi Hình Vuông")

    label_canh_hinh_vuong = tk.Label(cua_so_hinh_vuong, text="Cạnh:")
    entry_canh_hinh_vuong = tk.Entry(cua_so_hinh_vuong)
    button_tinh_dien_tich = tk.Button(cua_so_hinh_vuong, text="Tính Diện Tích", command=lambda: tinh_dien_tich("hình vuông"))
    button_tinh_chu_vi = tk.Button(cua_so_hinh_vuong, text="Tính Chu Vi", command=lambda: tinh_chu_vi("hình vuông"))
    label_ket_qua = tk.Label(cua_so_hinh_vuong, text="Kết Quả: ")

    label_canh_hinh_vuong.grid(row=0, column=0)
    entry_canh_hinh_vuong.grid(row=0, column=1)
    button_tinh_dien_tich.grid(row=1, column=0, columnspan=2)
    button_tinh_chu_vi.grid(row=2, column=0, columnspan=2)
    label_ket_qua.grid(row=3, column=0, columnspan=2)

    # Hiển thị công thức
    label_cong_thuc_dien_tich = tk.Label(cua_so_hinh_vuong, text="Diện tích (S) = Cạnh * Cạnh")
    label_cong_thuc_chu_vi = tk.Label(cua_so_hinh_vuong, text="Chu vi (P) = 4 * Cạnh")

    label_cong_thuc_dien_tich.grid(row=4, column=0, columnspan=2)
    label_cong_thuc_chu_vi.grid(row=5, column=0, columnspan=2)
def hien_cua_so_hinh_tron():
    global entry_canh_hinh_tron, label_ket_qua

    cua_so_hinh_tron = tk.Toplevel(root)
    cua_so_hinh_tron.title("Tính Diện Tích và Chu Vi Hình Vuông")

    label_canh_hinh_tron = tk.Label(cua_so_hinh_tron, text="Bán Kính:")
    entry_canh_hinh_tron = tk.Entry(cua_so_hinh_tron)
    button_tinh_dien_tich = tk.Button(cua_so_hinh_tron, text="Tính Diện Tích", command=lambda: tinh_dien_tich("hình tròn"))
    button_tinh_chu_vi = tk.Button(cua_so_hinh_tron, text="Tính Chu Vi", command=lambda: tinh_chu_vi("hình tròn"))
    label_ket_qua = tk.Label(cua_so_hinh_tron, text="Kết Quả: ")

    label_canh_hinh_tron.grid(row=0, column=0)
    entry_canh_hinh_tron.grid(row=0, column=1)
    button_tinh_dien_tich.grid(row=1, column=0, columnspan=2)
    button_tinh_chu_vi.grid(row=2, column=0, columnspan=2)
    label_ket_qua.grid(row=3, column=0, columnspan=2)

    # Hiển thị công thức
    label_cong_thuc_dien_tich = tk.Label(cua_so_hinh_tron, text="Diện tích (S) = π * (Bán Kính)^2")
    label_cong_thuc_chu_vi = tk.Label(cua_so_hinh_tron, text="Chu vi (P) = 2 * π * Bán Kính")

    label_cong_thuc_dien_tich.grid(row=4, column=0, columnspan=2)
    label_cong_thuc_chu_vi.grid(row=5, column=0, columnspan=2)
def tinh_dien_tich(loai_hinh):
    try:
        if loai_hinh == "hình chữ nhật":
            chieu_dai = float(entry_chieu_dai.get())
            chieu_rong = float(entry_chieu_rong.get())
            if chieu_rong <= 0 or chieu_dai <= 0 or chieu_dai <= chieu_rong:
                messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")
            else:
                dien_tich = chieu_dai * chieu_rong
                label_ket_qua.config(text=f"Diện tích (S): {dien_tich}")
        elif loai_hinh == "hình hộp chữ nhật":
            dai = float(entry_dai.get())
            rong = float(entry_rong.get())
            cao = float(entry_cao.get())

            if rong <= 0 or dai <= 0 or cao <= 0 or dai <= rong:
                messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")
            else:
                dien_tich_xq = 2 * cao * (rong + dai)
                dien_tich_tp = 2 * cao * (rong + dai) + 2 * dai * rong
                label_ket_qua.config(text=f"Diện tích Xung Quanh (Sxq): {dien_tich_xq} \n "
                                          f"Diện tích Toàn Phần (Stp): {dien_tich_tp}")
        elif loai_hinh == "hình vuông":
            canh = float(entry_canh_hinh_vuong.get())
            if canh <= 0:
                messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")
            else:
                dien_tich = canh * canh
                label_ket_qua.config(text=f"Diện tích (S): {dien_tich}")
        elif loai_hinh == "hình tròn":
            ban_kinh = float(entry_canh_hinh_tron.get())
            if ban_kinh <= 0:
                messagebox.showerror("Lỗi", "Hãy nhâp lại số liệu !")
            else:
                dien_tich = math.pi * (ban_kinh ** 2)
                label_ket_qua.config(text=f"Diện tích (S): {dien_tich}")
    except ValueError:
        messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")

def tinh_chu_vi(loai_hinh):
    try:
        if loai_hinh == "hình chữ nhật":
            chieu_dai = float(entry_chieu_dai.get())
            chieu_rong = float(entry_chieu_rong.get())
            if chieu_rong <= 0 or chieu_dai <= 0 or chieu_dai <= chieu_rong:
                messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")
            else:
                chu_vi = 2 * (chieu_dai + chieu_rong)
                label_ket_qua.config(text=f"Chu vi (P): {chu_vi}")
        elif loai_hinh == "hình hộp chữ nhật":
            dai = float(entry_dai.get())
            rong = float(entry_rong.get())
            cao = float(entry_cao.get())
            if rong <= 0 or dai <= 0 or cao <= 0 or dai <= rong:
                messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")
            else:
                the_tich = dai * rong * cao
                label_ket_qua.config(text=f"Thể Tích (V): {the_tich}")
        elif loai_hinh == "hình vuông":
            canh = float(entry_canh_hinh_vuong.get())
            if canh <= 0:
                messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")
            else:
                chu_vi = 4 * canh
                label_ket_qua.config(text=f"Chu vi (P): {chu_vi}")
        elif loai_hinh == "hình tròn":
            ban_kinh = float(entry_canh_hinh_tron.get())
            if ban_kinh <= 0:
                messagebox.showerror("Lỗi", "Hãy nhâp lại số liệu !")
            else:
                chu_vi = 2 * math.pi * ban_kinh
                label_ket_qua.config(text=f"Chu vi (P): {chu_vi}")
    except ValueError:
        messagebox.showerror("Lỗi", "Hãy nhập lại số liệu !")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Chương Trình Hình Học")

# Tạo nút để mở cửa sổ hình chữ nhật
button_hinh_chu_nhat = tk.Button(root, text="Hình Chữ Nhật", command=hien_cua_so_hinh_chu_nhat)
button_hinh_chu_nhat.pack(pady=20)

# Tạo nút để mở cửa sổ hình vuông
button_hinh_vuong = tk.Button(root, text="Hình Vuông", command=hien_cua_so_hinh_vuong)
button_hinh_vuong.pack(pady=20)

# Tạo nút để mở cửa sổ hình tròn
button_hinh_tron = tk.Button(root, text="Hình Tròn", command=hien_cua_so_hinh_tron)
button_hinh_tron.pack(pady=20)

# Tạo nút để mở cửa sổ hình hộp chữ nhật
button_hinh_hop_chu_nhat = tk.Button(root, text="Hình Hộp Chữ Nhật", command=hien_cua_so_hinh_hop_chu_nhat)
button_hinh_hop_chu_nhat.pack(pady=20)

# Chạy ứng dụng
root.mainloop()