import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def calculate(operation):
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        
        if operation == "cộng":
            result = num1 + num2
        elif operation == "trừ":
            result = num1 - num2
        elif operation == "nhân":
            result = num1 * num2
        elif operation == "chia":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Lỗi", "Không thể chia cho 0.")
                return
        
        label_result.config(text=f"Kết quả: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ.")

def show_help():
    messagebox.showinfo("Trợ giúp", "Đây là ứng dụng máy tính đơn giản với hai thẻ.\n"
                                    "Thẻ 1: Thực hiện các phép tính cơ bản (cộng, trừ, nhân, chia).\n"
                                    "Thẻ 2: Chức năng mở rộng sẽ được thêm sau.\n"
                                    "Nhập hai số và chọn phép tính bạn muốn thực hiện.")

def exit_app():
    root.quit()

root = tk.Tk()
root.title("Máy Tính Cơ Bản")

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
notebook.add(tab1, text="Tab 1")

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Tab 2")

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

frame_tab2 = ttk.Frame(tab2)
frame_tab2.pack(pady=20)
label_tab2 = tk.Label(frame_tab2, text="Chức năng sẽ được thêm sau.")
label_tab2.pack()

root.mainloop()
