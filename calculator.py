from tkinter import *
from math import sqrt as sqr


class Application(Frame):
    def __init__(self, master):

        Frame.__init__(self, master)
        self.entry = Entry(master, width=24, font=("Arial", 25))
        self.entry.grid(row=0, column=0, columnspan=6, sticky="w")
        self.entry.focus_set()
        self.entry.configure(state="disabled", disabledbackground="white", disabledforeground="black")
        self.create_widgets()
        self.bind_buttons(master)
        self.grid()

    def add_char(self, char, btn=None):
        self.entry.configure(state="normal")
        self.flash(btn)
        if self.entry.get() == "Invalid Input":
            self.entry.delete(0, END)
        self.entry.insert(END, char)
        self.entry.configure(state="disabled")

    def clear(self):
        self.entry.configure(state="normal")
        if self.entry.get() != "Invalid Input":
            text = self.entry.get()[:-1]
            self.entry.delete(0, END)
            self.entry.insert(0, text)
        else:
            self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def clear_all(self):
        self.entry.configure(state="normal")
        self.entry.delete(0, END)
        self.entry.configure(state="disabled")

    def calculate(self):
        self.entry.configure(state="normal")
        e = self.entry.get()
        e = e.replace("√", "sqr")
        e = e.replace("×", "*")
        e = e.replace("²", "**2")
        e = e.replace("^", "**")
        e = e.replace("÷", "/")

        try:
            answer = eval(e)
        except Exception as ex:
            self.entry.delete(0, END)
            self.entry.insert(0, "Invalid Input")
        else:
            self.entry.delete(0, END)
            if len(str(answer)) > 20:
                self.entry.insert(0, '{:.10e}'.format(answer))
            else:
                self.entry.insert(0, answer)
        self.entry.configure(state="disabled")

    def flash(self, btn):
        if btn != None:
            btn.config(bg="yellow")
            if btn == self.c_button:
                self.clear()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            elif btn == self.eq_button:
                self.master.after(100, lambda: btn.config(bg="lightgrey"))
                self.calculate()
            elif btn == self.ac_button:
                self.clear_all()
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
            else:
                self.master.after(100, lambda: btn.config(bg="SystemButtonFace"))
        else:
            pass

    def bind_buttons(self, master):
        master.bind("<Return>", lambda event, btn=self.eq_button: self.flash(btn))
        master.bind("<BackSpace>", lambda event, btn=self.c_button: self.flash(btn))
        master.bind("9", lambda event, char="9", btn=self.nine_button: self.add_char(char, btn))
        master.bind("8", lambda event, char="8", btn=self.eight_button: self.add_char(char, btn))
        master.bind("7", lambda event, char="7", btn=self.seven_button: self.add_char(char, btn))
        master.bind("6", lambda event, char="6", btn=self.six_button: self.add_char(char, btn))
        master.bind("5", lambda event, char="5", btn=self.five_button: self.add_char(char, btn))
        master.bind("4", lambda event, char="4", btn=self.four_button: self.add_char(char, btn))
        master.bind("3", lambda event, char="3", btn=self.three_button: self.add_char(char, btn))
        master.bind("2", lambda event, char="2", btn=self.two_button: self.add_char(char, btn))
        master.bind("1", lambda event, char="1", btn=self.one_button: self.add_char(char, btn))
        master.bind("0", lambda event, char="0", btn=self.zero_button: self.add_char(char, btn))
        master.bind("*", lambda event, char="×", btn=self.mult_button: self.add_char(char, btn))
        master.bind("/", lambda event, char="÷", btn=self.div_button: self.add_char(char, btn))
        master.bind("^", lambda event, char="^", btn=self.sqr_button: self.add_char(char, btn))
        master.bind("%", lambda event, char="%", btn=self.mod_button: self.add_char(char, btn))
        master.bind(".", lambda event, char=".", btn=self.dec_button: self.add_char(char, btn))
        master.bind("-", lambda event, char="-", btn=self.sub_button: self.add_char(char, btn))
        master.bind("+", lambda event, char="+", btn=self.add_button: self.add_char(char, btn))
        master.bind("(", lambda event, char="(", btn=self.lpar_button: self.add_char(char, btn))
        master.bind(")", lambda event, char=")", btn=self.rpar_button: self.add_char(char, btn))
        master.bind("c", lambda event, btn=self.ac_button: self.flash(btn), self.clear_all)

    def create_widgets(self):
        self.eq_button = Button(self, text="=", width=20, height=3, bg="grey", command=lambda: self.calculate())
        self.eq_button.grid(row=4, column=4, columnspan=2)

        self.ac_button = Button(self, text='CE', width=9, height=3, bg='grey', command=lambda: self.clear_all())
        self.ac_button.grid(row=1, column=4)

        self.c_button = Button(self, text='←', width=9, height=3, bg='grey', command=lambda: self.clear())
        self.c_button.grid(row=1, column=5)

        self.add_button = Button(self, text="+", width=9, height=3, bg='grey', command=lambda: self.add_char('+'))
        self.add_button.grid(row=4, column=3)

        self.mult_button = Button(self, text="×", width=9, height=3, bg='grey', command=lambda: self.add_char('×'))
        self.mult_button.grid(row=2, column=3)

        self.sub_button = Button(self, text="-", width=9, height=3, bg='grey', command=lambda: self.add_char('-'))
        self.sub_button.grid(row=3, column=3)

        self.div_button = Button(self, text="÷", width=9, height=3, bg='grey', command=lambda: self.add_char('/'))
        self.div_button.grid(row=1, column=3)

        self.mod_button = Button(self, text="%", width=9, height=3, bg='grey', command=lambda: self.add_char('%'))
        self.mod_button.grid(row=4, column=2)

        self.seven_button = Button(self, text="7", width=9, height=3, bg='grey', command=lambda: self.add_char(7))
        self.seven_button.grid(row=1, column=0)

        self.eight_button = Button(self, text="8", width=9, height=3, bg='grey', command=lambda: self.add_char(8))
        self.eight_button.grid(row=1, column=1)

        self.nine_button = Button(self, text="9", width=9, height=3, bg='grey', command=lambda: self.add_char(9))
        self.nine_button.grid(row=1, column=2)

        self.four_button = Button(self, text="4", width=9, height=3, bg='grey', command=lambda: self.add_char(4))
        self.four_button.grid(row=2, column=0)

        self.five_button = Button(self, text="5", width=9, height=3, bg='grey', command=lambda: self.add_char(5))
        self.five_button.grid(row=2, column=1)

        self.six_button = Button(self, text="6", width=9, height=3, bg='grey', command=lambda: self.add_char(6))
        self.six_button.grid(row=2, column=2)

        self.one_button = Button(self, text="1", width=9, height=3, bg='grey', command=lambda: self.add_char(1))
        self.one_button.grid(row=3, column=0)

        self.two_button = Button(self, text="2", width=9, height=3, bg='grey', command=lambda: self.add_char(2))
        self.two_button.grid(row=3, column=1)

        self.three_button = Button(self, text="3", width=9, height=3, bg='grey', command=lambda: self.add_char(3))
        self.three_button.grid(row=3, column=2)

        self.zero_button = Button(self, text="0", width=9, height=3, bg='grey', command=lambda: self.add_char(0))
        self.zero_button.grid(row=4, column=0)

        self.dec_button = Button(self, text=".", width=9, height=3, bg='grey', command=lambda: self.add_char('.'))
        self.dec_button.grid(row=4, column=1)

        self.lpar_button = Button(self, text="(", width=9, height=3, bg='grey', command=lambda: self.add_char('('))
        self.lpar_button.grid(row=2, column=4)

        self.rpar_button = Button(self, text=")", width=9, height=3, bg='grey', command=lambda: self.add_char(')'))
        self.rpar_button.grid(row=2, column=5)

        self.sqr_button = Button(self, text="√", width=9, height=3, bg='grey', command=lambda: self.add_char('√('))
        self.sqr_button.grid(row=3, column=4)

        self.sqr_button = Button(self, text="^", width=9, height=3, bg='grey', command=lambda: self.add_char('^'))
        self.sqr_button.grid(row=3, column=5)


root = Tk()
root.geometry()
app = Application(root)
root.mainloop()
