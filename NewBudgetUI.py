#New budget UI
#Icon attributed to freepik

import BudgetCalculations
import BudgetExports
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

accounts = []

window = Tk()

window.wm_title("Budget Manager")
window.geometry("800x800")
window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")

base_frame = LabelFrame(window, text="Open Ledger", padx=5, pady=5)
base_frame.pack(padx=10, pady=10)

def item_created(item):
    global accounts
    head = item + " created"
    if item == "Account":
        response = messagebox.askyesno(head, "Would you like to create default categories for this account?")
        if response == 1:
            accounts[0].create_defaults(BudgetCalculations.default_categories)
            fill_text = " has been created successfully. The following default categories have been added:\n"
            cat = []
            for i in accounts[0].root_category.children:
                cat.append(i.name)
            categories = "\n".join(cat)
            message = item + fill_text + categories
            messagebox.showinfo(head, message)
        else:
            fill_text = " has been created successfully. No categories have been added."
            message = item + fill_text
            messagebox.showinfo(head, message)
    else:
        message = item + " has been created successfully."
        messagebox.showinfo(head, message)


def new_account_window():
    account_window = Toplevel(window)
    account_window.title("Create New Account")
    account_window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    account_window.geometry("300x100")

    account_name = StringVar()
    name_field = Entry(account_window, textvariable=account_name)
    name_field.grid(row=0, column=1, columnspan=2)

    account_label = Label(account_window, text="Account Name")
    account_label.grid(row=0, column=0)

    def create_account():
        global accounts
        account = BudgetCalculations.Account(account_name.get())
        accounts.append(account)
        item_created("Account")
        name_field.delete(0, END)

        file_menu.entryconfig("New Ledger", state="active")
        file_menu.entryconfig("Open Ledger", state="active")
        file_menu.entryconfig("Save Ledger", state="active")
        bar_menu.entryconfig("Budget", state="active")

        account_window.destroy()

        display_ledger()
        

    submit = Button(account_window, text="Submit", width=8, command=create_account)
    submit.grid(row=1, column=1)

    exit = Button(account_window, text="Close", width=8, command=account_window.destroy)
    exit.grid(row=1, column=2)

def display_ledger():
    account_frame = LabelFrame(window, text="Primary Ledger", padx=5, pady=5)
    account_frame.pack()

    b = Button(account_frame, text="Does Nothing")
    b.grid(row=0, column=0)

def new_ledger_window():
    ledger_window = Toplevel(window)
    ledger_window.title("Create New Ledger")
    ledger_window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    ledger_window.geometry("300x100")
        
    ledger_name = StringVar()
    name_field = Entry(ledger_window, textvariable=ledger_name)
    name_field.grid(row=0, column=1, columnspan=2)
        
    ledger_label = Label(ledger_window, text="Ledger Name")
    ledger_label.grid(row=0, column=0)
    
    def create_ledger():
        global accounts
        item_created("Ledger")
        Label(window, text=ledger_name.get()).pack()
        name_field.delete(0, END)

        file_menu.entryconfig("Save Ledger", state="active")
        bar_menu.entryconfig("Budget", state="active")

        ledger_window.destroy()
    
    submit = Button(ledger_window, text="Submit", width=8, command=create_ledger)
    submit.grid(row=1, column=1)

    exit = Button(ledger_window, text="Close", width=8, command=ledger_window.destroy)
    exit.grid(row=1, column=2)

def new_budget_window():
    budget_window = Toplevel(window)
    budget_window.title("Create New Budget")
    budget_window.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    budget_window.geometry("300x100")
        
    budget_name = StringVar()
    name_field = Entry(budget_window, textvariable=budget_name)
    name_field.grid(row=0, column=1)
        
    budget_label = Label(budget_window, text="Budget Name")
    budget_label.grid(row=0, column=0)

    def create_budget():
        global accounts
        item_created("Budget")
        Label(window, text=budget_name.get()).pack()
        name_field.delete(0, END)

        budget_menu.entryconfig("Save Budget", state="active")
        budget_menu.entryconfig("Modify Budget", state="active")
        bar_menu.entryconfig("Cash Flow", state="active")

        budget_window.destroy()
        
    submit = Button(budget_window, text="Submit", width=8, command=create_budget)
    submit.grid(row=1, column=1)

    exit = Button(budget_window, text="Close", width=8, command=budget_window.destroy)
    exit.grid(row=1, column=2)
    

def select_ledger():
    file_open_frame.pack(fill="both", expand=1)
    window.filename = filedialog.askopenfilename(initialdir="D:\Python learning materials and programs\Budget Project", title="Select a file", filetypes=(("JSON", "*.json"),("all files","*.*")))
    label_opened = Label(file_open_frame, text = window.filename)
    label_opened.grid(row=0, column=0)

    bar_menu.entryconfig("Edit Ledger", state="active")
    # select_ledger = Toplevel(window)
    # select_ledger.title("Select Budget")
    # select_ledger.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    # select_ledger.geometry("300x200")

    select = Label(select_ledger, text="This is where you'll choose which ledger to open.")
    select.grid(row=0, column=1)

def save_ledger():
    ledger_save = Toplevel(window)
    ledger_save.title("Save Ledger")
    ledger_save.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    ledger_save.geometry("300x200")

    select = Label(ledger_save, text="This is where you'll save the ledger.")
    select.grid(row=0, column=1)

def select_budget():
    select_budget = Toplevel(window)
    select_budget.title("Select Budget")
    select_budget.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    select_budget.geometry("300x200")

    select = Label(select_budget, text="This is where you'll choose which budget to open.")
    select.grid(row=0, column=1)

def select_account():
    select_account = Toplevel(window)
    select_account.title("Select Account")
    select_account.iconbitmap("D:/Python learning materials and programs/Budget Project/budget.ico")
    select_account.geometry("300x200")

    select = Label(select_account, text="This is where you'll choose which account to open.")
    select.grid(row=0, column=1)



bar_menu = Menu(window)
window.config(menu=bar_menu)

file_menu = Menu(bar_menu, tearoff=False)
bar_menu.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New Account", command=new_account_window)
file_menu.add_command(label="Open Account", command=select_account)
file_menu.add_command(label="New Ledger", command=new_ledger_window, state='disabled')
file_menu.add_command(label="Open Ledger", command=select_ledger, state='disabled')
file_menu.add_command(label="Save Ledger", command=save_ledger, state='disabled')
file_menu.add_separator()
file_menu.add_command(label="Close Program", command=window.quit)

edit_menu = Menu(bar_menu, tearoff=False)
bar_menu.add_cascade(label="Edit Ledger", menu=edit_menu, state='disabled')
edit_menu.add_command(label="Add Transaction", command=new_ledger_window)
edit_menu.add_command(label="Add Recurring Transaction", command=new_ledger_window)
edit_menu.add_command(label="Modify Transaction", command=new_ledger_window)
edit_menu.add_command(label="View Transaction", command=new_ledger_window)
edit_menu.add_separator()
edit_menu.add_command(label="Add Spending Category", command=new_ledger_window)
edit_menu.add_command(label="Modify Spending Category", command=new_ledger_window)
edit_menu.add_command(label="View Spending Categories", command=new_ledger_window)
edit_menu.add_separator()
edit_menu.add_command(label="Add User", command=new_ledger_window)
edit_menu.add_command(label="Modify User", command=new_ledger_window)
edit_menu.add_command(label="Select Current User", command=new_ledger_window)
edit_menu.add_command(label="View User List", command=new_ledger_window)

budget_menu = Menu(bar_menu, tearoff=False)
bar_menu.add_cascade(label="Budget", menu=budget_menu, state='disabled')
budget_menu.add_command(label="New Budget", command=new_budget_window)
budget_menu.add_command(label="Open Budget", command=select_budget)
budget_menu.add_command(label="Save Budget", command=select_budget, state='disabled')
budget_menu.add_command(label="Modify Budget", command=select_budget, state='disabled')


cash_flow_menu = Menu(bar_menu, tearoff=False)
bar_menu.add_cascade(label="Cash Flow", menu=cash_flow_menu, state='disabled')
cash_flow_menu.add_command(label="Generate Cash Flow", command=new_budget_window)
cash_flow_menu.add_command(label="Save Cash Flow", command=new_budget_window)
cash_flow_menu.add_command(label="Modify Cash Flow", command=new_budget_window)
cash_flow_menu.add_command(label="Export to Excel", command=new_budget_window)

file_open_frame = Frame(base_frame, width=450, height=450, bg="white")

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