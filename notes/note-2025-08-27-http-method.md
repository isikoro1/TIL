# 学習ノート 2025-08-27 — HTTP-method

## 今日学んだこと
- @GetMapping
    - GETに対応し、データ御取得する。
    - 例）Todoの一覧取得、１件取得

- @PostMapping
    - POSTに対応し、データを新規作成
    - 例）新しいTodoを追加

- @PutMapping
    - PUTに対応し、データを更新
    - 例）Todoのタイトルや状態を上書き

- @DeleteMapping
    - DELETEに対応し、データを削除
    - 例）Todoを削除

- @RestController
    - クラスにつける。「このクラスはAPIを返すコントローラ」と宣言
    - 例）public class TodoController {...}

- @RewuestMapping("～")
    - クラスやメソッドにつける。URLの共通プレフィックスをまとめる
    - 例）`/todos`をまとめる

### URLの共通プレフィックス（@RequestMapping）
- 共通のURLの「前置き部分」のこと
- クラスに着けると、そのクラスの全メソッドのURLに共通で付与される

例:
~~~java
@RestController
@RequestMapping("/todos")
public class TodoController {
    @GetMapping
    public List<Todo> findAll() { ... } // GET /todos
}
~~~
`@RequestMapping("/todos")`があるから、このクラスのAPIは全部`/todos`で始まる。
なければ`GET / `（ルート）になる。

## 疑問点・調べたいこと
- 

## 実験したコード / メモ
~~~bash
# ここに貼る
~~~

## 明日の目標
- 