import tkinter
import random

# 1 - Crate a window
window = tkinter.Tk()

# 2 - Set size
window.geometry("700x500")

# 3 - Create a frame
frame = tkinter.Frame()

#  Set the tile
frame.master.title("CREATE BY @SOMPHORS")


def doOnClick_1(event):
    colors = ["#33E924","#94F318","#F39118","#18F386","#694AC5","#8F866E","red","blue"]
    randomcolor = random.choice(colors)
    number = random.randrange(0,200)
    X1 = event.x - number
    X2 = event.x + number
    Y1 = event.y - number
    Y2 = event.y + number
    canvas.create_oval(X1, Y1, X2, Y2, fill=randomcolor)

# Create the cavas to draw
canvas = tkinter.Canvas(frame)
canvas.bind("<Button-1>", doOnClick_1)

# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()