- ノート数: <!-- NOTES_COUNT -->5<!-- NOTES_COUNT -->
- 最終更新: <!-- LAST_UPDATED -->2025-08-24<!-- LAST_UPDATED -->

# Learning Notes

このリポジトリは、日々の学習記録をまとめた技術日誌です。  
実際に手を動かして学んだことや、調べたこと、試したコードなどを残しています。

## 構成
- `notes/` : 日々の学習ノート
  - `note-YYYY-MM-DD.md` の形式で追加

## 目的
- 学習内容の整理
- 後から見返せる技術メモ

## 今後の方針
- 疑問点はメモして解決まで追う
- 実験したコードも残す

## 自分用（コマンド操作等）
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
