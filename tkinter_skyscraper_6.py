from tkinter import *

skyWide = 6
skyHigh = 7

def updateTower(event):
    event.widget.delete("all")
    global skyWide, skyHigh
    for i in range(skyWide):
        for j in range(skyHigh):
            # create_rectangle(startX(left), startY(top), finishX(right), finishY(bottom), outline, fill)
            event.widget.create_rectangle((15*i+10),(15*j+10),(15*i+20),(15*j+20),outline="#fb7",fill=None)
    event.widget.pack(fill=BOTH, expand=1)

def writeItOut():
    global skyWide, skyHigh
    selection = "value="+str(var.get())
    label1.config(text=selection)
    print(skyWide,skyHigh,var.get())
    skyWide = var.get()
    updateTower(Event)

def newTower(self, myW, myH): 
    for i in range(myW):
        for j in range(myH):
            # create_rectangle(startX(left), startY(top), finishX(right), finishY(bottom), outline, fill)
            event.widget.create_rectangle((15*i+10),(15*j+10),(15*i+20),(15*j+20),outline="#fb7",fill=None)
    event.widget.pack(fill=BOTH, expand=1)
    


root = Tk()
myBuilding = Canvas(root, width=300, height=300)
root.title("Skyscraper")
myBuilding.pack()

var = IntVar()
scale1 = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=var)
scale1.pack()

button1 = Button(root, text="Get Scale", command=writeItOut)
button1.pack()
label1 = Label(root)
label1.pack()

myBuilding.bind("<ButtonRelease-1>", updateTower)
root.mainloop()
