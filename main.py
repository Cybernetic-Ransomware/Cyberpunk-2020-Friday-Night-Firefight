import sys
# import random

import tkinter as tk
from tkinter import ttk, PhotoImage


TEST = False
if len(sys.argv) > 1 and sys.argv[1] == '-test':
    TEST = True


class FridayNightFirefight:

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('800x600')
        self.root.title(' Friday Night Firefight ')
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file='img/pistol.png'))

        self.round = 0

        self.s = ttk.Style()
        self.s.configure('TNotebook.Tab', font=('Ubuntu', 10))
        self.s.configure('TLabel', font=('Ubuntu', 12))
        self.s.configure('TButton', font=('Ubuntu', 10))

        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill='both', pady=10, expand=True)

        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab4 = ttk.Frame(self.tabs, width=600, height=100)

        self.tabs.add(self.tab1, text=' Inicjatywa ')
        self.tabs.add(self.tab2, text=' Trafienie ')
        self.tabs.add(self.tab3, text=' Obrażenia ')
        self.tabs.add(self.tab4, text=' Obrona ')

        self.grid_round = ttk.Label(self.tab1, width=200)
        self.grid_round.pack(pady=25, padx=10, side='top', anchor=tk.W)

        self.round_label_01 = ttk.Label(self.grid_round, text='Runda:')
        self.round_label_01.grid(row=0, column=0, padx=2, sticky=tk.W)

        self.round_label_value_01 = ttk.Label(self.grid_round, text=self.round)
        self.round_label_value_01.grid(row=0, column=1, padx=(2, 25))

        self.round_label_button_01 = ttk.Button(self.grid_round, text='', command=self.round_increase, width=2)
        self.round_label_button_01.grid(row=0, column=2, padx=2, sticky=tk.E)

        self.round_label_button_02 = ttk.Button(self.grid_round, text='', command=self.round_decrease, width=2)
        self.round_label_button_02.grid(row=0, column=3, padx=2)

        self.round_label_button_03 = ttk.Button(self.grid_round, text='reset', command=self.round_reset, width=6)
        self.round_label_button_03.grid(row=0, column=4, padx=2)


        self.root.mainloop()


        # TODO reset checkboxów wykonanego ruchu w tabeli
    def round_increase(self):
        self.round += 1
        self.round_label_value_01.config(text=self.round)

    def round_decrease(self):
        if self.round > 0:
            self.round -= 1
            self.round_label_value_01.config(text=self.round)

    def round_reset(self):
        self.round = 0
        self.round_label_value_01.config(text=self.round)


if __name__ == '__main__':
    FridayNightFirefight()
