import tkinter as tk
import datetime

class App:
    def __init__(self,parent):
        self.parent = parent

        

        self.hour_label = tk.Label(self.parent,text="H",background='plum1',font=('verdana',12,'bold'))
        self.tick1 = tk.Label(self.parent,text=':',background='plum1',font=('verdana',12,'bold'))
        self.minute_label = tk.Label(self.parent,text="M",background='plum1',font=('verdana',12,'bold'))
        self.tick2 = tk.Label(self.parent,text=':',background='plum1',font=('verdana',12,'bold'))
        self.second_label = tk.Label(self.parent,text="S",background='plum1',font=('verdana',12,'bold'))


        
        self.hour_label.place(x=150,y=130)
        self.tick1.place(x=180,y=130)
        self.minute_label.place(x=190,y=130)
        self.tick2.place(x=220,y=130)
        self.second_label.place(x=230,y=130)

        def time_update():
            self.my_label = tk.Label(self.parent,text="Digital Watch",background='yellow',
                                                  font=('times new roman',14,'bold'),borderwidth=4,relief='groove')
            self.my_label.place(x=140,y=50)
            hours = datetime.datetime.now().strftime("%H")
            minutes = datetime.datetime.now().strftime("%M")
            seconds = datetime.datetime.now().strftime("%S")
            a = self.hour_label.cget(key="text")
            b = self.minute_label.cget(key="text")
            c = self.second_label.cget(key="text")
            d = self.tick1.cget(key="text")
            e = self.tick2.cget(key="text")
            if a != hours:
                self.hour_label.config(text=hours)
            if b != minutes:
                self.minute_label.config(text=minutes)
            if c != seconds:
                self.second_label.config(text=seconds)

            if d == ':':
                self.tick1.config(text=' ')
            elif d == ' ':
                self.tick1.config(text=':')

            if e == ':':
                self.tick2.config(text=' ')
            elif e == ' ':
                self.tick2.config(text=':')
            
            self.my_label.after(500,time_update)
        time_update()
        


def main():
    root = tk.Tk()
    root.title('Digital Watch!!!')
    root.geometry('390x300+450+100')
    root.config(bg='plum1')
    root.resizable(0,0)
    obj = App(root)
    root.mainloop()
main()