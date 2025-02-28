# эту хуйню сделал XZY ( не хуйт не дипхуик)
import subprocess
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Хуй на блюде")  # и так понятно (если не тупой)
root.geometry("250x150")  # Размер окна

value_var = IntVar()
text_var = StringVar(value="0%")
progressbar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", variable=value_var)
progressbar.pack(fill=X, padx=6, pady=6)

label = ttk.Label(root, textvariable=text_var)
label.pack(anchor=NW, padx=6, pady=6)

Time = 5  # Время выполнения
app_path = "C:\\Path\\To\\Your\\app.exe"  # Путь к исполняемому файлу

def update_progress(i=0):
    if i <= Time:
        percentage = i * (100 / Time)
        value_var.set(percentage)
        text_var.set(f"{int(percentage)}%")
        progressbar.update()
        root.after(1000, update_progress, i + 1)
    else:
        value_var.set(100)
        text_var.set("100% - Complete")  # Обновляем текст сразу
        progressbar.update()
        root.after(3000, subprocess.Popen, [app_path])
        root.after(3000, root.destroy)

update_progress()

root.mainloop()