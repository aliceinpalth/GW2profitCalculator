# Code written and owned by Luna (on GitHub as: snowspirit)
# See read-me file for features and description of the program
# Icon provided by the icon archive with free commercial use:
# http://www.iconarchive.com/show/100-flat-2-icons-by-graphicloads.html

from Tkinter import *

top = Tk()

#Changing the window's title
top.wm_title("Profit Calculator")

#Keep the window always on top
top.wm_attributes("-topmost", 1)

#Make the window not able to change size
top.resizable(0,0)

#Changing the icon of the window
top.iconbitmap('program_icon.ico')

#Labels for the input boxes on the left-hand side of the window
Label(top, text="T5 Material:").grid(row=0)
Label(top, text="Mithril Ore:").grid(row=1)
Label(top, text="Elder Wood Log:").grid(row=2)
Label(top, text="Sell price of lowest Krait Slayer:").grid(row=3)
Label(top, text="Amount crafting:").grid(row=4)
profit = Label(top, text="Profit = ").grid(row=5, column=1)

#Creating the price input boxes
#T5 Material price input box  
e1 = Entry(top)
#Mithril Ore price input box
e2 = Entry(top)
#Elder Wood Log price input box
e3 = Entry(top)
#Lowest Krait Slayer price input box
e4 = Entry(top)
#Amount crafting input box
e5 = Entry(top)

#Adding the price input boxes to their appropriate places on the window    
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)
e3.grid(row = 2, column = 1)
e4.grid(row = 3, column = 1)
e5.grid(row = 4, column = 1)

#The calculate method, which is called when the "Check profit" button is clicked
def calculate():
    #Convert T5 material price input into a float variable
    t5 = float(e1.get())
    #Convert Mithril Ore price input into a float variable
    m = float(e2.get())
    #Convert Elder Wood Log input price into a float variable
    l = float(e3.get())
    #Convert lowest Krait Slayer input price into a float variable
    k = float(e4.get())
    #Convert number being crafted input into an int variable
    n = int(e5.get())
    
    '''
    Each crafted greatsword requires the following amount of materials:
        > 15 T5 Materials
        > 24 Mithril Ore
        > 12 Elder Wood Logs
    '''
    
    #Total costs:
    TC = ((15 * t5) + (24 * m) + (12 * l)) * n
    #Revenue:
    R = (k * n) * 0.85
    #Profit:
    P = R - TC
    
    profitString = str(P)
    
    if P > 0:
        profit = Label(top, text=("Profit = " + profitString + ""), bg = "green").grid(row=5, column=1)
    if P < 0:
        profit = Label(top, text=("Profit = " + profitString + ""), bg = "red").grid(row=5, column=1)
    
#Adding the button to check profit
calculateButton = Button(top, text = "Check profit", command = calculate)

#Displaying the button to check profit
calculateButton.grid(row = 5)

#Initiating the window
top.mainloop()
