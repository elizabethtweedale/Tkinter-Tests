# Skyscraper Code - Python - Elizabeth Tweedale

from tkinter import *

skyWide = 6
skyHigh = 7

def change_width():
    global skyWide
    skyWide = new
    print(new)

def draw_windows(self,W,H):
    for i in range(W):
        for j in range(H):
            # create_rectangle(startX(left), startY(top), finishX(right), finishY(bottom), outline, fill)
            self.create_rectangle((15*i+10),(15*j+10),(15*i+20),(15*j+20),outline="#fb7",fill=None)
    self.pack(fill=BOTH, expand=1)
    print(W,H)

def main():
    root = Tk()
    myBuilding = Canvas(root, width=300, height = 300)
    root.title("Skyscraper")
    myBuilding.pack()
    
    slider1 = Scale(root, from_=5, to=50, orient=HORIZONTAL)
    slider1.pack()

    skyWide = slider1.get()
    
    #draw_windows(myBuilding,SKY_WIDTH,SKY_HEIGHT)
    myBuilding.bind("<ButtonPress-1>", draw_windows(myBuilding,skyWide,skyHigh))

    root.mainloop()

main()
