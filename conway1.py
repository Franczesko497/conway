import tkinter as tk
ROZDZ_X = 1600
ROZDZ_Y = 900
L = []
ROZMIAR = 20
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
            x1 = c * cell_size +110 #lewy-górny
            y1 = r * cell_size #prawy-górny
            x2 = x1 + cell_size + 110#lewy-dolny
            y2 = y1 + cell_size #prawy-dolny
            canvas.create_rectangle(x1, y1, x2, y2, fill="gray64", outline="black")

def update_grid(val):
    global ROZMIAR, running, after_id, L

    # Zatrzymaj automatyczne odświeżanie (jeśli trwa)
    if after_id:
        root.after_cancel(after_id)
        after_id = None

    running = False
    button.config(text="Start", bg="SystemButtonFace", activebackground="gray20")

    # Aktualizuj rozmiar i wyczyść dane
    size = int(val)
    ROZMIAR = size
    L = []

    # Odbuduj siatkę
    build_grid(size)


def get_color(x, y, cols, rows):
    idx = y * cols + x + 1
    return canvas.itemcget(idx, "fill")

#gray11 - zaludnione

def gra():
    global L
    L = []
    ry = int(ROZMIAR * ROZDZ_X / ROZDZ_Y)  # liczba kolumn

    for y in range(ROZMIAR):
        for x in range(ry):
            idx = y * ry + x + 1
            ss = canvas.itemcget(idx, "fill")

            s1 = canvas.itemcget(((y-1)%ROZMIAR) * ry + (x-1)%ry + 1, "fill") == "gray11"
            s2 = canvas.itemcget(((y-1)%ROZMIAR) * ry + (x)%ry + 1, "fill") == "gray11"
            s3 = canvas.itemcget(((y-1)%ROZMIAR) * ry + (x+1)%ry + 1, "fill") == "gray11"
            s4 = canvas.itemcget(((y)%ROZMIAR) * ry + (x-1)%ry + 1, "fill") == "gray11"
            s5 = canvas.itemcget(((y)%ROZMIAR) * ry + (x+1)%ry + 1, "fill") == "gray11"
            s6 = canvas.itemcget(((y+1)%ROZMIAR) * ry + (x-1)%ry + 1, "fill") == "gray11"
            s7 = canvas.itemcget(((y+1)%ROZMIAR) * ry + (x)%ry + 1, "fill") == "gray11"
            s8 = canvas.itemcget(((y+1)%ROZMIAR) * ry + (x+1)%ry + 1, "fill") == "gray11"

            S = sum([s1, s2, s3, s4, s5, s6, s7, s8])

            if ss == "gray11":
                L.append("gray11" if 2 <= S <= 3 else "gray64")
            else:
                L.append("gray11" if S == 3 else "gray64")

    # Aktualizacja stanu
    for y in range(ROZMIAR):
        for x in range(ry):
            canvas.itemconfig(y * ry + x + 1, fill=L[y * ry + x])


def auto_gra():
    gra()
    root.after(200, auto_gra)

running = False  # czy gra jest włączona
after_id = None  # ID zaplanowanego wywołania (żeby można było je anulować)

def toggle_game():
    global running, after_id

    if not running:
        running = True
        button.config(text="Stop", bg="red", activebackground="dark red")
        auto_gra()
    else:
        running = False
        button.config(text="Start", bg="SystemButtonFace", activebackground="gray20")
        if after_id:
            root.after_cancel(after_id)
            after_id = None


root = tk.Tk()
root.geometry(f"{ROZDZ_X}x{ROZDZ_Y}")
root.title("Game of Life")

canvas = tk.Canvas(root, bg="light goldenrod")
canvas.pack(fill="both", expand=True)
canvas.bind("<Button-1>", on_click)

w = tk.Scale(root, from_=ROZMIAR, to=40, orient="horizontal", label="       Size", command = update_grid)
w.place(x = 3, y = 220)
build_grid(ROZMIAR)
w.set(ROZMIAR)

button = tk.Button(root, text="Start", width=10, height=3, activebackground="gray20", activeforeground="white", command=toggle_game)
button.place(x=16, y=350)

button.place(x = 16, y = 350)

root.mainloop()
