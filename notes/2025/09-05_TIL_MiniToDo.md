# TIL_MiniToDo — 2025-09-05

MiniToDo (Daily-codes)でAIに教えて貰って分からなかった部分など
Java
## `equalsIgnoreCase`

- 文字列の内容を大文字小文字を区別せずに比較するメソッド
~~~java
"exit".equalsIgnoreCase("EXIT"); //true
"exit".equalsIgnoreCase("Exit"); //true
~~~

普通の`equals`だと`"exit".equals("EXIT)`はfalseになる

## `substring`
- 文字列の一部を切り出すメソッド

~~~java
String text = "add 勉強";
String task = text.substring(4); // index=4以降を切り出す → "勉強"
~~~
- indexは始まり(`0:a, 1:d, 2:d, 3:スペース, 4:勉強...`)
⇒MiniToDo.javaでは「`add`の後ろだけを取り出す」のに使っている。

## `startswith`
- 文字列が指定した文字列で始まっているかを判定

~~~java
"add 勉強".startsWith("add "); // true
"delete 1".startsWith("add "); // false
~~~
⇒MiniToDo.javaでは「コマンドが`add`で始まってるか？」を判定するのに使っている。

## `try { } catch(NumberFormatException e) { }`
- `NumberFormatException` = 「数字に変換できないとき」に発生する例外

~~~java
int n = Integer.parseInt("123"); // OK → 123
int m = Integer.parseInt("abc"); // エラー! → NumberFormatException
~~~
⇒MiniToDo.javaでは`delete abc`みたいに数字じゃない入力をしてもプログラムが落ちないようにcatchで拾っている。
- `e`は例外オブジェクトであり、中にエラーメッセージなどが入っている。
