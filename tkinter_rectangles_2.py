from tkinter import *

def drawWindow(self,x,y,width,height):
    myBuilding.create_rectangle(5,5,5,5, fill="#fb0")
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
            myBuilding.create_rectangle(((i+10)*6),((j+10)*10),5, 20,
                                        outline="#fb7", fill=None)
            myBuilding.create_rectangle(((i+10)*6+5),((j+10)*10+5),2,100,
                                        outline="#05f", fill=None)

    myBuilding.pack(fill=BOTH, expand=1)

 #   drawOneFloor(myBuilding,10,25)

main()
