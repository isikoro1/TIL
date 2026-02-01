SQLのUPDATEはインクリメントできる

例：
~~~
UPDATE テーブル名
SET 列名 = 列名 + 1
WHERE 条件
~~~


CRUD処理での[楽観ロック](https://github.com/isikoro1/TIL/blob/main/WEB%E3%81%A8API%E9%96%A2%E9%80%A3/%E6%A5%BD%E8%A6%B3%E3%83%AD%E3%83%83%E3%82%AF.md)を用いた更新処理をする場合、Versionといったフィールド変数などを使う。
ビジネスロジック層よりもデータアクセス層から直接SQLで楽観ロック管理をした方が安心。



参考:https://teratail.com/questions/14809

[同じテーブルのcount項目をインクリメントしてUPDATEする方法は？](https://teratail.com/questions/14809 )