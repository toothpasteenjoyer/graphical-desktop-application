import tkinter as tk

# SETTING UP TKINTER CANVAS
root = tk.Tk()
root.geometry('800x700')
root.title('TKinter Graphical Desktop Application')

canvas = tk.Canvas(root, width=800, height=700, bg='white')
canvas.pack(anchor=tk.CENTER, expand=False)


canvas.create_line((50, 50), (100, 100), width = 4, fill = "red")

sum = 0

# DEFINITIONS

def CalculateSum():
        num1 = float(BoxEntry1.get())
        num2 = float(BoxEntry2.get())
        num3 = float(BoxEntry3.get())
        num4 = float(BoxEntry4.get())
        sum = ((num1 + num2 + num3 + num4) / 10)
        bar1 = sum * num1
        bar2 = sum * num2
        bar3 = sum * num3
        bar4 = sum * num4
        lblBar1.config(text=float(num1))
        lblBar2.config(text=float(num2))
        lblBar3.config(text=float(num3))
        lblBar4.config(text=float(num4))
        Create_Rectangle(bar1, bar2, bar3, bar4)


def Create_Rectangle(bar1, bar2, bar3, bar4):
    barheight1 = bar1 * 10
    barheight2 = bar2 * 10
    barheight3 = bar3 * 10
    barheight4 = bar4 * 10
    
    canvas.create_rectangle(300, barheight1, 375, 500,outline ="red",fill ="red",width =2)
    canvas.create_rectangle(400, barheight2, 475, 500,outline ="blue",fill ="blue",width =2)
    canvas.create_rectangle(500, barheight3, 575, 500,outline ="green",fill ="green",width =2)
    canvas.create_rectangle(600, barheight4, 675, 500,outline ="yellow",fill ="yellow",width =2)

def Clear():
    BoxEntry1.delete(0, tk.END)
    BoxEntry2.delete(0, tk.END)
    BoxEntry3.delete(0, tk.END)
    BoxEntry4.delete(0, tk.END)
    lblBar1.config(text="-")
    lblBar2.config(text="-")
    lblBar3.config(text="-")
    lblBar4.config(text="-")
    canvas.create_rectangle(300, 100, 800, 500,outline ="white",fill ="white",width =2)

# BUTTON BOXES

btnSubmit = tk.Button(canvas, text = "Submit", command=CalculateSum)
canvas.create_window(100, 550, window = btnSubmit, anchor = "nw")
btnClear = tk.Button(canvas, text = "Clear", command=Clear)
canvas.create_window(50, 550, window = btnClear, anchor = "nw")

# TEXT LABELS

lblEntry1 = tk.Label(canvas, text = "Entry 1:")
canvas.create_window(40, 160, window = lblEntry1, anchor = "nw")

lblEntry2 = tk.Label(canvas, text = "Entry 2:")
canvas.create_window(40, 260, window = lblEntry2, anchor = "nw")

lblEntry3 = tk.Label(canvas, text = "Entry 3:")
canvas.create_window(40, 360, window = lblEntry3, anchor = "nw")

lblEntry4 = tk.Label(canvas, text = "Entry 4:")
canvas.create_window(40, 460, window = lblEntry4, anchor = "nw")


lblBar1 = tk.Label(canvas, text = "-")
canvas.create_window(350, 550, window = lblBar1, anchor = "nw")

lblBar2 = tk.Label(canvas, text = "-")
canvas.create_window(450, 550, window = lblBar2, anchor = "nw")

lblBar3 = tk.Label(canvas, text = "-")
canvas.create_window(550, 550, window = lblBar3, anchor = "nw")

lblBar4 = tk.Label(canvas, text = "-")
canvas.create_window(650, 550, window = lblBar4, anchor = "nw")


# TEXT BOXES

BoxEntry1 = tk.Entry(canvas)
canvas.create_window(100, 200, window = BoxEntry1)

BoxEntry2 = tk.Entry(canvas)
canvas.create_window(100, 300, window = BoxEntry2)

BoxEntry3 = tk.Entry(canvas)
canvas.create_window(100, 400, window = BoxEntry3)

BoxEntry4 = tk.Entry(canvas)
canvas.create_window(100, 500, window = BoxEntry4)



# TITLE TEXT

canvas.create_text(
    (450, 50),
    text="How many fruits have you eaten this week?",
    fill="orange",
    font='tkDefaeultFont 24'
)






root.mainloop()