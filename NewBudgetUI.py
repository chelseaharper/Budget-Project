#New budget UI
#Icon attributed to freepik

# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtCore import pyqtSlot
# import sys
 
# class Window(QMainWindow):
#    def __init__(self):
#        super().__init__()
 
#        self.setGeometry(300, 300, 600, 400)
#        self.setWindowTitle("Budget Manager")
#        self.show()
 
# app = QApplication(sys.argv)
# window = Window()
# sys.exit(app.exec_())

import BudgetCalculations
import BudgetExports
from tkinter import *

window = Tk()

window.wm_title("Budget Manager")
window.geometry("500x500")
window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")

def new_account_window():
    account_window = Toplevel(window)
    account_window.title("Create New Account")
    account_window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    account_window.geometry("500x500")

    account_name = StringVar()
    name_field = Entry(account_window, textvariable=account_name)
    name_field.grid(row=0, column=1)

    account_label = Label(account_window, text="Account Name")
    account_label.grid(row=0, column=0)

    submit = Button(account_window, text="Submit", width=17)
    submit.grid(row=1, column=1)

def new_ledger_window():
    ledger_window = Toplevel(window)
    ledger_window.title("Create New Ledger")
    ledger_window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    ledger_window.geometry("500x500")

    ledger_name = StringVar()
    name_field = Entry(ledger_window, textvariable=ledger_name)
    name_field.grid(row=0, column=1)

    ledger_label = Label(ledger_window, text="Ledger Name")
    ledger_label.grid(row=0, column=0)

    submit = Button(ledger_window, text="Submit", width=17)
    submit.grid(row=1, column=1)

def new_budget_window():
    budget_window = Toplevel(window)
    budget_window.title("Create New Budget")
    budget_window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    budget_window.geometry("500x500")

    budget_name = StringVar()
    name_field = Entry(budget_window, textvariable=budget_name)
    name_field.grid(row=0, column=1)

    budget_label = Label(budget_window, text="Budget Name")
    budget_label.grid(row=0, column=0)

    submit = Button(budget_window, text="Submit", width=17)
    submit.grid(row=1, column=1)
    

def select_ledger():
    file_open_frame.pack(fill="both", expand=1)
    # select_ledger = Toplevel(window)
    # select_ledger.title("Select Budget")
    # select_ledger.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    # select_ledger.geometry("300x200")

    select = Label(select_ledger, text="This is where you'll choose which ledger to open.")
    select.grid(row=0, column=1)

def select_budget():
    select_budget = Toplevel(window)
    select_budget.title("Select Budget")
    select_budget.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    select_budget.geometry("300x200")

    select = Label(select_budget, text="This is where you'll choose which budget to open.")
    select.grid(row=0, column=1)


bar_menu = Menu(window)
window.config(menu=bar_menu)

file_menu = Menu(bar_menu)
bar_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Account", command=new_account_window)
file_menu.add_command(label="New Ledger", command=new_ledger_window)
file_menu.add_command(label="Open Ledger", command=select_ledger)
file_menu.add_separator()
file_menu.add_command(label="Close Program", command=window.quit)

edit_menu = Menu(bar_menu)
bar_menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Edit Something", command=new_ledger_window)

budget_menu = Menu(bar_menu)
bar_menu.add_cascade(label="Budget", menu=budget_menu)
budget_menu.add_command(label="New Budget", command=new_budget_window)
budget_menu.add_command(label="Open Budget", command=select_budget)

cash_flow_menu = Menu(bar_menu)
bar_menu.add_cascade(label="Cash Flow", menu=cash_flow_menu)
cash_flow_menu.add_command(label="New Ledger")

file_open_frame = Frame(window, width=400, height=400, bg="white")

# win_label = Label(window, text="Welcome to Budget Manager!")
# win_label.grid(row=0, column=1)

# new_account = Button(window, text="Create New Account", width=17, command=new_account_window)
# new_account.grid(row=1, column=0)

# new_ledger = Button(window, text="Create Ledger", width=17, command=new_ledger_window)
# new_ledger.grid(row=2, column=0)

# open_ledger = Button(window, text="Open Ledger", width=17, command=select_ledger)
# open_ledger.grid(row=3, column=0)

# new_budget = Button(window, text="Create Budget", width=17, command=new_budget_window)
# new_budget.grid(row=4, column=0)

# open_budget = Button(window, text="Open Budget", width=17, command=select_budget)
# open_budget.grid(row=5, column=0)

# close_program = Button(window, text="Close Program", width=17, command=window.destroy)
# close_program.grid(row=6, column=0)


window.mainloop()