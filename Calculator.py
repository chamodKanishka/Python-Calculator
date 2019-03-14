from tkinter import *

from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Python Calculator")

        # create screen widget
        self.screen = Text(master, state='disabled', width=40, height=4, background="white", foreground="black")

        # position screen in window
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        self.screen.configure(state='normal')

        # initialize screen value as empty
        self.equation = ''

        # create buttons using method createButton
        button1 = self.createButton(7)
        button2 = self.createButton(8)
        button3 = self.createButton(9)
        button4 = self.createButton(u"\u232B", None)
        button5 = self.createButton(4)
        button6 = self.createButton(5)
        button7 = self.createButton(6)
        button8 = self.createButton(u"\u00F7")
        button9 = self.createButton(1)
        button10 = self.createButton(2)
        button11 = self.createButton(3)
        button12 = self.createButton('*')
        button13 = self.createButton('.')
        button14 = self.createButton(0)
        button15 = self.createButton('+')
        button16 = self.createButton('-')
        button17 = self.createButton('=', None, 46)

        # buttons stored in list
        buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11, button12,
                   button13, button14, button15, button16, button17]

        # intialize counter
        count = 0
        # arrange buttons with grid manager
        for row in range(1, 5):
            for column in range(4):
                buttons[count].grid(row=row, column=column)
                count += 1
        # arrange last button '=' at the bottom
        buttons[16].grid(row=5, column=0, columnspan=4)

    def createButton(self, val, write=True, width=10):


        return Button(self.master, text=val, command=lambda: self.click(val, write), width=width)

    def click(self, text, write):

        if write == None:

            # only evaluate code when there is an equation to be evaluated
            if text == '=' and self.equation:
                # replace the unicode value of division ./.with python division symbol / using regex
                self.equation = re.sub(u"\u00F7", '/', self.equation)
                print(self.equation)
                answer = str(eval(self.equation))
                self.clear_screen()
                self.insert_screen(answer, newline=True)
            elif text == u"\u232B":
                self.clear_screen()


        else:

            self.insert_screen(text)

    def clear_screen(self):
        self.equation = ''
        self.screen.configure(state='normal')
        self.screen.delete('1.0', END)

    def insert_screen(self, value, newline=False):
        self.screen.configure(state='normal')
        self.screen.insert(END, value)
        self.equation += str(value)
        self.screen.configure(state='disabled')


root = Tk()
my_gui = Calculator(root)
root.mainloop()







