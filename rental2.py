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


csv_open = ""


# csvを開いて表示するための関数
def open_csv_data():
    global csv_open

    csv_open = open(csv_file_path, newline="")
    with csv_open as file:
        reader = csv.reader(file)
        r = 3
        for col in reader:
            c = 0
            for row in col:
                open_csv_label = tk.Label(root, width=10, height=2, text=row, relief=tk.RIDGE)
                open_csv_label.grid(row=r, column=c)
                c += 1
            r += 1


# データ追加のためのウインドウ
def add_window():
    add_win = tk.Toplevel()  # データ入力用のサブウインドウを生成

    # 入力フォームなどを配置

    tk.Label(add_win, text="番号: ").grid(row=0, column=0)
    num_entry = tk.Entry(add_win)
    num_entry.grid(row=0, column=1)

    tk.Label(add_win, text="田中: ").grid(row=1, column=0)
    tanaka_entry = tk.Entry(add_win)
    tanaka_entry.grid(row=1, column=1)

    tk.Label(add_win, text="井上: ").grid(row=2, column=0)
    inoue_entry = tk.Entry(add_win)
    inoue_entry.grid(row=2, column=1)

    tk.Label(add_win, text="砂糖: ").grid(row=3, column=0)
    sato_entry = tk.Entry(add_win)
    sato_entry.grid(row=3, column=1)

    def add_data():
        global csv_open

        # 入力された値を取得
        num = num_entry.get()
        inoue = inoue_entry.get()
        tanaka = tanaka_entry.get()
        sato = sato_entry.get()

        # 値をリスト化する
        add_list = [num, tanaka, inoue, sato]

        csv_open = open(csv_file_path, "a", newline="")
        file = csv_open
        writer = csv.writer(file, lineterminator="\n")
        writer.writerow(add_list)
        file.close()

    button = tk.Button(add_win, text="追加", command=add_data)
    button.grid(row=3, column=2)


root = tk.Tk()
tk.Label(root, text='File Path').grid(row=0, column=0)
v = tk.StringVar()
entry = tk.Entry(root, textvariable=v).grid(row=0, column=1, columnspan=2)
tk.Button(root, text='参照',command=import_csv_data).grid(row=0, column=3)
tk.Button(root, text='終了',command=root.destroy).grid(row=1, column=0)
tk.Button(root, text='開く/更新', command=open_csv_data).grid(row=1, column=3)
tk.Button(root, text='追加', command=add_window).grid(row=2, column=3)
root.mainloop()

# エントリ（テキストボックス）形式で各セルに情報を表示して書き換え可能にして、それを列・行ごとにまるまるcsvファイルに上書きすれば書き換えできるかも
# リストボックスで表示したほうがスマートな感じ
