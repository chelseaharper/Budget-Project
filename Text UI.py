from BudgetCalculations import *
from BudgetExports import *

def query_choices(prompt, responses):
    repeat = True
    question = [prompt, "\n"]
    for k,v in responses.items():
        entry = str(k) + "\t" + v
        question.append(entry)
        question.append("\n")
    while repeat == True:
        response = int(input("".join(question)))
        if response in responses:
            repeat = False
        else:
            print("Invalid selection. Please enter a valid response.")
    return responses.get(response)

def query_yn(prompt,responses):
    repeat = True
    while repeat == True:
        response = str(input(prompt))
        if response in responses:
            repeat = False
        else:
            print("Invalid selection. Please enter a valid response.")
    result = len(responses)
    for i in responses:
        if response == i:
            result = responses.index(i)
    if result < (len(responses)//2):
        return True
    else:
        return False

def transaction_test():
    print("This is a test of the transaction methods.")
    exit = False
    while exit == False:
        action = query_choices("What would you like to do?",
            {
                1: "Create a new account",
                2: "Add a transaction",
                3: "Add a recurring transaction",
                4: "Add new category",
                5: "Display transactions",
                6: "Correct transaction",
                7: "Run Cash Flow Report",
                8: "Exit program"})
        if action == "Create a new account":
            name = input(str("Enter the name of your account. "))
            main = Account(name)
            defaults = query_yn(
                "Would you like to create default categories? ",
                    [
                        "yes",
                        "Yes",
                        "y",
                        "Y",
                        "no",
                        "No",
                        "n",
                        "N"])
            if defaults:
                default_categories = [
                    "Food",
                    "Transportation",
                    "Clothing",
                    "Entertainment",
                    "Household",
                    "Payoff",
                    "Pets"]
                main.create_defaults(default_categories)
        elif action == "Add a transaction":
            trans_name = input(str("Enter the name of the transaction. "))
            trans_amount_entry = input(str("Enter the amount for the transaction. "))
            trans_type = query_yn(
                "Is this transaction a deposit or withdraw? ",
                    [
                        "deposit",
                        "Deposit",
                        "D",
                        "d",
                        "withdraw",
                        "Withdraw",
                        "w",
                        "W"])
            if trans_type:
                trans_amount = Decimal(trans_amount_entry)
            else:
                trans_amount = -1 * Decimal(trans_amount_entry)
            trans_date = input(str("Enter the date of the transaction. (mm-dd-yyyy) "))
            trans_cat = input(str("Enter the category for the transaction. "))
            main.ledger.add_transaction(Transaction(
                Decimal(trans_amount),
                trans_name,
                main.get_category(trans_cat),
                datetime.datetime.strptime(trans_date, "%m-%d-%Y").date()), main)
        elif action == "Add a recurring transaction":
            sample_trans_name = input(str("Enter the name of the transaction. "))
            sample_trans_amount = input(str("Enter the amount for the transaction. "))
            sample_trans_date = input(str("Enter the start date of the transaction. (mm-dd-yyyy) "))
            sample_trans_end_date = input(str("Enter the end date of the transaction. (mm-dd-yyyy) "))
            sample_trans_cat = input(str("Enter the category for the transaction. "))
            question = query_choices("How often does this transaction happen?",
            {
                1: "Monthly",
                2: "Yearly",
                3: "Other",})
            sample = Transaction(
                    Decimal(sample_trans_amount),
                    sample_trans_name,
                    main.get_category(sample_trans_cat),
                    datetime.datetime.strptime(sample_trans_date, "%m-%d-%Y").date())
            if question == "Monthly":
                schedule = TransactionSchedule(
                    sample,
                    sample.date,
                    sample_trans_end_date)
            elif question == "Yearly":
                schedule = TransactionSchedule(
                    sample,
                    sample.date,
                    sample_trans_end_date,
                    frequency = Yearly())
            else:
                days = input(str("Enter the number of days between transaction. "))
                schedule = TransactionSchedule(
                    sample,
                    sample.date,
                    sample_trans_end_date,
                    frequency = Regularly(int(days)))
            main.schedules.append(schedule)
        elif action == "Add new category":
            cat_name = input(str("Enter the name of the new category. "))
            main.root_category.add_child_category(cat_name)
        elif action  == "Display transactions":
            start = input(str("Enter the start date of the time frame. (mm-dd-yyyy) "))
            end = input(str("Enter the end date of the time frame. (mm-dd-yyyy) "))
            main.ledger.display(
                datetime.datetime.strptime(start, "%m-%d-%Y").date(),
                datetime.datetime.strptime(end, "%m-%d-%Y").date(), main)
        elif action  == "Correct transaction":            
            transaction_options = []
            for i in main.ledger.transactions:
                entry = str(i.date) + "   " + str(i.description)
                transaction_options.append(entry)
            options = {}
            for i in transaction_options:
                key = transaction_options.index(i) + 1
                value = i
                options[key] = value
            choice = query_choices("Which transaction do you need to update?", options)
            if choice in transaction_options:
                ind = transaction_options.index(choice)
                trans = main.ledger.transactions[ind]
            select = query_choices("What transaction element do you need to update?",
            {
                1: "Date",
                2: "Amount",
                3: "Description",
                4: "Category"
            })
            if select == "Date":
                v = input(str("Enter the date of the transaction. (mm-dd-yyyy) "))
                trans.date = datetime.datetime.strptime(v, "%m-%d-%Y").date()
            if select == "Amount":
                trans_amount_entry = input(str("Enter the amount for the transaction. "))
                trans_type = query_yn(
                    "Is this transaction a deposit or withdraw? ",
                    [
                        "deposit",
                        "Deposit",
                        "D",
                        "d",
                        "withdraw",
                        "Withdraw",
                        "w",
                        "W"])
                if trans_type:
                    trans.amount = Decimal(trans_amount_entry)
                else:
                    trans.amount = -1 * Decimal(trans_amount_entry)
            if select == "Description":
                trans.description = input(str("Enter the correct description for the transaction. "))
            if select == "Category":
                v = input(str("Enter the correct category for the transaction. "))
                trans.category = main.get_category(v)
        elif action  == "Run Cash Flow Report":
            start = input(str("Enter the start date of the time frame. (mm-dd-yyyy) "))
            end = input(str("Enter the end date of the time frame. (mm-dd-yyyy) "))
            initial = input(str("Enter the starting balance of the account: "))
            initial_amount = Decimal(initial)
            create_cash_flow(
                datetime.datetime.strptime(start, "%m-%d-%Y").date(),
                datetime.datetime.strptime(end, "%m-%d-%Y").date(), main, initial_amount)
        elif action == "Exit program":
            exit = True

#     for i in main.root_category.children:
#         print(i.name, " ", i.spending)
#     main.update_category_goal("Food", 300)
#     for i in main.root_category.children:
#         print(i.name, " ", i.goal)
#     for i in main.root_category.children:
#         print(i.name, " ", i.spending)


transaction_test()
