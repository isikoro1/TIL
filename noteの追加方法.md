- ターミナルで以下のコマンド入力し、ファイルを作成（自動で日付付きタイトルになり、中身にテンプレが作成される）

PowerShellで入力し、ファイル作成する
~~~bash
.\scripts\new-note.ps1 -Title "Test1" 
~~~

- コミット前のファイルの消し方

~~~bash
Remove-Item -Force "notes\note-2025-08-21-test2.md"
~~~

- このリポジトリではGitHub Actionsを使用しており、GitHub上で自動更新される内容があるため、リモートを最新化する必要がある。

~~~ bash
git pull origin main --rebase
~~~

自分の変更をコミットしてpush

~~~ bash
git add .
git commit -m "Update: ファイル名"
git push origin main
~~~