# Mavenとは

Mavenは「Javaプロジェクトを管理するツール」

正式には「ビルドツール」だが、単なるビルド以上のことができる。

- 依存関係の管理：　ライブラリを自動でダウンロード・管理
- ビルドの自動化：　Javaコードをコンパイルしてjar/warにまとめる
- プロジェクト構成の統一：　ディレクトリ構造を標準化（どの現場でも同じ構造に）
- 実行やテストの融合：　mvn testやmvn spring-boot:run でまとめて動かせる

# なぜ必要なのか

Mavenがないとどうなるか？
→ライブラリの導入・更新・設定を手動で行う必要がある。

例：Spring Frameworkを使いたいとき、

- Springのjarを自分で探してダウンロード
- クラスパスに自動で追加
- バージョンが合わずエラー

→非効率

Mavenなら以下のようにpom.xml　に一行書くだけでよい
~~~
<dependency>
  <groupId>org.springframework.boot</groupId>
  <artifactId>spring-boot-starter-web</artifactId>
</dependency>
~~~
すると、必要な依存ライブラリを全部自動で落としてくれる。

# プロジェクト構造
Mavenプロジェクトはどの現場でも同じ構造になっている。
これを「標準ディレクトリ構造」という
~~~
myapp/
├─ src/
│   ├─ main/
│   │   ├─ java/          ← Javaコード
│   │   └─ resources/     ← 設定ファイル、テンプレート
│   └─ test/
│       └─ java/          ← テストコード
├─ pom.xml                 ← Mavenの設定ファイル

~~~
pom.xml がMavenの心臓部
（POM = Project Object Model）

