# import time, os

# def clear_console():
#     os.system('cls' if os.name == 'nt' else 'clear')

# text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
# text2 = "Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of \"de Finibus Bonorum et Malorum\" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, \"Lorem ipsum dolor sit amet..\", comes from a line in section 1.10.32."
# for i in range(0, min(len(text), len(text2)), 5):
#     clear_console()
#     print(f"Worker 1: {text[:i]}\n")
#     print(f"Worker 2: {text2[:i]}\n")
#     print(f"Worker 3: {text[:i]}\n")
#     print(f"Worker 2: {text2[:i]}\n")

#     # time.sleep(.1)

import tkinter as tk
from threading import Thread
import time

# Example function simulating another part of the program
def background_task():
    global counter1, counter2
    while True:
        counter1 += 1
        counter2 += 2
        time.sleep(1)  # Simulates some processing time

def update_text():
    # Update GUI text elements with latest values
    block1_label.config(text=f"Block 1: {counter1}")
    block2_label.config(text=f"Block 2: {counter2}")
    
    # Schedule this function to be called again after 1 second
    root.after(1000, update_text)

# Main program
counter1, counter2 = 0, 0  # Shared state variables

root = tk.Tk()

# Create labels
block1_label = tk.Label(root, text="Block 1: 0")
block2_label = tk.Label(root, text="Block 2: 0")
block1_label.pack()
block2_label.pack()

# Start the background task in a separate thread
background_thread = Thread(target=background_task, daemon=True)
background_thread.start()

# Start GUI updates
update_text()

# Start the Tkinter mainloop
root.mainloop()
