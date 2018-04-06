from tkinter import *
from tkinter.filedialog import askopenfilename
import openpyxl as px
import os

# os.chdir('/Users/Yusuke/Documents/Python/materials')

root = Tk()
root.title("Book")

# フレームの生成
f0 = Frame(root)
f1 = Frame(root)
f2 = Frame(root)

file_path = ""


# 任意の場所からファイルを読み込む
def import_data():
    global v
    global file_path
    file_path = askopenfilename()
    print(file_path)
    v.set(file_path)


# ファイルを開く
def open_data():
    global wb
    global ws
    global list1, list2, list3
    wb = px.load_workbook(file_path)
    ws = wb.get_sheet_by_name('Library')

    list1 = []
    list2 = []
    list3 = []

    for col in range(1, 3716):
        list1.append(ws.cell(col, 2).value)
        list2.append(ws.cell(col, 3).value)
        list3.append(ws.cell(col, 15).value)

    # 開いているファイルの名前が表示されるようにする
    file_name = os.path.splitext(os.path.basename(file_path))
    Label(root, text=file_name).grid(row=1, column=4, columnspan=2, sticky=N+W)


search_box = Entry()
search_box.insert(END, "")
search_box.grid(row=1, column=1, sticky=E)

tx = Text()
tx.grid(row=2, column=0, columnspan=2)


def search():
    value1 = search_box.get()
    for i in range(0, 3715):
        index = list2[i].find(value1)
        if index != -1:
            if list3[i] == "貸出中":
                tx.insert(END, "貸出中：" + str(i+1) + "：" + str(list1[i]) + "：" + list2[i] + "\n\n")
            else:
                tx.insert(END, str(i+1) + "：" + str(list1[i]) + "：" + list2[i] + "\n\n")


# 新しいウインドウを作り、そこで貸出と返却の処理をするためのウィジェットを配置する
def borrow_window():
    borrow_win = Toplevel()

    book_number_box = Entry(borrow_win)
    book_number_box.insert(END, "書籍番号")
    book_number_box.grid(row=0, column=0, columnspan=2)

    book_name_box = Entry(borrow_win)
    book_name_box.insert(END, "名前")
    book_name_box.grid(row=1, column=0, columnspan=2)

    def borrow():
        value2 = book_number_box.get()
        value3 = book_name_box.get()
        ws.cell(row=int(value2), column=15).value = "貸出中"
        ws.cell(row=int(value2), column=16).value = value3
        wb.save("library.xlsx")

    def returning():
        value1 = book_number_box.get()
        ws.cell(row=int(value1), column=15).value = ""
        wb.save("library.xlsx")

    Button(borrow_win, text="貸出", command=borrow).grid(row=2, column=0, sticky=E)
    Button(borrow_win, text="返却", command=returning).grid(row=2, column=1, sticky=W)


# 親フレームのウィジェット配置
Label(root, text='パス: ').grid(row=0, column=3)
v = StringVar()
entry = Entry(root, textvariable=v).grid(row=0, column=4)
Button(root, text="参照", command=import_data).grid(row=0, column=5)
Button(root, text="開く", command=open_data).grid(row=1, column=5)
Button(root, text="検索", command=search).grid(row=1, column=2, sticky=W)
Button(root, text="貸出/返却", command=borrow_window).grid(row=3, column=1, padx=10, pady=10, sticky=E)
root.mainloop()

# フレームでレイアウトを整理する
# ファイルを開くのと貸し出しの処理は別ウインドウでいいかも
