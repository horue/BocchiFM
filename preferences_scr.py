import tkinter as tk
from tkinter import ttk
from preferences import *

def edit_pref():
    root = tk.Tk()
    root.title("Preferences")
    root.iconbitmap(r"Visual_Assets/bcc_2.ico")


    # Frame para organizar os widgets
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Labels e Entradas (Entry)
    ttk.Label(frame, text="User:").grid(column=1, row=1, sticky=tk.W)
    e1 = ttk.Entry(frame, width=30)
    e1.grid(column=2, row=1)

    ttk.Label(frame, text="API Key:").grid(column=1, row=2, sticky=tk.W)
    e2 = ttk.Entry(frame, width=30)
    e2.grid(column=2, row=2)

    # Botão de Envio
    submit_button = ttk.Button(frame, text="Save", command=lambda:save_pref(user=e1.get(), key=e2.get()))
    submit_button.grid(column=2, row=3, pady=10)

    # Para garantir que as colunas ajustem ao tamanho do conteúdo
    for child in frame.winfo_children():
        child.grid_configure(padx=5, pady=5)

    root.mainloop()
