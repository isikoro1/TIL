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

### `@RequestBody`
-リクエストの中身（JSONなど）をJavaオブジェクトに変換するためのアノテーション

例：
~~~java
POST  /todos
{
    "title": "牛乳を買う"
}
~~~
このJSONが、Springによって`Todo todo`に変換される
だから`public Todo create(@RequestBody Todo todo)`で、リクエストの中身をそのまま受け取れる。




## 疑問点・調べたいこと
- アプリ開発の経験が少なく、正直何言ってるかまで体験に落とし込めてない気がする。
- 細かい所は分からないまま、アプリを毎日何個も作る方向にシフトして、体験の中で理解を進めていった方が効率よさそう。

## 明日（以降）の目標
- なるべく毎日基本的なアプリ開発を進めて、可能であれば１日１アプリを開発、最終的に自力で１から作れる状態にする。