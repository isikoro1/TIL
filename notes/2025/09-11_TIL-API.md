# TIL-API — 2025-09-11

## RESTful APIとは？


### RESTの意味
- REpresentational State Transfer(表現状態転送) の略
- Webアーキテクチャの設計思想の一つ

### RESTful APIの特徴
#### - URLがリソースを表す
    - 例: https://pokeapi.co/api/v2/pokemon/pikachu → 「ピカチュウというポケモン」

#### - HTTPメソッドで操作を区別
    - GET → データ取得
    - POST → データ新規作成
#### - 返すデータはJSONやXML → 機械が扱いやすい
要は「WebのURLをそのまま使ってデータをやりとりするシンプルなAPI」のこと
PokéAPIやOpenWeatherMapはRESTful APIの代表例

### 面白いAPIいろいろ（無料 or 無料枠あり）

#### エンタメ系

- PokéAPI → ポケモン図鑑・技・進化

- Star Wars API (SWAPI) → 登場人物や惑星のデータ

- The Rick and Morty API → キャラクター・エピソード情報

#### ネタ系

- Chuck Norris Jokes API → ランダムでジョークを返す

- Cat Facts API → 猫に関する豆知識を返す

- Dog CEO’s Dog API → 犬の画像ランダム取得

#### 実用系

- NewsAPI → 世界中のニュース記事（無料枠あり）

- ExchangeRate API → 為替レート

- NASA API → 天体画像や宇宙データ（宇宙好きに人気）

- Public-apis.io → 世界中の無料APIカタログ