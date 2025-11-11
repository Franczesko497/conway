import tkinter as tk
def on_click(event):
    """Zmienia kolor klikniętego pola."""
    label = event.widget  # obiekt, który został kliknięty
    # Jeśli już jest żółty — przywróć oryginalny
    if label["bg"] == "gray64":
        label["bg"] = "gray11"
    else:
        label["bg"] = "gray64"

def build_grid(size_x, size_y):
    for widget in frame.winfo_children():
        widget.destroy()
    labels.clear()
    for r in range(size_x):
        row = []
        for c in range(size_y):
            label = tk.Label( #tworzenie obiektu label
                frame,
                bg="gray64",
                width=5,
                height=2,
                relief="solid",
                borderwidth=0
            )
            label.grid(row=r+30, column=c+30, padx=0, pady=0) #umieszczenie obiektu
            label.bind("<Button-1>", on_click)  # kliknięcie myszą
            row.append(label)
        labels.append(row)

def update_grid(val):
    size = int(val)
    build_grid(int(size), int(size*1.5))

root = tk.Tk() #inicjalizacja
root.geometry("1920x1080")
root.title("Conway's game of life'") #nazwa
frame = tk.Frame(root, bg="black") #ramka (inicjalizacja i kolor)
frame.pack(padx=1, pady=1) # rozmiar ramki


labels = []
w = tk.Scale(root, from_=1, to=25, orient="horizontal", label="     Size", command = update_grid)
w.place(x = 0, y = 0)
build_grid(10, 15)
w.set(10)
root.mainloop()
#labels["bg"] = kolor
#gray11 = zaludniona
#gray64 = pusta
