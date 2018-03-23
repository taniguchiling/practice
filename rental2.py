import tkinter as tk
from tkinter.filedialog import askopenfilename
import csv
# import pandas as pd


csv_file_path = ""


# csvデータのパスを指定して読み込む準備をするための関数
def import_csv_data():
    global v
    global csv_file_path
    csv_file_path = askopenfilename()
    print(csv_file_path)
    v.set(csv_file_path)
    # df = pd.read_csv(csv_file_path)


# csvを開いて表示するための関数
def open_csv_data():
    with open(csv_file_path, newline="") as file:
        reader = csv.reader(file)
        r = 2
        for col in reader:
            c = 0
            for row in col:
                open_csv_label = tk.Label(root, width=10, height=2, text=row, relief=tk.RIDGE)
                open_csv_label.grid(row=r, column=c)
                c += 1
            r += 1


root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1, columnspan=2)
tk.Button(root, text='参照',command=import_csv_data).grid(row=0, column=3)
tk.Button(root, text='終了',command=root.destroy).grid(row=1, column=0)
tk.Button(root, text='開く', command=open_csv_data).grid(row=1, column=3)
root.mainloop()

# エントリ（テキストボックス）形式で各セルに情報を表示して書き換え可能にして、それを列・行ごとにまるまるcsvファイルに上書きすれば書き換えできるかも
# リストボックスで表示したほうがスマートな感じ
