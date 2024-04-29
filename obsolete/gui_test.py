import tkinter as tk
from tkinter import messagebox

# Main window setup
root = tk.Tk()
root.title("AI Assistant GUI")
root.attributes('-fullscreen', True)

# CEO section
ceo_frame = tk.Frame(master=root, pady=10)
ceo_frame.pack(fill=tk.X)

ceo_label = tk.Label(ceo_frame, text="CEO Assistant", font=("Helvetica", 16))
ceo_label.pack()

ceo_text = tk.Text(ceo_frame, height=5, state='disabled', bg='#f0f0f0', wrap='word')
ceo_text.pack(fill=tk.X)

ceo_input = tk.Entry(ceo_frame)
ceo_input.pack(fill=tk.X)

def ceo_send():
    message = ceo_input.get()
    if message.strip():
        ceo_text.configure(state='normal')
        ceo_text.insert(tk.END, f"User: {message}\n")
        ceo_text.configure(state='disabled')
        ceo_input.delete(0, tk.END)

ceo_input.bind('<Return>', lambda e: ceo_send())

# Worker section with toggle
worker_frame = tk.Frame(root)
worker_frame.pack(fill=tk.BOTH, expand=False)  # Initially do not pack
worker_textboxes = []
toggle_var = tk.BooleanVar(value=False)

def toggle_workers():
    if toggle_var.get():
        worker_frame.pack(fill=tk.BOTH, expand=True)
    else:
        worker_frame.pack_forget()

toggle_btn = tk.Checkbutton(ceo_frame, text="Show Workers", variable=toggle_var, command=toggle_workers)
toggle_btn.pack(anchor='w')

def add_worker():
    worker_index = len(worker_textboxes)
    worker_column = tk.Frame(worker_frame)
    worker_column.grid(row=0, column=worker_index, sticky='nsew')
    worker_frame.grid_columnconfigure(worker_index, weight=1)

    worker_label = tk.Label(worker_column, text=f"Worker AI {worker_index + 1}", font=("Helvetica", 14))
    worker_label.pack()

    worker_text = tk.Text(worker_column, height=5, state='disabled', bg='#f0f0f0', wrap='word')
    worker_text.pack(fill=tk.BOTH, expand=True)

    worker_textboxes.append(worker_text)

# Adding initial workers
for i in range(3):  # Initial number of workers
    add_worker()

# Button to add more workers
add_worker_btn = tk.Button(ceo_frame, text="Add Worker", command=add_worker)
add_worker_btn.pack(anchor='w')

# Exit button
exit_button = tk.Button(ceo_frame, text="Exit", command=root.destroy)
exit_button.pack(anchor='e')

root.mainloop()
