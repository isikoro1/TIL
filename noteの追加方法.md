- ターミナルで以下のコマンド入力し、ファイルを作成（自動で日付付きタイトルになり、中身にテンプレが作成される）

PowerShellで入力し、ファイル作成する
~~~bash
.\scripts\new-note.ps1 -Title "Test1" 
~~~

- コミット前のファイルの消し方

~~~bash
Remove-Item -Force "2025\08-21_test2.md"
~~~

