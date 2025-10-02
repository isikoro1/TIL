import pyttsx3

print("=== 音声読み上げプログラム ===")
print("読み上げたいテキストを入力してください。終了するには 'exit' と入力します。")

with open("voice_log.txt", "a", encoding="utf-8") as f:
    while True:
        text = input("> ")
        if text.lower() == "exit":
            print("終了します。")
            break
        f.write(text + "\n")

        # 毎回初期化することで必ず発声する
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
