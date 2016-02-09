リテラル、変数、式
=====

数値 {#numbers}
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
  - 整数は32bit(Int),64bit(Long)の２種類に分かれる。RubyのBignumと違い大きさに制限がある。
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
  - 指数表記
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

### Longよりも大きな整数

BigIntクラスを使う

```scala
BigInt(Long.MaxValue)  // => scala.math.BigInt = 9223372036854775807
BigInt(Long.MaxValue) + 1  // => scala.math.BigInt = 9223372036854775808
BigInt(9223372036854775808)  // => error: integer number too large
BigInt("9223372036854775808")  // => scala.math.BigInt = 9223372036854775808
```

Longの最大値よりも大きな数を数値リテラルとして直接記述することはできない。
BigIntへのコンストラクタに渡す必要があるときは文字列として記述する。

実数はBigDecimalクラスを使う。

文字列 {#strings}
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
    シングルクォートを単語の先頭だけにつけるとシンボルを表す式になる。
    'a' のように１文字の両端を囲むとChar型のオブジェクトになる。
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
  - ヒアドキュメントはないので、改行を含む文字列はRaw Stringで代用する。バックスラッシュによるエスケープが効かない。
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


変数 {#variables}
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
  - 'var a: Int = 123'
  - ''
-
  - 定数
  - A = 123
  - 'val a: Int = 123'
  - 変数をvalで宣言すると再代入がコンパイルエラーになる（Rubyの定数より厳格）
```

### 変数と型

Rubyとの大きな違いとして、Scalaはコンパイル時に変数やメソッド、関数の型が決定される。
下記のようなケースはコンパイルエラーとなる。
（メソッドと関数は異なるものだが、以下では明確な区別が必要なとき以外は広い意味で「関数」として総称する）

* 変数に対して決められた型以外の値を代入する
* 関数に対して決められた型以外の引数を渡す
* 関数が決められた型以外の値を返す

型注釈は型推論によって省略できる場合もあるが、複雑なケースでは推論できないこともある。

変数の型注釈

```scala
val 変数名: 型名 = 値
var 変数名: 型名 = 値
```

型推論の例

```scala
val name = "たろう"
```

変数nameの型はStringであることが推論されている。

メソッド、関数 {#functions}
----

メソッドはクラスやオブジェクトに属する。関数はクラスやオブジェクトとは独立している。

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - メソッド
  - |
    def foo(i, j)
      i + j
    end
  - |
    def foo(i: Int, j:Int): Int = {
      i + j
    }
  - '引数と返り値の型注釈、関数本体のブラケットなどを省略せず書いた場合'
-
  - 無名関数
  - |
    f = ->(a,b){ a + b }
    f.call(1, 2) # => 3
  - |
    val f = (a: Int, b: Int) => { a + b }: Int
    f.apply(1, 2) // => 3
  - applyを省略して f(1,2) と書くことができる

```

### メソッドの型注釈

```scala
def メソッド名(引数名: 型名, 引数名: 型名): 返り値の型名 = {
  本体
}
```

値を返す必要がない場合、`Unit`という型を記述する。


### メソッドと関数の型推論

Intクラスの .+() メソッドはIntの値を返すことから、foo()の返り値の型が Int であることが推論できる。
そのため、返り値の型は省略できる。

```scala
// 返り値の型を省略
def foo(i: Int, j: Int) = {
  i + j
}
```

[Scala Style Guide](http://docs.scala-lang.org/style/)では、パブリックなメソッドは明示的に型注釈を書いておくべきとされている。
（可視性などメソッドの詳細については[オブジェクト志向](objects.html)を参照）

### 無名関数の型注釈

メソッドと同じく型推論により型注釈を省略できる。

```scala
//返り値の型は推論できるが引数の型は省略できない
val f = (a: Int, b: Int) => { a + b }
```

関数を変数に代入するとき、その変数は「関数」という型になる。
関数の型は、引数の型と返り値の型を `=>` という記号でつないで表す。

```scala
// 引数のない関数の場合 (Function0)
() => Int

// 1引数関数の場合 (Function1)
Int => Int

// 2引数関数の場合 (Function2)
(Int, Int) => Int
```

変数に型を記述すると、関数の側の型注釈を省略することができる。

```scala
val f: (Int, Int) => Int = (a,b) => { a + b }
```

演算子 {#operators}
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
  - ''
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
    (foo, bar, baz) = (1, 2, 3)  // カッコで囲むとタプル
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
  - 演算子 and はない
-
  - オア条件
  - |
    foo || bar
    foo or bar
  - foo || bar
  - 演算子 or はない
-
  - 否定
  - |
    !foo
    not foo
  - '!foo'
  - 演算子 not はない
-
  - ３項演算子
  - 'obj == 1 ? foo : bar'
  - 'if (obj == 1) foo else bar'
  - ３項演算子がないのでif式を使う

```

配列、ハッシュ {#arrayhash}
----

ArrayとHashがあれば大抵間にあうRubyに比べると、Scalaには用途別に様々なコレクションクラスがある。
データ構造によって挙動や動作効率が違ってくるので、違いをおさえて使い分けるべきとされている。
[コレクションAPI](http://docs.scala-lang.org/ja/overviews/collections/overview.html)

Rubyでは配列やハッシュのインスタンスを生成するのに専用のリテラルが用意されているが、Scalaではそういうものは用意されていない。
代わりに、コンパニオンオブジェクトのapplyメソッド（とその省略形）を呼ぶ事でインスタンスを生成することができる。

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 配列
  - '[1, 2, 3]'
  - |
    Array(1, 2, 3)
    List(1, 2, 3)
  - Rubyでの配列にあたるものは、Array, Listなどがある。
-
  - ハッシュ
  - '{foo: "foo", bar: "bar", baz: "baz"}'
  - Map('foo -> "foo", 'bar -> "bar", 'baz -> "baz")
  - RubyでのハッシュにあたるものはMap
```

* `Array(1,2,3)`は`Array.apply(1,2,3)`の省略形。

### Mapの読み書き

ScalaのMapには immutable（不変）なものと mutable（可変）なものがある。
両者は効率と安全性のトレードオフで使い分ける。
一般的にはパフォーマンスに問題のない場合は不変コレクションを使うことが推奨される。

単に `Map`と記述した場合、不変コレクションの `scala.collection.immutable.Map` クラスを指す。
`scala.collection.mutable.Map` を使用する場合はインポートなどが必要。

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 値の格納
  - hash["key"] = 100
  - |
    // immutable ... 追加or更新された新しいインスタンスを返す
    val newMap = map.updated("key" -> 100)
    // mutable ... レシーバのインスタンスを直接更新する
    map("key") = 100
  - ''
-
  - 値の読み出し
  - hash["key"]  # => 100
  - |
    map.get("key")  // => Some(100)
    map.get("bad key")  // => None
    map.getOrElse("key", 0)  // => 100
    map.getOrElse("bad key", 0) // => 0
  - ''
```

Scalaの`Map#get`はOption型の値を返す。
* 値があるときは Some(値)
* 値がないときは None

`Map#getOrElse`を使うとOptionを介さず値を取り出すことができる。
キーに対応する値がないときは２番目の引数に指定したデフォルト値が返る。

### 型パラメータ

Rubyでは一つの配列の中に数値、文字列、その他オブジェクトなど自由に混在できる。
Scalaでは原則として1種類のオブジェクトだけを格納する。

別の型を格納する型の表記方法は `外側の型[内側の型]` となる。`[]`の中を型パラメータという。
* 「Intの配列」 `Array[Int]`
* 「文字列のリスト」 `List[String]`

Mapのキーと値のように、内側の型を複数もつ型も定義できる。また、型パラメータはネストできる。
* 「文字列をキーとして整数を値とするMap」 `Map[String, Int]`
* 「シンボルをキーとして整数の配列を値とするMap」 `Map[Symbol, Array[Int]]`

すべてのクラスの基底クラスである`Any`を指定して`Array[Any]` という型のインスタンスを用意すればRubyと同様の事はできるが、型安全性の観点から推奨されていない。
