# TIL — 2025-09-09

## メモ

curlでAPIアクセス
~~~bash
curl -X GET http://localhost:8080/todos
~~~

MySQLコンテナに接続
~~~bash
docker exec -it mysql mysql -u root -p
~~~

- MySQLの実行
~~~sql
USE tododb;
SHOW TABLES;
SELECT * FROM todo;
~~~


mvn 起動
~~~bash
mvn spring-boot:run
~~~

## SQLのデータが文字化けする問題
todoアプリを作成中、`title`が日本語だと文字化けする

## 対策

- MySQL側のDB・テーブルをUTF-8にする
~~~sql
ALTER DATABASE tododb CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
ALTER TABLE todo CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
~~~

src/main/resources/application.propertiesのMySQL URLを直す
~~~properties
spring.datasource.url=jdbc:mysql://127.0.0.1:3306/tododb?useSSL=false&allowPublicKeyRetrieval=true&serverTimezone=Asia/Tokyo&characterEncoding=UTF-8
~~~

- アプリ再起動
- 再び`curl`で`買い物`を登録
- SELECT * FROM todo; で正しく表示されるか確認

~~~sql
mysql> SELECT * FROM todo;
+----+------------+-------+ 
| id | done | title | 
+----+------------+-------+ 
| 1 | 0x00 | ??? | 
| 2 | 0x00 | ??? | 
+----+------------+-------+
~~~
→ 解決せず
原因：既存データは文字化けしたまま残るため、新規データで確認が必要

## 再トライ
- アプリ再起動
- MySQL再ログイン時にUTF-8(utf8mb4)でログイン
~~~bash
docker exec -it mysql mysql -u root -p --default-character-set=utf8mb4
~~~

- 再度
~~~sql
USE tododb;
SELECT * FROM todo;
~~~

## 結果
~~~sql
mysql> SELECT * FROM todo;
+----+------------+-----------+
| id | done       | title     |
+----+------------+-----------+
|  1 | 0x00       | 買い物    |
|  2 | 0x00       | 買い物    |
+----+------------+-----------+
~~~
→ 解決


## 学び
- DB/テーブルの文字コード設定とJDBCの接続パラメータは両方必要
- 既に保存された文字化けデータは直らない、新規データで確認する必要がある
- MySQLクライアントの接続文字コード指定も忘れずに