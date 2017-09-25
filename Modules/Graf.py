

canva_width = 1600
canva_height = 880
elements = ['Резистор','Переключатель','Лампочка','Батарейка','Провод']

class simulate:
    def __init__(self):
        self.but_check = Button(root,text="Просчитать")
        self.lis = Listbox(root,selectmode=SINGLE,height=5)
        for i in elements:
            self.lis.insert(END,i)
        self.canva = Canvas(width=canva_width,height=canva_height,bg='grey80')
        self.tex = Text(root,width=150,height=4,font="Verdana 12",wrap=WORD)

        self.but_check.grid(row=0,column=0,padx=5,pady=5)
        self.lis.grid(row=1,column=0,padx=5,pady=5)
        self.canva.grid(row=0,column=1,padx=5,pady=5)
        self.tex.grid(row=1,column=1,padx=5,pady=5)

        for x in range(0,canva_width,80):
            self.canva.create_line(x,0,x+canva_width,canva_width*2000, width=1,fill="red")

        for y in range(0,canva_height,80):
            self.canva.create_line(0,y,canva_width*3500,y+canva_width, width=1,fill="red")

from tkinter import *
root = Tk()
root.title("Test")
w, h = root.winfo_screenwidth() - 15, root.winfo_screenheight() - 80
root.geometry("{}x{}+0+0".format(w, h))

simulate = simulate()

root.mainloop()
