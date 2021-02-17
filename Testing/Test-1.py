import tkinter
import random

# 1 - Crate a window
window = tkinter.Tk()

# 2 - Set size
window.geometry("900x600")

# 3 - Create a frame
frame = tkinter.Frame()

#  Set the tile
frame.master.title("CREATE BY @SOMPHORS")


def doOnClick_1(event):
    canvas.create_text(450,300,fill="skyblue",font="Times 50 italic bold", text="Welcome to the Game!")
    


# Create the cavas to draw
canvas = tkinter.Canvas(frame)
colors = ["#33E924","#94F318","#F39118","#18F386","#694AC5","#8F866E","red","blue"]

canvas.create_rectangle(400, 500, 500, 550, fill=colors[random.randrange(0,7)], tags="myTag")
canvas.create_text(450,520,fill="black",font="Times 20 italic bold", text="Start", tags="myTag")
canvas.tag_bind("myTag", "<Button-1>", doOnClick_1)

# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()

