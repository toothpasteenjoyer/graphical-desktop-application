import tkinter as tk

tot_savings = 0
tot_emer = 0
tot_fun = 0

def CalculateSum():


    try:
        num1 = float(txtNum1.get())
        savings = round(((num1 / 10) * 3.5), 2)
        emergency = round(((num1 / 10) * 5), 2)
        fun = round(((num1 / 10) * 1.5), 2)
        lblSavings.config(text=str(savings))
        lblEmergency.config(text=str(emergency))
        lblFun.config(text=str(fun))
    except ValueError:
        lblSavings.config(text="Invalid Input")
        lblEmergency.config(text="Invalid Input")
        lblFun.config(text="Invalid Input")

# clears this paycheck only
def clear():
    txtNum1.delete(0, tk.END) #clear the text box
    txtNum2.delete(0, tk.END)
    txtNum3.delete(0, tk.END)
    lblSavings.config(text="-") #clear the label
    lblEmergency.config(text="-")
    lblFun.config(text="-")

# clears longterm bank savings
def clearall():
    lblTotSavings.config(text="-") #clear the label
    lblTotEmergency.config(text="-")
    lblTotFunn.config(text="-")

def Transfer():
        global tot_savings
        global tot_emer
        global tot_fun
        num1 = float(txtNum1.get())
        savings = round(((num1 / 10) * 3.5), 2)
        emergency = round(((num1 / 10) * 5), 2)
        fun = round(((num1 / 10) * 1.5), 2)
        tot_savings = tot_savings + savings
        tot_emer = tot_emer + emergency
        tot_fun = tot_fun + fun
        lblTotSavings.config(text=str(tot_savings))
        lblTotEmergency.config(text=str(tot_emer))
        lblTotFunn.config(text=str(tot_fun))


#tot_savings = tot_savings + lblSavings
#tot_emer = tot_emer + lblEmergency
#tot_fun = tot_fun + lblFun
#lblSavings, lblEmergency, lblFun

#####builds the window


window = tk.Tk() #create a window
window.title("Dividing Paycheck")
window.geometry("600x600") #set the window size
window.resizable(False, False) #make the window unresizable




####adding GUI elements
lblOne = tk.Label(window, text="Enter payroll: ")

lblSavings = tk.Label(window, text="-")
lblEmergency = tk.Label(window, text="-")
lblFun = tk.Label(window, text="-")

lblTitlSav = tk.Label(window, text="Savings: ")
lblTitlEmer = tk.Label(window, text="Emergency: ")
lblTitlFun = tk.Label(window, text="Fun: ")

lblTotSavings = tk.Label(window, text="-")
lblTotEmergency = tk.Label(window, text="-")
lblTotFunn = tk.Label(window, text="-")

lblTotSavLabel = tk.Label(window, text="Total Savings: ")
lblTotEmerLabel = tk.Label(window, text="Total Emergency: ")
lblTotFunLabel = tk.Label(window, text="Total Fun: ")

txtNum1 = tk.Entry(window)
txtNum2 = tk.Entry(window)
txtNum3 = tk.Entry(window)

txtNum7 = tk.Entry(window)
txtNum8 = tk.Entry(window)
txtNum9 = tk.Entry(window)


btnCalc = tk.Button(window, text="Calculate", command=CalculateSum)
btnTransfer = tk.Button(window, text="Transfer", command=Transfer)
btnClear = tk.Button(window, text="Clear", command=clear)
btnClearAll = tk.Button(window, text="Clear All", command=clearall)




#####building the grid
lblOne.grid(row=0, column=0, padx=10, pady=10)

lblTitlSav.grid(row=4, column=0, padx=10, pady=10) #labels
lblTitlEmer.grid(row=5, column=0, padx=10, pady=10)
lblTitlFun.grid(row=6, column=0, padx=10, pady=10)

lblTotSavLabel.grid(row=8, column=0, padx=10, pady=10) #labels
lblTotEmerLabel.grid(row=9, column=0, padx=10, pady=10)
lblTotFunLabel.grid(row=10, column=0, padx=10, pady=10)
 

lblSavings.grid(row=4, column=1, padx=10, pady=10) #outputs
lblEmergency.grid(row=5, column=1, padx=10, pady=10)
lblFun.grid(row=6, column=1, padx=10, pady=10)

lblTotSavings.grid(row=8, column=1, padx=10, pady=10) #outputs
lblTotEmergency.grid(row=9, column=1, padx=10, pady=10)
lblTotFunn.grid(row=10, column=1, padx=10, pady=10)




txtNum1.grid(row=0, column=1, padx=10, pady=10)



lblSavings.grid(row=4, column=1, padx=10, pady=10)
lblEmergency.grid(row=5, column=1, padx=10, pady=10)
lblFun.grid(row=6, column=1, padx=10, pady=10)

lblTotSavings.grid(row=8, column=1, padx=10, pady=10)
lblTotEmergency.grid(row=9, column=1, padx=10, pady=10)
lblTotFunn.grid(row=10, column=1, padx=10, pady=10)


btnClear.grid(row=7, column=10, padx=10, pady=10)
btnClearAll.grid(row=11, column=0, padx=10, pady=10)
btnTransfer.grid(row=7, column=0, padx=10, pady=10)
btnCalc.grid(row=3, column=0, padx=10, pady=10)


####builds and runs the app
window.mainloop() #run the app
