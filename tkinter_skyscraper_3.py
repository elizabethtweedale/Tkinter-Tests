# Skyscraper Code - Python - Elizabeth Tweedale
# Successfully draws a grid of 6 x 6 windows... then extra functions not in use at the top

from tkinter import *

buildingHeight = 200
buildingLength = 40


def drawWindow(self,x,y,width,height):
    myBuilding.create_rectangle(5,5,5,5, outline="#fb0", fill="#fb0")
    myBuilding.pack()

def drawOneFloor(self,number, size):
    for i in range(number):
        drawWindow(self,i+size,i+size,size,size)


def drawBuilding(number, size):
    for j in range(number):
        drawOneRow(number, size)

def main():
    root = Tk()
    myBuilding = Canvas(root, width=300, height = 400)
    myBuilding.pack()

    for i in range(6):
        for j in range(6):
            # create_rectangle (startX(right), startY(down), width, height)
            myBuilding.create_rectangle((15*i+10),(15*j+10),(15*i+20),(15*j+20),
                                        outline="#fb7", fill=None)
    myBuilding.pack(fill=BOTH, expand=1)

 #   drawOneFloor(myBuilding,10,25)

main()
