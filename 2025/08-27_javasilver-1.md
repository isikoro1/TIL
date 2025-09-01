# 学習ノート 2025-08-27 — javaSilver-1

## 今日学んだこと

### Java クラスの書き方
- 参考動画　Oracle Certified Java Programmer, Silver SE 8 認定資格試験(1Z0-808)対策ポイント解説セミナー（1）
　https://youtu.be/2yx0b5y2c7s?si=_yVTFdxnSNzJ7eUx

- 識別子の命名規則
    - 先頭は英字、$、_のみ

- if 文などのブロックが一文で構成される場合は、中括弧｛｝を省略可

- package文はソースファイル先頭に一回のみ記述可能。import文は複数回記述可能

- mainメソッドの宣言方法
~~~java
public static void main(String[] args) { /* 処理 */ }
~~~

### 変数のスコープ
- 変数のスコープ...変数が見える(=特定の識別子で参照できる)範囲
    - インスタンス変数 / static変数...クラス内の全てのブロックからアクセス可能
    - ローカル変数 / メソッドやif文などの特定のブロック内でのみアクセス可能

### プリミティブ型と参照型
- プリミティブ型（基本データ型）
    - 値そのものを格納する
        - 整数型(byte, short, int , long), 浮動小数点型
        - プリミティブ型に対応したラッパークラスがある
            - オートボクシングにより相互代入可能

### Java SE 7 の新機能
- リテラル
    - バイナリリテラル...整数型（byte, short, int long）を2進数で表記
        - int i1 = 0b1010;　または int i2 =  0B1010;
        　リテラルは"0b"または"0B"で開始

    - アンダースコアつきリテラル
        - int i = 0x5_2; //16進数
        - foloat pi = 3.14_15f;
        ※コンパイル時にはアンダースコアは自動的に外れる

### StringBuilderクラス
- java.lang.StringBuilderクラス - 文字列の可変シーケンス
    - append(引数)...引数をStringBuilderの文字列シーケンスに追加
    - insert(int offsetm, 引数) ... StringBuilderのoffset番目の位置に引数を挿入
    - replace(int start, int end, String str)... start番目からend番目を文字列strで置換
        - Stringクラスのreplaceとの違いを確認
    
    Point: String クラスのreplaceメソッド
    public String replace(CharSequence taget, CharSequence replacement)
    targetに一致する文字列をreplacementで置換する。
    置換は文字列の先頭から終端まで行う
        例）: "aaa".replace("aa", "bb"); → "bba"
        例）: "aaaa".replace("aa", "bb"); → "bbbb"


## 疑問点・調べたいこと
- オートボクシングがまだふんわり


## 実験したコード / メモ
~~~java
public static void main(String[] args) { /* 処理 */ }
~~~

## 明日の目標
- 