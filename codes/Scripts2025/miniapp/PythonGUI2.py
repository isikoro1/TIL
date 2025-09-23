import tkinter as tk

# ウィンドウ作成
root = tk.Tk()
root.title("入力フォーム付きGUI")
root.geometry("400x200")

# ラベル作成
label = tk.Label(root, text="ここに入力結果が表示されます", font=("Arial", 12))
label.pack(pady=10)

# 入力フォーム
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

# ボタン処理
def on_click():
    text = entry.get() # 入力内容を取得
    if text.strip() == "":
        label.config(text="入力してください")
    else:
        label.config(text=f"入力された文字: {text}")

# ボタン
button = tk.Button(root, text="反映", command=on_click)
button.pack(pady=10)

# 表示ループ開始
root.mainloop()