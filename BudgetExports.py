from BudgetCalculations import *
from openpyxl import Workbook


str_dates = ["03-20-2022", "03-15-2022", "04-01-2022", "04-20-2022"]
new_dates = []
for i in str_dates:
    instance = datetime.datetime.strptime(i, "%m-%d-%Y")
    new_dates.append(instance)

wb = Workbook()
dest_filename = "Test_File.xlsx"
ws = wb.active
ws.title = "Cash Flow"

ws['A1'] = "Date"
i = 0
while i < len(new_dates):
    cell = "A" + str(i + 2)
    ws[cell] = new_dates[i]
    i += 1

wb.save(filename = dest_filename)

def create_cash_flow(start, end, initial=0):
    pass