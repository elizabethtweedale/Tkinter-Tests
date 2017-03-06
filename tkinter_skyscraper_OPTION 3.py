from tkinter import *

#skyWide, skyHigh = 1, 1

#winW, winH = 10, 15
#gap = 5

def newTower():
    skyWide = varW.get()
    skyHigh = varH.get()
    winW = varWinW.get()
    winH = varWinH.get()
    gap = varGap.get()
    myBuilding.delete("all")

    # draw outline
    myBuilding.create_rectangle(gap,gap,(skyWide+2)*gap+skyWide*winW,(skyHigh+2)*gap+skyHigh*winH,
                                        outline="gray", fill="gray")
    
    for i in range(skyWide):
        for j in range(skyHigh):
            # create_rectangle(startX(left), startY(top), finishX(right), finishY(bottom), outline, fill)
            myBuilding.create_rectangle(((winW+gap)*i+2*gap),
                                        ((winH+gap)*j+2*gap),
                                        ((winW+gap)*i+(2*gap+winW)),
                                        ((winH+gap)*j+(2*gap+winH)),
                                        outline="black",fill="white")       # try using different colours such as "blue" or "red"

    myBuilding.pack(fill=BOTH, expand=1)
    

root = Tk()
myBuilding = Canvas(root, width=500, height=500)
root.title("Skyscraper")
myBuilding.pack()

varW = IntVar()     # Windows Wide
scaleW = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varW, label="Windows Wide")
scaleW.pack()

varH = IntVar()     # Windows High
scaleH = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varH, label="Windows High")
scaleH.pack()

varWinW = IntVar()  # Window Width
scaleWinW = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varWinW, label="Window Width")
scaleWinW.pack()

varWinH = IntVar()  # Window Height
scaleWinH = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varWinH, label="Window Height")
scaleWinH.pack()

varGap = IntVar()  # Gap
scaleGap = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varGap, label="Gap")
scaleGap.pack()

button1 = Button(root, text="Draw Tower", command=newTower)
button1.pack()

root.mainloop()
