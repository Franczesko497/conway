
import tkinter as tk
ROZDZ_X = 1600
ROZDZ_Y = 900

ROZMIAR = 10
def on_click(event):
    if(event.x >= 110):
        item = event.widget.find_closest(event.x, event.y)
        color = event.widget.itemcget(item, "fill")
        if color == "gray64":
            new_color = "gray11"
        else:
            new_color = "gray64"
        event.widget.itemconfig(item, fill=new_color)

def build_grid(size):
    cell_size = ROZDZ_Y/size
    canvas.delete("all")
    for r in range(size):
        for c in range(int(size * (ROZDZ_X / ROZDZ_Y))):
            x1 = c * cell_size + 110#lewy-górny
            y1 = r * cell_size #prawy-górny
            x2 = x1 + cell_size + 110#lewy-dolny
            y2 = y1 + cell_size #prawy-dolny
            canvas.create_rectangle(x1, y1, x2, y2, fill="gray64", outline="black")

def update_grid(val):
    size = int(val)
    build_grid(size)
    global ROZMIAR
    ROZMIAR = size

def gra():
    cell_size = ROZDZ_Y/ROZMIAR
    ry = int(ROZMIAR * 16/9)
    L = []
    #canvas.find_all()
    #canvas.itemconfig(item, fill="red")
    #kolor = canvas.itemcget(item, "fill")
    for x in range(int(ROZMIAR * 16/9)): #poziomo
        for y in range(ROZMIAR): #pionowo
            s1 = kolor = canvas.itemcget(((x-1)%ry)*(ry) + (y-1)%(ROZMIAR) + 1, "fill")
            s2 = kolor = canvas.itemcget(((x-1)%ry)*(ry) + (y)%(ROZMIAR) + 1, "fill")
            s3 = kolor = canvas.itemcget(((x-1)%ry)*(ry) + (y+1)%(ROZMIAR) + 1, "fill")
            s4 = kolor = canvas.itemcget(((x)%ry)*(ry) + (y-1)%(ROZMIAR) + 1, "fill")
            s5 = kolor = canvas.itemcget(((x)%ry)*(ry) + (y+1)%(ROZMIAR) + 1, "fill")
            s6 = kolor = canvas.itemcget(((x+1)%ry)*(ry) + (y-1)%(ROZMIAR) + 1, "fill")
            s7 = kolor = canvas.itemcget(((x+1)%ry)*(ry) + (y)%(ROZMIAR) + 1, "fill")
            s8 = kolor = canvas.itemcget(((x+1)%ry)*(ry) + (y+1)%(ROZMIAR) + 1, "fill")
            S = len([x for x in [s1, s2, s3, s4, s5, s6, s7, s8] if x == "gray11"])
            if(canvas.itemcget((x%ry) * ry + y%ROZMIAR + 1), "fill") == "gray64":
                if(S <= 1 or S >= 4):
                    L.append("gray64")
                elif(S == 2 or S == 3):
                    L.append("gray11")
root = tk.Tk()
root.geometry(f"{ROZDZ_X}x{ROZDZ_Y}")
root.title("Game of Life")

canvas = tk.Canvas(root, bg="light goldenrod")
canvas.pack(fill="both", expand=True)
canvas.bind("<Button-1>", on_click)

w = tk.Scale(root, from_=10, to=70, orient="horizontal", label="       Size", command = update_grid)
w.place(x = 3, y = 220)
build_grid(ROZMIAR)
w.set(10)

button = tk.Button(root, text="Start", width = 10, height=3, activebackground="gray20", activeforeground="white", command = gra)
button.place(x = 16, y = 350)

root.mainloop()
