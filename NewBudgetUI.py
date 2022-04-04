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
import tkinter as tk

window = tk.Tk()

window.wm_title("Budget Manager")
window.geometry("300x200")
window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")

def new_account_window():
    account_window = tk.Toplevel(window)
    account_window.title("Create New Account")
    account_window.geometry("500x500")

    account_name = tk.StringVar()
    name_field = tk.Entry(account_window, textvariable=account_name)
    name_field.grid(row=0, column=1)

    account_label = tk.Label(account_window, text="Account Name")
    account_label.grid(row=0, column=0)

    submit = tk.Button(account_window, text="Submit", width=17)
    submit.grid(row=1, column=1)

def new_ledger_window():
    ledger_window = tk.Toplevel(window)
    ledger_window.title("Create New Ledger")
    ledger_window.geometry("500x500")

    ledger_name = tk.StringVar()
    name_field = tk.Entry(ledger_window, textvariable=ledger_name)
    name_field.grid(row=0, column=1)

    ledger_label = tk.Label(ledger_window, text="Ledger Name")
    ledger_label.grid(row=0, column=0)

    submit = tk.Button(ledger_window, text="Submit", width=17)
    submit.grid(row=1, column=1)

def new_budget_window():
    budget_window = tk.Toplevel(window)
    budget_window.title("Create New Budget")
    budget_window.geometry("500x500")

    budget_name = tk.StringVar()
    name_field = tk.Entry(budget_window, textvariable=budget_name)
    name_field.grid(row=0, column=1)

    budget_label = tk.Label(budget_window, text="Budget Name")
    budget_label.grid(row=0, column=0)

    submit = tk.Button(budget_window, text="Submit", width=17)
    submit.grid(row=1, column=1)
    

def select_ledger():
    select_ledger = tk.Toplevel(window)
    select_ledger.title("Select Budget")
    select_ledger.geometry("300x200")

    select = tk.Label(select_ledger, text="This is where you'll choose which ledger to open.")
    select.grid(row=0, column=1)

def select_budget():
    select_budget = tk.Toplevel(window)
    select_budget.title("Select Budget")
    select_budget.geometry("300x200")

    select = tk.Label(select_budget, text="This is where you'll choose which budget to open.")
    select.grid(row=0, column=1)


win_label = tk.Label(window, text="Welcome to Budget Manager!")
win_label.grid(row=0, column=1)

new_account = tk.Button(window, text="Create New Account", width=17, command=new_account_window)
new_account.grid(row=1, column=0)

new_ledger = tk.Button(window, text="Create Ledger", width=17, command=new_ledger_window)
new_ledger.grid(row=2, column=0)

open_ledger = tk.Button(window, text="Open Ledger", width=17, command=select_ledger)
open_ledger.grid(row=3, column=0)

new_budget = tk.Button(window, text="Create Budget", width=17, command=new_budget_window)
new_budget.grid(row=4, column=0)

open_budget = tk.Button(window, text="Open Budget", width=17, command=select_budget)
open_budget.grid(row=5, column=0)

close_program = tk.Button(window, text="Close Program", width=17, command=window.destroy)
close_program.grid(row=6, column=0)


window.mainloop()