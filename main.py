from tkinter import *
import random as rdm
import ui_base

class Main(Frame):
    def __init__(self, window):
        super(Main, self).__init__(window)
        #self.startUI()

    def btn_start(self, window):
        btn_rock = Button(window, text='Камень', command=lambda x=1:self.btn_click(x))
        btn_scissors = Button(window, text='Ножницы', command=lambda x=1:self.btn_click(x))
        btn_paper = Button(window, text='Бумага', command=lambda x=1:self.btn_click(x))

        btn_rock.place(x=10, y=250, width=100, height=50)
        btn_scissors.place(x=150, y=250, width=100, height=50)
        btn_paper.place(x=290, y=250, width=100, height=50)

    def lbl_start(self):
        self.lbl_start = Label(window, text='Начинаем!\nВаш выбор:')
        self.lbl_score = Label(window, justify="left", text=f"Побед: {self.win}\nПроигрышей:{self.lose}\nДружба: {self.drow}")

        self.lbl_start.place(x=100, y=50)
        #self.lbl_score.place(x=165, y=150)

    def btn_click(self, play_choise):
        comp_choise = rdm.randint(1, 3)
        if play_choise == comp_choise:
            self.drow += 1
            self.lbl_score.configure(text="Ничья")
        elif play_choise == 1 and comp_choise == 2 \
            or play_choise == 2 and comp_choise == 3 \
            or play_choise == 3 and comp_choise == 1:
            self.win += 1
            self.lbl_score.configure(text="Победа")
        else:
            self.lose += 1
            self.lbl_score.configure(text="Проигрыш")

        self.lbl_score.configure(text=f"Побед: {self.win}\nПроигрышей:{self.lose}\Дружба: {self.drow}")

        del comp_choise

    def startUI(self):
        self.win = self.drow = self.lose = 0

        self.btn_start(window)
        self.lbl_start(window)
        

if __name__ == '__main__':
    #window = Tk()
    #window.title('Rock Scissors Paper')
    #window.geometry('400x400+300+300')
    #window.resizable(False, False)   
    window = ui_base.create_window()
    app = Main(window)
    app.pack()
    window.mainloop()
    
    