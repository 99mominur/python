import tkinter as tk

def on_canvas_click(event):
    # Get the current position of the mouse click
    x, y = event.x, event.y
    # Draw a point at the clicked position
    canvas.create_oval(x, y, x+2, y+2, fill="black")

def write_text():
    text = entry.get()  # Get the text from the entry field
    canvas.create_text(50, 50, text=text, fill="blue")

# Create the main window
root = tk.Tk()
root.title("Drawing and Writing")

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Bind the click event to the canvas
canvas.bind("<Button-1>", on_canvas_click)

# Create an Entry widget for entering text
entry = tk.Entry(root)
entry.pack()

# Create a button to write the entered text on the canvas
write_button = tk.Button(root, text="Write Text", command=write_text)
write_button.pack()

# Start the main loop
root.mainloop()

