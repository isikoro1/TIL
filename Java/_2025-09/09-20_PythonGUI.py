import tkinter as tk

# ウィンドウ作成
root = tk.Tk()
root.title("Hello GUI")
root.geometry("300x200")

# ラベル作成
label = tk.Label(root, text="こんにちは GUI!", font=("Arial", 14))
label.pack(pady=20)

# ボタン作成
def on_click():
    label.config(text="ボタンが押されました")

button = tk.Button(root, text="クリックしてね", command=on_click)
button.pack()

# 表示ループ開始
root.mainloop()