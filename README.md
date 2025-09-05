# Today I Learned(今日学んだこと)

## ディレクトリ構成
- codes/ ⇒ 書いたコードを保存
    - AtCoder_2025/
        ⇒ 競技プログラミングの提出コード
    - miniapps/
        ⇒ 簡単なアプリの少し長めのコード
    - Scripts/
        ⇒ 1機能のみの簡単なコード

- notes/
    ⇒ 学んだ内容やメモなどを自然言語でマークダウンファイルで保存
    - 2025/
    - chatGPT-prompts/
        ⇒ chatGPTとの壁打ち履歴（更新停止中）



## noteの作成方法
- ターミナルで以下のコマンド入力し、ファイルを作成（自動で日付付きタイトルになり、中身にテンプレが作成される）

PowerShellで入力し、ファイル作成する
~~~bash
.\scripts\new-note.ps1 -Title "Test1" 
~~~

- コミット前のファイルの消し方

~~~bash
Remove-Item -Force "2025\08-21_test2.md"
~~~

