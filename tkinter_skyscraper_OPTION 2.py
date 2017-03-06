from tkinter import *

#skyWide, skyHigh = 1, 1

winW, winH = 10, 15
gap = 5

def newTower():
    skyWide = varW.get()
    skyHigh = varH.get()
    myBuilding.delete("all")
    for i in range(skyWide):
        for j in range(skyHigh):
            # create_rectangle(startX(left), startY(top), finishX(right), finishY(bottom), outline, fill)
            myBuilding.create_rectangle(((winW+gap)*i+2*gap),
                                        ((winH+gap)*j+2*gap),
                                        ((winW+gap)*i+(2*gap+winW)),
                                        ((winH+gap)*j+(2*gap+winH)),
                                        outline="#fb7",fill=None)
    # draw outline
    myBuilding.create_rectangle(gap,gap,(skyWide+2)*gap+skyWide*winW,(skyHigh+2)*gap+skyHigh*winH, outline="#05f", fill=None)
    myBuilding.pack(fill=BOTH, expand=1)
    

root = Tk()
myBuilding = Canvas(root, width=500, height=500)
root.title("Skyscraper")
myBuilding.pack()

varW = IntVar()
scaleW = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varW, label="Windows Wide")
scaleW.pack()

varH = IntVar()
scaleH = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varH, label="Windows High")
scaleH.pack()

button1 = Button(root, text="Draw Tower", command=newTower)
button1.pack()

root.mainloop()
