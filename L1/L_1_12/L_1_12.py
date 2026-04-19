import math
import tkinter as tk
from tkinter import messagebox


def compute_y(x):
    x_rad = math.radians(x)
    if x < 3:
        subfunc = "lg( cos(2x) / (x − 0.5) )"
        if abs(x - 0.5) < 1e-12:
            return None, "Знаменник (x − 0.5) дорівнює нулю"
        cos2x = math.cos(2 * x_rad)
        fraction = cos2x / (x - 0.5)
        if fraction <= 0:
            return None, f"Аргумент lg = {fraction:.6g} ≤ 0 — логарифм не визначено"
        return math.log10(fraction), subfunc
    elif x >= 4:
        subfunc = "ln( cos(x) / (1 + tg²(x)) )"
        cos_x = math.cos(x_rad)
        if abs(cos_x) < 1e-12:
            return None, "cos(x) = 0 — tg(x) не визначено"
        tan_x = math.tan(x_rad)
        # 1 + tg²(x) = sec²(x) = 1/cos²(x) > 0 завжди при cos(x) ≠ 0
        fraction = cos_x / (1 + tan_x ** 2)  # = cos³(x)
        if fraction <= 0:
            return None, f"cos(x) = {cos_x:.6g} < 0 — аргумент ln ≤ 0"
        return math.log(fraction), subfunc
    else:
        return None, "Функція не визначена при 3 ≤ x < 4"


def on_calculate():
    try:
        x = float(entry_x.get())
    except ValueError:
        messagebox.showerror("Помилка введення", "x повинен бути числом")
        return

    result, info = compute_y(x)

    if result is not None:
        lbl_subfunc.config(text=f"Підфункція: {info}", fg="black")
        lbl_result.config(text=f"y = {result:.8f}", fg="blue")
    else:
        lbl_subfunc.config(text="", fg="black")
        lbl_result.config(text=f"Помилка: {info}", fg="red")


root = tk.Tk()
root.title("Лаб. робота — Варіант 12, Завдання 1")
root.geometry("520x200")
root.resizable(False, False)

tk.Label(root, text="Введіть x (у градусах):").pack(pady=(15, 2))
entry_x = tk.Entry(root, width=20, font=("Arial", 11))
entry_x.pack()

tk.Button(root, text="Обчислити", command=on_calculate, width=15).pack(pady=8)

lbl_subfunc = tk.Label(root, text="", font=("Arial", 10))
lbl_subfunc.pack()

lbl_result = tk.Label(root, text="", font=("Arial", 12, "bold"))
lbl_result.pack(pady=4)

root.mainloop()