# 学習ノート 2025-08-21 — git pull

## 今日学んだこと

### git pull origin main --rebase
- 実務現場では他の人のコミットがされている事が多いので、作業前に必ずリモートを最新化する。
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

### ブランチ運用（実務では必須）
- 直接 `main`に書き込むことは少ない
- 実務では作業ブランチを切って→ mainにマージする流れ
~~~ bash
git checkout -b feature/add-slug-gix
#作業
git push origin feature/add-slug-fix
~~~
- その後GitHubのPull Request(PR)でレビューを経てmainにマージ



## 疑問点・調べたいこと
- 

## 実験したコード / メモ
~~~bash
# ここに貼る
~~~

## 明日の目標
- 