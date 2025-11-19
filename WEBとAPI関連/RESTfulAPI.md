最終更新日:2025/11/18

# RESTful API

Webサービスやアプリケーション間で情報を安全にやり取りするための設計原則に従ったAPI

関連記事
https://qiita.com/185shingeki/items/ce01ee915504b8601193
「RESTとはなんぞや？」を４原則から考えてみる

４原則がある。

- アドレス可能性 (Addressability)
- ステートレス性 (Stateless)
- 接続性 (Connectability)
- 統一インターフェース (Uniform Interface)


## アドレス可能性 (Addressability)
提供する情報がURIを通して表現できること

## ステートレス性（Stateless）
情報のやり取りにおいて状態を持たず、各リクエストやレスポンスにて情報が完結していること

## 接続性 (Connectability)
情報の内部に他のリソースへのリンクを含めることができること

## 統一インターフェース (Uniform Interface)
最も重要。情報の操作（取得、作成、更新、削除）を統一メソッドを使用して行うこと
→HTTPメソッド（GET, POST, PUT, DELETE）が代表例 


関連記事２
https://qiita.com/NagaokaKenichi/items/0647c30ef596cedf4bf2