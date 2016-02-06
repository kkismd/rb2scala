その他おぼえがき
====

## 命名規則

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

## map, select, reject, inject

map

```ruby
numbers = [1, 2, 3]
numbers.map do |num|
  num * 2
end
# => [2, 4, 6]
```

```scala
val numbers = List(1, 2, 3)
numbers.map { num =>
  num * 2
}
// => List(2, 4, 6)
```

select

```ruby
numbers = [1, 2, 3, 4]
numbers.select do |num|
  num % 2 == 0
end
# => [2, 4]
```
```scala
val numbers = List(1, 2, 3, 4)
numbers.filter { num =>
  num % 2 == 0
}
// => List(2, 4)
```

reject

```ruby
numbers = [1, 2, 3, 4]
numbers.reject do |num|
  num % 2 == 0
end
# => [1, 3]
```
```scala
val numbers = List(1, 2, 3, 4)
numbers.filterNot { num =>
  num % 2 == 0
}
// => List(1, 3)
```

inject

```ruby
numbers = [1, 2, 3, 4]
numbers.inject(0) do |sum, n|
  sum + n
end
# => 10
```
```scala
val numbers = List(1, 2, 3, 4)
numbers.foldLeft(0) { (sum, n) =>
  sum + n
}
// => 10
```


## Array#join

`TraversableOnce#mkString`

```
List("foo", "bar", "baz").mkString(",")  // => "foo,bar,baz"
```

ListやSeqで使えるっぽい

## Enumerable#all? Enumerable#any?

`IterableLike#forall` すべての述語が真のとき真を返す
`IterableLike#exists` 述語がひとつでも真ならば真を返す

```
numbers.forall(_.isEven) //すべてが偶数か？
numbers.exists(_.isOdd) // 一つでも奇数があるか？
```


## パターンマッチで(最初のうち)気付きにくいこと

```
obj match {
  case hoge =>
    ...
    ... ここの部分は複数行書ける!
    ...
  case fuga =>
    ...
}
```
