from tkinter import *
import openpyxl as px, os

os.chdir('/Users/Yusuke/Documents/Python/materials')

root = Tk()
root.title("Book")

wb = px.load_workbook('library.xlsx')
ws = wb.get_sheet_by_name('Library')

list1 = []
list2 = []
list3 = []

for col in range(1, 3000):
    list1.append(ws.cell(col, 2).value)
    list2.append(ws.cell(col, 3).value)
    list3.append(ws.cell(col, 15).value)

EditBox1 = Entry()
EditBox1.insert(END,"")
EditBox1.pack()

tx = Text()
tx.pack()

EditBox2 = Entry()
EditBox2.insert(END,"書籍番号")
EditBox2.pack()

EditBox3 = Entry()
EditBox3.insert(END,"名前")
EditBox3.pack()

def func1():
    value1 = EditBox1.get()
    for i in range(0, 2000):
        index = list2[i].find(value1)
        if index != -1:
            if list3[i] == "貸出中":
                tx.insert(END, "貸出中：" + str(i+1) + "：" + str(list1[i]) + "：" + list2[i] + "\n\n")
            else:
                tx.insert(END, str(i+1) + "：" + str(list1[i]) + "：" + list2[i] + "\n\n")

def func2():
    value2 = EditBox2.get()
    value3 = EditBox3.get()
    ws.cell(row=int(value2), column=15).value = "貸出中"
    ws.cell(row=int(value2), column=16).value = value3
    wb.save("library.xlsx")

def func3():
    value1 = EditBox2.get()
    ws.cell(row=int(value1), column=15).value = ""
    wb.save("library.xlsx")

Button(text = "検索", command = func1).pack()
Button(text = "貸出", command = func2).pack()
Button(text = "返却", command = func3).pack()

root.mainloop()