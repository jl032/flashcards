import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Scrollable Area")

# Create a frame to hold the canvas and scrollbar
frame = ttk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create a canvas widget
canvas = tk.Canvas(frame, borderwidth=0)
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a scrollbar to the canvas
scrollbar = ttk.Scrollbar(frame, orient="vertical", command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
canvas.configure(yscrollcommand=scrollbar.set)

# Create a frame inside the canvas to hold the scrollable content
scrollable_frame = ttk.Frame(canvas)

# Add the scrollable frame to the canvas
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Update the scrollregion when all widgets are in the scrollable frame
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# Add widgets to the scrollable frame (for example, some buttons)
for i in range(50):
    button = ttk.Button(scrollable_frame, text=f"Button {i+1}")
    button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()