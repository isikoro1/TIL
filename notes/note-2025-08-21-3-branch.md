# 学習ノート 2025-08-21 — branch

## 今日学んだこと
- 実務の開発ではブランチ運用をよく使う。学習でもブランチ運用で進めるとより実務に近い感覚で進められる。

### ブランチ運用の基本的な流れ（実務でよくある形）
1. 新しいブランチを作って作業開始
~~~powershell:powershell
git checkout -b feature/update-new-note-script
~~~
- feature/... や fix/... みたいな名前で切るのが定番

- 今回なら「new-note.ps1 を直す」とか「README更新処理追加」とかに合わせて名前を付ける

2. 作業してコミット
~~~powershell
git add .
git commit -m "Update: new-note.ps1 to use Convert-Slug instead of To-Slug"
~~~

3. リモートにブランチをpush
~~~powershell
git push origin feature/update-new-note-script
~~~

4.GitHub上で Pull Request（PR）を作成
- GitHubにアクセスすると「Compare & pull request」ボタンが出る

- タイトル・説明を入れて PR 作成

- （実務ではチームメンバーがレビュー）

- 自分のリポジトリなら、自分でマージ操作できる

5. main にマージして作業完了
- PRをマージするとmain に統合
- ローカルでも main を最新化しておく

~~~
git checkout main
git pull origin main --rebase
~~~

### ポイント
-main は常に「動く状態」を保つ
-作業は必ずブランチで → PR → main へ
-実務の現場でも「直接 main 触るのは禁止」ってルールが多い


