import tkinter as tk

# ウィンドウを作成する
root = tk.Tk()
root.title("簡易アドレス帳")
root.geometry("400x300")


# 名前入力
name_label = tk.Label(root, text="名前;")
name_label.pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

# 電話番号入力
phone_label = tk.Label(root, text="電話番号:")
phone_label.pack()
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()


# リストボックス
listbox = tk.Listbox(root, width=40, height=8)
listbox.pack(pady=10)

# 登録処理
def add_entry():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    if name == "" or phone == "":
        listbox.insert(tk.END, "エラー: 名前と電話番号を入力してください")
    else:
        listbox.insert(tk.END, f"{name} ({phone})")
        # 入力フォームをクリア
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

# 登録ボタン
add_button = tk.Button(root, text="登録", command=add_entry)
add_button.pack(pady=5)

# メインループを開始する
root.mainloop()

