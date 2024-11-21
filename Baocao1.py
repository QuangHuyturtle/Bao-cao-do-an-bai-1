import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == "cộng":
            result = num1 + num2
            operation_symbol = "+"
        elif operation == "trừ":
            result = num1 - num2
            operation_symbol = "-"
        elif operation == "nhân":
            result = num1 * num2
            operation_symbol = "*"
        elif operation == "chia":
            if num2 != 0:
                result = num1 / num2
                operation_symbol = "/"
            else:
                messagebox.showerror("Lỗi", "Không thể chia cho 0.")
                return
        
        # Hiển thị kết quả
        label_result.config(text=f"Kết quả: {result}")
        
        # Thêm vào lịch sử
        history.append(f"{num1} {operation_symbol} {num2} = {result}")
        update_history()
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def show_help():
    messagebox.showinfo("Trợ giúp", "Đây là ứng dụng máy tính đơn giản với hai thẻ.\n"
                                    "Thẻ 1: Thực hiện các phép tính cơ bản (cộng, trừ, nhân, chia).\n"
                                    "Thẻ 2: Hiển thị lịch sử các phép tính đã thực hiện.")

def exit_app():
    root.quit()

def update_history():
    listbox_history.delete(0, tk.END)
    for item in history:
        listbox_history.insert(tk.END, item)

root = tk.Tk()
root.title("Máy Tính Cơ Bản")

# Danh sách lưu lịch sử
history = []

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Tệp", menu=file_menu)
file_menu.add_command(label="Thoát", command=exit_app)

edit_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Chỉnh sửa", menu=edit_menu)
edit_menu.add_command(label="Tùy chọn")

help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Trợ giúp", menu=help_menu)
help_menu.add_command(label="Giới thiệu", command=show_help)

notebook = ttk.Notebook(root)
notebook.pack(pady=10, expand=True)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Máy tính")

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Lịch sử")

# Tab 1
frame_tab1 = ttk.Frame(tab1)
frame_tab1.pack(pady=10)

entry_num1 = tk.Entry(frame_tab1, width=10)
entry_num1.grid(row=0, column=0, padx=5, pady=5)

entry_num2 = tk.Entry(frame_tab1, width=10)
entry_num2.grid(row=0, column=1, padx=5, pady=5)

add_button = tk.Button(frame_tab1, text="Cộng", command=lambda: calculate("cộng"))
add_button.grid(row=1, column=0, padx=5, pady=5)

subtract_button = tk.Button(frame_tab1, text="Trừ", command=lambda: calculate("trừ"))
subtract_button.grid(row=1, column=1, padx=5, pady=5)

multiply_button = tk.Button(frame_tab1, text="Nhân", command=lambda: calculate("nhân"))
multiply_button.grid(row=2, column=0, padx=5, pady=5)

divide_button = tk.Button(frame_tab1, text="Chia", command=lambda: calculate("chia"))
divide_button.grid(row=2, column=1, padx=5, pady=5)

label_result = tk.Label(frame_tab1, text="Kết quả: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Tab 2
frame_tab2 = ttk.Frame(tab2)
frame_tab2.pack(pady=10)

label_tab2 = tk.Label(frame_tab2, text="Lịch sử các phép tính:")
label_tab2.pack()

listbox_history = tk.Listbox(frame_tab2, width=40, height=10)
listbox_history.pack(pady=5)

root.mainloop()
