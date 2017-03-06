from tkinter import *

class Building(Frame):

    def __init(self, parent):
        Frame.__init__(self, parent)

        self.parent = parent
        self.drawBldg()

    def drawWindows(self,width,height,number):
        print (number)
        for i in range(number):
            canvas.create_rectangle(((i+1)*2), ((i+1)*2), width, height,
                                    outline="#05f", fill="05f")
            canvas.pack()
            print ("Rectangle",i)

    def drawBldg(self):

        self.parent.title("Building")
        self.pack(fill=BOTH, expand=1)
        drawWindows(self,120,40,5)
        canvas = Canvas(self)





def main():
    root = Tk()
    bldg = Building(root)
    root.geometry("400x100+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()
