from tkinter import *

skyWide = 6
skyHigh = 7

def main():
    root = Tk()
    myBuilding = Canvas(root, width=300, height=300)
    root.title("Skyscraper")
    myBuilding.pack()
    
    var = IntVar()
    scale1 = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=var)
    scale1.pack()
    
    skyWide = scale1.get()

    button1 = Button(root, text="Get Scale", command=writeItOut)
    button1.pack()
    
    myBuilding.bind("<ButtonRelease-1>", updateTower)
    root.mainloop()

def updateTower(event):
    global skyWide, skyHigh, slider1
    for i in range(skyWide):
        for j in range(skyHigh):
            # create_rectangle(startX(left), startY(top), finishX(right), finishY(bottom), outline, fill)
            event.widget.create_rectangle((15*i+10),(15*j+10),(15*i+20),(15*j+20),outline="#fb7",fill=None)
    event.widget.pack(fill=BOTH, expand=1)

def writeItOut():
    global var
    selection = "value="+str(var.get())
    label.config(text=selection)

main()
