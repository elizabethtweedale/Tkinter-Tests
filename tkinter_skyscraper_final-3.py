from tkinter import *

def newTower():
    skyWide = varW.get()        # Windows Wide
    skyHigh = varH.get()        # Windows High
    winW = varWinW.get()        # Window Width
    winH = varWinH.get()        # Window Height
    gap = varGap.get()          # Gap
    myBuilding.delete("all")

    # Draw Main Building
    myBuilding.create_rectangle(gap,gap,(skyWide+2)*gap+skyWide*winW,(skyHigh+2)*gap+skyHigh*winH,
                                        outline="gray", fill="gray")
    # Draw Windows
    for i in range(skyWide):
        for j in range(skyHigh):
            myBuilding.create_rectangle(((winW+gap)*i+2*gap),               # startX(left)
                                        ((winH+gap)*j+2*gap),               # startY(top)
                                        ((winW+gap)*i+(2*gap+winW)),        # finsihX(right)
                                        ((winH+gap)*j+(2*gap+winH)),        # finishY(bottom)
                                        outline="black",fill="white")       # outline, fill
                                        # Try using different colours such as "blue" or "red"

    myBuilding.pack(fill=BOTH, expand=1)
    

root = Tk()                                         # Set up Tkinter
myBuilding = Canvas(root, width=500, height=500)    # Set up Canvas
root.title("Skyscraper")                            # Set the title of your screen
myBuilding.pack()                                   # Pack adds everything to the Tkinter Canvas

""" Draw Scales """
# Create scales for the number of windows wide, number of windows high,
#   the window height and width as well as the gap between windows
varW = IntVar()     # Windows Wide Variable
scaleW = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varW, label="Windows Wide")
scaleW.pack()       # Add it to the Canvas

varH = IntVar()     # Windows High Variable
scaleH = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varH, label="Windows High")
scaleH.pack()       # Add it to the Canvas

varWinW = IntVar()  # Window Width Variable
scaleWinW = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varWinW, label="Window Width")
scaleWinW.pack()    # Add it to the Canvas

varWinH = IntVar()  # Window Height Variable
scaleWinH = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varWinH, label="Window Height")
scaleWinH.pack()    # Add it to the Canvas

varGap = IntVar()   # Gap Variable
scaleGap = Scale(root, from_=5, to=50, orient=HORIZONTAL, variable=varGap, label="Gap") #
scaleGap.pack()     # Add it to the Canvas

button1 = Button(root, text="Draw Tower", command=newTower) # Create a button to draw your tower
button1.pack()      # Add it to the Canvas

root.mainloop()     # Start Main Loop
