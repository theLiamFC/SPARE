import os
import tkinter as tk
from tkinter import scrolledtext
import time
import threading

def read_files():
    """
    Reads up to three text files from the 'logs/worker_logs' directory and returns their content.
    """
    logs_folder = "logs/worker_logs"
    files = os.listdir(logs_folder)
    txt_files = [f for f in files if f.endswith('.txt')]
    txt_files.sort()
    
    # Read content of each file
    contents = []
    for file in txt_files[:3]:  # Limit to 3 files
        with open(os.path.join(logs_folder, file), 'r') as f:
            contents.append((file, f.read()))
    return contents

def update_textboxes(textboxes):
    """
    Continuously updates the textboxes with the content of the log files.
    """
    while True:
        # Get updated content from the files
        file_contents = read_files()
        
        # Clear previous content and update textboxes
        for i, (file_name, content) in enumerate(file_contents):
            # Clear the textbox and insert new content
            textboxes[i].delete(1.0, tk.END)
            textboxes[i].insert(tk.INSERT, content)
            textboxes[i].label.config(text=file_name)  # Update label
        
        # If fewer than 3 files, clear any remaining textboxes
        for i in range(len(file_contents), 3):
            textboxes[i].delete(1.0, tk.END)
            textboxes[i].label.config(text="")
        
        time.sleep(1)  # Sleep for a second before checking again

def main():
    # Create a new window
    root = tk.Tk()
    root.title("Log Viewer")
    # root.attributes('-fullscreen', True)

    # Create a frame for organizing the textboxes
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    # Create and place textboxes in the frame
    textboxes = []
    for i in range(3):
        subframe = tk.Frame(frame)
        subframe.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
        
        # Create a label for the file name
        label = tk.Label(subframe, text="", font=("Arial", 14))
        label.pack()
        
        # Create the scrolled text widget for file content
        text_widget = scrolledtext.ScrolledText(subframe, wrap=tk.WORD, width=30, height=60)
        text_widget.pack(expand=True, fill="both")
        
        # Associate the label with the text widget
        text_widget.label = label
        textboxes.append(text_widget)

    # Configure frame columns to equally distribute space
    for i in range(3):
        frame.grid_columnconfigure(i, weight=1)
    
    # Create a separate thread for updating the textboxes
    update_thread = threading.Thread(target=update_textboxes, args=(textboxes,))
    update_thread.daemon = True  # Daemon thread to end with main program
    update_thread.start()

    # Start the Tkinter main loop
    root.mainloop()

if __name__ == "__main__":
    main()
