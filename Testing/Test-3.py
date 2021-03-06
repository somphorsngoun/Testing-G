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
    canvas.move("click", 20, 20)
def doOnClick_2(event):
    canvas.move("click", 20, -20)

# Create the cavas to draw
canvas = tkinter.Canvas(frame)
colors = ["#33E924","#94F318","#F39118","#18F386","#694AC5","#8F866E","red","blue"]
for index1 in range(0,9):
    for index2 in range(0,9):
        canvas.create_rectangle(5+(index2*50), 5+(50*index1), 50+(index2*50), 50+(index1*50), fill=colors[random.randrange(0,7)], tags="click")
canvas.tag_bind("click","<Button-1>", doOnClick_1)
canvas.tag_bind("click","<Button-3>", doOnClick_2)
# 4 Display hhe window
canvas.pack(expand=True, fill='both')
frame.pack(expand=True, fill='both')
window.mainloop()