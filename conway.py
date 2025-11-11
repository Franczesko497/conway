import tkinter as tk

def on_click(event):
    item = event.widget.find_closest(event.x, event.y)
    color = event.widget.itemcget(item, "fill")
    if color == "gray64":
        new_color = "gray11"
    else:
        new_color = "gray64"
    event.widget.itemconfig(item, fill=new_color)

def build_grid(size):
    cell_size = 1080/size
    canvas.delete("all")
    for r in range(size):
        for c in range(int(size * (16/9))):
            x1 = c * cell_size + 110#lewy-górny
            y1 = r * cell_size #prawy-górny
            x2 = x1 + cell_size + 110#lewy-dolny
            y2 = y1 + cell_size #prawy-dolny
            canvas.create_rectangle(x1, y1, x2, y2, fill="gray64", outline="black")

def update_grid(val):
    size = int(val)
    build_grid(size)

root = tk.Tk()
root.geometry("1920x1080")
root.title("Game of Life")

canvas = tk.Canvas(root, bg="light goldenrod")
canvas.pack(fill="both", expand=True)
canvas.bind("<Button-1>", on_click)

w = tk.Scale(root, from_=10, to=70, orient="horizontal", label="     Size", command = update_grid)
w.place(x = 3, y = 220)
build_grid(9)
w.set(10)

button = tk.Button(root, text="Start", activebackground="blue", activeforeground="white")
button.place(x = 100, y = 100)

root.mainloop()
