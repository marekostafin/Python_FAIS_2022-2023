import random
import tkinter as tk

def roll(facelabel):
    facelabel.config(image=face_dict[random.randint(1, 6)])

root = tk.Tk()
root.configure(background="white")
face1 = tk.PhotoImage(file="img/1.png")
face2 = tk.PhotoImage(file="img/2.png")
face3 = tk.PhotoImage(file="img/3.png")
face4 = tk.PhotoImage(file="img/4.png")
face5 = tk.PhotoImage(file="img/5.png")
face6 = tk.PhotoImage(file="img/6.png")
face_dict = {
    1: face1,
    2: face2,
    3: face3,
    4: face4,
    5: face5,
    6: face6
}
root.minsize(face1.width() + 50, face1.height() + 120)
root.maxsize(face1.width() + 50, face1.height() + 120)

frame = tk.Frame(root)

facelabel = tk.Label(
    root,
    image=face1
)
facelabel.pack(
    padx=(25, 25),
    pady=(25, 25)
)

button = tk.Button(
    text="Roll!",
    width=10,
    height=1,
    bg="navy",
    fg="white",
)
button['command'] = lambda arg1=facelabel: roll(arg1)
button.pack(
    pady=(0, 25)
)

frame.pack()

root.mainloop()
