式、値
=====

数値
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 整数
  - '123'
  - |
    123
    2147483647L
  - 整数は32bit(Int),64bit(Long)の２種類がある
-
  - 実数
  - '123.45'
  - |
    123.45
    123.
    123.45d
    123.45f
  -  実数はDoubleとFloat
-
  - 浮動小数
  - '1.2e-3'
  - '1.2e-3'
  - ''
-
  - 16進整数
  - '0xffff'
  - '0xffff'
  - ''
-
  - 8進数
  - '0377'
  - ''
  - ゼロから始める8進数表記はScala 2.11から非推奨
-
  - 2進整数
  - '0b1011'
  - ''
  - 2進数のリテラルなし
-
  - 桁区切り文字
  - '1_000_000_000'
  - ''
  - 桁区切り文字はなし
```

文字列
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - ダブルクォート
  - '"this is a string expression\n"'
  - '"this is a string expression\n"'
  - ''
-
  - シングルクォート
  - '''this is a string expression'''
  - ''
  - シングルクォートはChar型やシンボルを表すため文字列には使えない
-
  - シンボル
  - ':aaa'
  - '''aaa'
  - |
    'シングルクォートを単語の先頭だけにつけるとシンボルを表す式になる。
    ''a'' のように１文字の両端を囲むとChar型のオブジェクトになる。'
-
  - ヒアドキュメント
  - |-
    <<EOF
    foo
    bar
    baz
    EOF
  - |-
    """foo
    bar
    baz
    """
  - 改行を含む文字列はダブルクォートを３つ重ねる(Raw String)。バックスラッシュによるエスケープが効かない。
-
  - 式埋め込み
  - '"foo #{1 + 2} baz"'
  - 's"foo ${1 + 2} baz"'
  - ダブルクォートの前に小文字のs (interpolator) を置く
-
  - フォーマット
  - |
    sprintf("foo %d baz", 123)
    "foo %d baz" % [123]
  - '"foo %d baz".format(123)'
  - ''
-
  - 正規表現
  - /^[abc]+/
  - '"^[abc]+".r'
  - 正規表現専用のリテラル表記はないが、文字列オブジェクトの .r というメソッドを呼び出す事でRegexクラスのオブジェクトを生成する
```


変数
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 変数
  - a = 123
  - var a = 123
  - ''
-
  - 定数
  - A = 123
  - val a = 123
  - 変数をvalで宣言すると再代入がコンパイルエラーになる（Rubyの定数より厳格）
```

演算子
----

ScalaもRubyと同じように演算子の一部がメソッドのシンタックスシュガーとして定義されている。

`1 + 2` は `1.+(2)` のシンタックスシュガー


```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 代入
  - foo = bar
  - foo = bar
  - 再代入が必要な時はvarで宣言する
-
  - 配列参照
  - array[1]
  - array(1)
  - カッコによる配列参照はメソッド呼び出し .apply(n) のシンタックスシュガー
-
  - 属性参照
  - foo.bar
  - foo.bar
  - 引数なしのメソッドをカッコ省略できる
-
  - 自己代入
  - foo += 1
  - foo += 1
  - 再代入があるのでvar変数として宣言が必要
-
  - 多重代入
  - |
    foo, bar, baz = 1, 2, 3
    foo, bar, baz = [1, 2, 3]
  - |
    (foo, bar, baz) = (1, 2, 3)
    Array(foo, bar, baz) = Array(1, 2, 3)
  - 多重代入はパターンマッチのシンタックスシュガー
-
  - 範囲式
  - 1 .. 20
  - |
    1 to 20
    1.to(20)
  - 整数クラスの .to() メソッドを使う。引数が１つしかないメソッドはドットやカッコを省略できる。
-
  - アンド条件
  - |
    foo && bar
    foo and bar
  - foo && bar
  - 演算子 and は使えない
-
  - オア条件
  - |
    foo || bar
    foo or bar
  - foo || bar
  - 演算子 or は使えない
-
  - 否定
  - |
    !foo
    not foo
  - '!foo'
  - 演算子notは使えない
-
  - ３項演算子
  - 'obj == 1 ? foo : bar'
  - 'if (obj == 1) foo else bar'
  - ３項演算子がないのでif式を使う

```

ラムダ式
----

Ruby
```ruby
f = ->(a,b){ a + b }
f.(1, 2) # => 3
```

Scala
```scala
//ラムダ式の型を省略せずに書いた場合
val f = (a: Int, b: Int) => { a + b }: Int
//返り値の型は推論できるが引数の型は省略できない
val f = (a: Int, b: Int) => { a + b }

//引数を位置パラメータに置き換えた場合
val f = (_: Int) + (_: Int)

//変数のほうに型を明記するとラムダ式の型は省略できる
val f: (Int,Int) => Int = (a,b) => { a + b }

f(1, 2) // => 3
```

配列、ハッシュ
----

ArrayとHashがあれば大抵間にあうRubyに比べると、Scalaには用途別に様々なコレクションクラスがある。
データ構造によって挙動や動作効率が違ってくるので、違いをおさえて使い分けるべきとされている。
[コレクションAPI](http://docs.scala-lang.org/ja/overviews/collections/overview.html)

Rubyでは配列やハッシュのインスタンスを生成するのに専用のリテラルが用意されているが、Scalaではそういうものは用意されていない。
代わりに、コンパニオンオブジェクトのapplyメソッド（とその省略形）を呼ぶ事でインスタンスを生成することができる。

### 配列

Rubyでの配列にあたるものは、Array, Listなどがある。

Ruby
```ruby
[1, 2, 3]
```

Scala
```scala
Array(1, 2, 3)
List(1, 2, 3)
```

* `Array(1,2,3)`は`Array.apply(1,2,3)`の省略形。

Rubyでは一つの配列の中に数値、文字列、その他オブジェクトなど自由に混在できる。
Scalaでも `Array[Any]` という型のインスタンスを用意すれば同様の事はできるが、型安全性の観点から推奨されていない。
Rubyからの移植などやむを得ないとき以外は`Array[Int]`や`Array[String]`など型を制限して使うようにしたい。


### ハッシュ

RubyでのハッシュにあたるものはMap

Ruby
```ruby
{foo: "foo", bar: "bar", baz: "baz"}
```

Scala
```scala
Map('foo -> "foo", 'bar -> "bar", 'baz -> "baz")
```
