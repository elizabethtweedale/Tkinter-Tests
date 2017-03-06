from tkinter import *

def newSkyscraper():
    winW = scaleWinW.get()
    winH = scaleWinH.get()
    w = scaleW.get()
    h = scaleH.get()
    gap = scaleGap.get()
    
    myBuilding.delete("all")

    # Draw main building
    myBuilding.create_rectangle(gap,gap,(winW+2)*gap+winW*w,(winH+2)*gap+winH*h,
                                        outline="gray", fill="gray")
    # Draw windows
    for i in range(winW):
        for j in range(winH):
            myBuilding.create_rectangle(((w+gap)*i+2*gap),               # startX(left)
                                        ((h+gap)*j+2*gap),               # startY(top)
                                        ((w+gap)*i+(2*gap+w)),        # finsihX(right)
                                        ((h+gap)*j+(2*gap+h)),        # finishY(bottom)
                                        outline="black",fill="white")       # outline, fill
                                        # Try using different colours such as "blue" or "red"

    myBuilding.pack(fill=BOTH, expand=1)    # Add the rectangles to your Canvas

root = Tk()                                         # Set up Tkinter
myBuilding = Canvas(root, width=500, height=500)    # Set up Canvas
root.title("Skyscraper")                            # Set the title of your screen
myBuilding.pack()                                   # Pack adds everything to the Tkinter Canvas

""" Draw Scales """
# Create a scale for the number of windows wide
scaleWinW = Scale(root, from_=5, to=50, orient=HORIZONTAL, label= "Windows Wide")
scaleWinW.pack()    # Add it to the Canvas

# Create a scale for the number of windows high
scaleWinH = Scale(root, from_=5, to=50, orient=HORIZONTAL, label= "Windows High")
scaleWinH.pack()    # Add it to the Canvas

# Create a scale for the windows' width
scaleW = Scale(root, from_=5, to=50, orient=HORIZONTAL, label= "Window Width")
scaleW.pack()    # Add it to the Canvas

# Create a scale for the windows' height
scaleH = Scale(root, from_=5, to=50, orient=HORIZONTAL, label= "Window Height")
scaleH.pack()    # Add it to the Canvas

# Create a scale for the size of the gap between windows
scaleGap = Scale(root, from_=2, to=20, orient=HORIZONTAL, label= "Window Gap")      # notice the smaller numbers for the from_ and to
scaleGap.pack()    # Add it to the Canvas

# Creaet a button to draw the skyscraper
button = Button(root, text="Draw Skyscraper", command=newSkyscraper)
button.pack()       # Add it to the Canvas

root.mainloop()     # start the main loop
