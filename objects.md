オブジェクト指向
====

クラス
----

### クラスの宣言と継承

Ruby
```ruby
class Foo < Bar
end
```

Scala
```scala
class Foo extends Bar {
}
```

### コンストラクタ

Rubyでは`initialize`という名前のメソッドを定義する。

```ruby
class Foo
  def def initialize(bar)
    # new した時点でここが実行される
  end
end
```
Scalaにはコンストラクタを複数定義できるが、ここではデフォルトのコンストラクタについて説明する。

デフォルトのコンストラクタはクラス定義のブラケット内にそのまま記述できる。
引数はクラス名の後ろのカッコ内に書く。

```scala
class Foo(bar: Int) {
  // new した時点でここが実行される
}
```

モジュール
----

Ruby
```ruby
module Foo
  def bar
  end
end
```

Scala
```scala
trait Foo {
  def bar: Unit = {
  }
}
```

barというメソッドを持つtrait Fooを定義することができる。

### Mixin

Scalaではtraitを継承することでmixinを行う。

Ruby
```ruby
module Bar
end

class Foo
  include Bar
end
```

Scala
```scala
trait Bar {
}

class Foo extends Bar {
}
```

ひとつのクラスが複数のtraitをmixinする場合、二つ目以降は with というキーワードを使う。

Scala
```scala
class Foo extends Bar with Baz with Hoge {
}
```

TODO: `prepend`や`using`についても調べて書く

### 名前空間

Rubyではモジュールを名前空間として使うことができる。

Ruby
```ruby
module Foo
  module Bar
    class Baz
    end
  end
end

baz = Foo::Bar::Baz.new
```

Scalaではパッケージのほか、シングルトンオブジェクトも名前空間として使うことができる。

Scala
```scala
package foo
object Bar {
  class Baz {
  }
}

val baz = new foo.Bar.Baz()
```

TODO: `import` について書く

メソッド
----

キーワードは同じ `def`
引数と返り値の型を指定する。

Ruby
```ruby
class Foo
  def bar(a, b)
    a + b
  end
end
```

Scala
```scala
class Foo {
  def bar(a: Int, b: Int): Int = {
    a + b
  }
}
```

### プロパティとアクセサ

デフォルトのゲッター、セッター

Ruby
```Ruby
class Foo
  attr_accessor :bar, :baz
  def initialize(bar, baz)
    @bar = bar
    @baz = baz
  end
end

foo = Foo.new(1, "abc")
foo.bar  # => 1
foo.baz  # => "abc"
```

Scala
```scala
class Foo(var bar: Int, var baz: String) {
}

val foo = new Foo(1, "abc")
foo.bar  // => 1
foo.baz  // => "abc"
```

セッターの実装

Ruby
```ruby
class Foo
  attr_reader :bar
  def bar=(i)
    @bar = i
  end
end

foo = Foo.new
foo.bar = 1
foo.bar  # => 1
```

Scala
```scala
class Foo {
  private var _bar: Int = _
  def bar = _bar
  def bar_=(i: Int): Unit = this._bar = i
}

val foo = new Foo()
foo.bar = 1
foo.bar  // => 1
```

Scalaのセッターメソッドは `def 変数名_=(引数): Unit = ???` という形で定義する。


### 演算子メソッド

Rubyでメソッドとして再定義可能な演算子
```
|  ^  &  <=>  ==  ===  =~  >   >=  <   <=   <<  >>
 +  -  *  /    %   **   ~   +@  -@  []  []=  ` ! != !~
```

Scalaで再定義できない予約語、キーワード
（[FAQ How do I find what some symbol means or does?](http://docs.scala-lang.org/tutorials/FAQ/finding-symbols.html)より引用）
（これ以外の記号、英数字は使えるらしい）

```
// Keywords
<-  // Used on for-comprehensions, to separate pattern from generator
=>  // Used for function types, function literals and import renaming
// Reserved
( )        // Delimit expressions and parameters
[ ]        // Delimit type parameters
{ }        // Delimit blocks
.          // Method call and path separator
// /* */   // Comments
#          // Used in type notations
:          // Type ascription or context bounds
<: >: <%   // Upper, lower and view bounds
" """      // Strings
'          // Indicate symbols and characters
@          // Annotations and variable binding on pattern matching
`          // Denote constant or enable arbitrary identifiers
,          // Parameter separator
;          // Statement separator
_*         // vararg expansion
_          // Many different meanings
```

どちらも記号を名前としたメソッドを定義することで演算子を定義できる。

```ruby
class Foo
  def +(other)
    "add method"
  end
end

foo1 = Foo.new
foo2 = Foo.new
foo1 + foo2  # "add method"
```

```scala
class Foo {
  def +(other: Foo): String = "add method"
}

val foo1 = new Foo
val foo2 = new Foo
foo1 + foo2  // "add method"
```


### 引数のデフォルト値

Ruby
```ruby
class Foo
  def bar(baz = 1)
    baz
  end
end

foo = Foo.new
foo.bar()  # => 1
foo.bar(2)  # => 2
```

Scala
```scala
class Foo {
  def bar(baz: Int = 1): Int = {
    baz
  }
}

val foo = new Foo()
foo.bar()  // => 1
foo.bar(2)  // => 2
```


### 可変長引数

Rubyでは定義するときも呼び出すときも `*` という記号をまえにつける。

```ruby
class Foo
  def bar(baz, *hoge)
    # 2つめ以降の引数はhogeに配列として入る
  end
end

foo = Foo.new
baz = 1
hoge = ["foo", "bar"]
foo.bar(baz, *hoge)
```

Scalaでは定義するときは `*`をうしろにつけ、呼び出すときは `:_*` という記号をうしろにつける。

```scala
class Foo {
  def bar(baz: Int, bar: String*): Unit = {
    // 2つめ以降の引数は bar にSeqとして入る
  }
}

val foo = new Foo
val baz = 1
val hoge = Seq("foo", "bar")
foo.bar(baz, hoge:_*)
```


### キーワード引数

Ruby
```ruby
def foo(bar:, baz: 1)
end

foo("hello", 12)
foo("hello")
```

Scala
```scala
def foo(bar: String, baz: Int = 1): Unit = {
}

foo("hello", 12)
foo("hello")
```

Scalaでは普通に定義したメソッドに名前付き引数を渡して呼び出すことができる。

### クラスメソッド

Ruby
```ruby
class Foo
  class << self
    def bar(baz)
  end
end
```

Scala
```scala
class Foo {
}
object Bar {
  def bar(baz: Int): Unit = {
  }
}
```

### 可視性と呼び出し制限

Ruby
```ruby
class Foo
  protected
  def bar()
  end

  private
  def baz()
  end
end
```

Scala
```scala
class Foo {
  def private bar(): Unit = {
  }
  def private[this] baz(): Unit = {
  }
}
```

RubyとScalaの可視性に関する機能は厳密には一致しない。
たとえばScalaの`private`はRubyの`protected`と違ってサブクラスからはアクセスできない。
