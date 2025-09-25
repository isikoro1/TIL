import pyttsx3

engine = pyttsx3.init()

print("=== 音声読み上げプログラム ===")
print("読み上げたいテキストを入力してください。終了するには 'exit' と入力します。")

with open("voice_log.txt", "a", encoding="utf-8") as f:
    while True:
        text = input("> ")
        if text.lower() == "exit":
            print("終了します。")
            break
        f.write(text + "\n")

        engine.say(text)
        engine.runAndWait()
        engine.stop()  # 次の入力に備えてキューをクリア
