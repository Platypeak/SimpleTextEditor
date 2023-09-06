import tkinter
from tkinter import filedialog

def open_file(text):
    file_path = filedialog.askopenfilename()
    with open(file_path, "r") as file:
        text.delete(1.0, tkinter.END)
        text.insert(tkinter.END, file.read())

def save_file(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt")
    with open(file_path, 'w') as file:
        file.write(text.get(1.0, tkinter.END))

root = tkinter.Tk()
root.title("Text Editor")

text = tkinter.Text(root)
text.pack()

menu = tkinter.Menu()
root.config(menu=menu)

file_menu = tkinter.Menu(menu)
menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=lambda: open_file(text))
file_menu.add_command(label="Save", command=lambda: save_file(text))
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.quit)

root.mainloop()
