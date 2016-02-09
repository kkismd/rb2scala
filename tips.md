その他おぼえがき
====

命名規則 {#naming}
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 変数名、メソッド名
  - snake_case
  - camelCase
  - ''
-
  - クラス名
  - CamelCase
  - CamelCase
  - ''
-
  - インスタンス変数
  - '@name_with_atmark'
  - this.camelCase
  - ''
-
  - グローバル変数
  - $name_with_doller
  - DO NOT USE IT
  - 使うな
-
  - 定数
  - CAPITAL_WITH_UNDERSCORE = 123
  - val CamelCase = 123
  - ''
-
  - 述語
  - ready?
  - isReady
  - メソッド名に疑問符は使えないので `is` を前置する
```


Array#join {#arrayjoin}
----

`TraversableOnce#mkString`

```scala
List("foo", "bar", "baz").mkString(",")  // => "foo,bar,baz"
```

ListやSeqで使えるっぽい

Enumerable#all? Enumerable#any? {#allany}
----

`IterableLike#forall` すべての述語が真のとき真を返す
`IterableLike#exists` 述語がひとつでも真ならば真を返す

```scala
numbers.forall(_.isEven) //すべてが偶数か？
numbers.exists(_.isOdd) // 一つでも奇数があるか？
```
