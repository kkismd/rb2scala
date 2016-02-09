制御構造
====

分岐 {#branches}
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - if-else
  - |
    if a == b
      "equal!"
    else
      "not equal!"
    end

    if a == b
      "ok"
    end
  - |
    if (a == b) {
      "equal!"
    }
    else {
      "not equal!"
    }

    if (a == b) {
      "ok"
    }
  - Scalaでもifは式であり、値を返すことができる。後置式はない。
-
  - unless
  - |
    unless foo?
      "not foo"
    else
      "foo"
    end

    unless foo?
      "ng"
    end
  - |
    if (!isFoo) {
      "not foo"
    }
    else {
      "foo"
    }

    if (!isFoo) {
      "ng"
    }
  - Scalaにunlessはない。
-
  - case
  - |
    case hoge
    when 1
      "one"
    when 2, 3
      "two or three"
    else
      "other case"
    end
  - |
    hoge match {
      case 1 =>
        "foo"
      case 2|3 =>
        "two or three"
      case _ =>
        "other case"
    }
  - Rubyのcase式もScalaのmatch式もどちらも強力だがここでは最も基本的な形を挙げている。
```

Scalaのmatch式も、case のひとつひとつに複数の式を書ける。

```scala
obj match {
  case hoge =>
    ...
    ... ここの部分は複数行書ける!
    ...
  case fuga =>
    ...
}
```

繰り返し {#loops}
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - while
  - |
    while true
      puts("Hello")
    end
  - |
    while (true) {
      println("Hello")
    }
  - ''
-
  - until
  - |
    until f.eof?
      print f.gets
    end
  - |
    while (!f.isEof) {
      println(f.getLine)
    }
  - untilはない。
-
  - for
  - |
    for i in [1,2,3]
      print i * 2, "\n"
    end
  - |
    for (i <- Seq(1,2,3)) {
      println(i * 2)
    }
  - Scalaのfor式はもっと多機能だがここでは基本的な形を挙げている。
-
  - break
  - |
    i = 0
    while true
      puts i
      i += 1
      if i > 10
        break
      end
    end
  - |
    import scala.util.control.Breaks
    val breaks = new Breaks
    var i = 0
    breaks.breakable {
     while (true) {
       println(i)
       i += 1
       if (i > 10) breaks.break()
     }
    }
  - ループのブレイクが構文として用意されていないので、標準ライブラリの Breaks を使う必要がある。
-
  - next, redo, retry
  - |
    lines.each do |line|
      next if line.blank?
      puts line
    end
  - |
    lines.foreach { line =>
      if (!line.isEmpty) {
        println(line)
      }
    }
  - next, redo, retryなどの構文はないのでifなどを使って実装する必要がある。
```

イテレータ {#iterater}
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - each
  - |
    [1, 2, 3].each do |num|
      puts num
    end
  - |
    List(1, 2, 3).foreach { num =>
      println(num)
    }
  - ''
-
  - map
  - |
    [1, 2, 3].map do |num|
      num * 2
    end
    # => [2, 4, 6]
  - |
    List(1, 2, 3).map { num =>
      num * 2
    }
    // => List(2, 4, 6)
  - ''
-
  - select
  - |
    [1, 2, 3, 4].select do |num|
      num % 2 == 0
    end
    # => [2, 4]
  - |
    List(1, 2, 3, 4).filter { num =>
      num % 2 == 0
    }
    // => List(2, 4)
  - ''
-
  - reject
  - |
    [1, 2, 3, 4].reject do |num|
      num % 2 == 0
    end
    # => [1, 3]
  - |
    List(1, 2, 3, 4).filterNot { num =>
      num % 2 == 0
    }
    // => List(1, 3)
  - ''
-
  - inject
  - |
    [1, 2, 3, 4].inject(0) do |sum, n|
      sum + n
    end
    # => 10
  - |
    List(1, 2, 3, 4).foldLeft(0) { (sum, n) =>
      sum + n
    }
    // => 10
  - ''
-
  - to_proc(&)を使った省略記法
  - |
    [1, 2, 3].map(&:to_s)
    # => ["1", "2", "3"]
  - |
    List(1, 2, 3).map(_.toString)
    // => List[String] = List("1", "2", "3")
  - プレースホルダ `_` を使うことで同じくらい短く書ける。
```

### ブロックつきメソッド

作り方と使い方

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    def foo(bar, &block)
      yield bar
    end

    foo(1) do |i|
      puts i * 2
    end
  - |
    def foo(bar: Int)(block: Int => Unit): Unit = {
      block(bar)
    }

    foo(1) { i =>
      println(i * 2)
    }
```

Scalaでは制御構造に似た見た目の関数をユーザーが任意に定義できるように、二つの文法規則を持っている。
* 関数の引数を複数のカッコでグループに分けることができる。
* 関数適用のカッコ `()` はブラケット `{}` で書くこともできる。

つまり上記の例は関数`foo`に整数と無名関数の二つの値を（引数グループを分けて）渡している。
わかりやすく分けて書くと下記のようになる。

```scala
// 一番目の引数は整数値
val bar = 1
// 二番目の引数は無名関数
val block = (i: Int) => { println(i * 2) }

// 二つの値を分けて適用する
foo(bar)(block)
```



例外処理 {#exceptions}
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 例外の送出
  - raise StandardError.new("例外が起きました")
  - throw new RuntimeException("例外が起きました")
  - ''
-
  - 例外の捕捉
  - |
    begin
      do_something
    rescue ZeroDivisionError => e
      recover(e)
    ensure
      must_to_do
    end
  - |
    try {
      doSomething
    }
    catch {
      case e: ArithmeticException =>
        recover(e)
    }
    finally {
      mustToDo
    }
  - ''
```

メソッド呼び出し、return {#callreturn}
----

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - メソッド呼び出し（引数なし）
  - foo.bar
  - foo.bar
  - ''
-
  - メソッド呼び出し（引数あり）
  - foo.bar(1, 2)
  - foo.bar(1, 2)
  - ''
-
  - 値の返却
  - return 1
  - return 1
  - 最後のretrunを省略すると、Rubyと同じように最後に評価された値を返す。
```
