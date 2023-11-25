import tkinter as tk
from tkinter import messagebox
Root.geometry("200x200")
Root.resizable(false,false)

var = tk.StringVar()

label = tk.Label(Root, textvariabel=var, relief=tk.RAISED )
label1 = tk.Label(Root, txt="hello python", relief=tk.RAISED)

var.set("hey!? how are you today?")

Lb1 = tk.Listbox(root)
Lb1.insert(1, "Python")
Lb1.insert(2, "Perl")
Lb1.insert(3, "C")
Lb1.insert(4, "PHP")
Lb1.insert(5, "JSP")
Lb1.insert(6, "Ruby")
Lb1.pack()
Top.Mainloop()
label.pack()

label.pack()
label1.pack()
Lb1.pack(pady=10)
Root.Mainloop()