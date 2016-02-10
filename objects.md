オブジェクト指向
====

クラス {#classes}
----

### クラスの宣言と継承

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    # Barを継承する場合
    class Foo < Bar
    end
  - |
    // Barを継承する場合
    class Foo extends Bar {
    }
-
  - |
    # 継承しない場合
    class Foo
    end
  - |
    // 継承しない場合
    class Foo {
    }
```


### コンストラクタ

Rubyでは`initialize`という名前のメソッドを定義する。
Scalaにはコンストラクタを複数定義できるが、ここではデフォルトのコンストラクタについて説明する。
デフォルトのコンストラクタはクラス定義のブラケット内にそのまま記述する。
引数はクラス名の後ろのカッコ内に書く。

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    class Foo
      def def initialize(bar)
        # new した時点でここが実行される
      end
    end
  - |
    class Foo(bar: Int) {
      // new した時点でここが実行される
    }
```

メソッド {#methods}
----

キーワードは同じ `def`
引数と返り値の型を指定する。

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    class Foo
      def bar(a, b)
        a + b
      end
    end
  - |
    class Foo {
      def bar(a: Int, b: Int): Int = {
        a + b
      }
    }
```

### プロパティとアクセサ

デフォルトのゲッター、セッター

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    class Foo
      attr_accessor :bar
      def initialize(bar)
        @bar = bar
      end
    end

    foo = Foo.new(1)
    foo.bar  # => 1
    foo.bar = 2
    foo.bar  # => 2
  - |
    class Foo(var bar: Int) {
    }

    val foo = new Foo(1, "abc")
    foo.bar  // => 1
    foo.bar = 2
    foo.bar  // => 2
```

セッターの実装

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    class Foo
      attr_reader :bar
      def bar=(i)
        @bar = i
      end
    end

    foo = Foo.new
    foo.bar = 1
    foo.bar  # => 1
  - |
    class Foo {
      private var _bar: Int = _
      def bar = _bar
      def bar_=(i: Int): Unit = this._bar = i
    }

    val foo = new Foo()
    foo.bar = 1
    foo.bar  // => 1
```

Scalaのセッターメソッドは `変数名_=(引数)` という名前で定義する。

### 演算子メソッド

どちらも記号を名前としたメソッドを定義することで演算子を定義できる。

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    class Foo
      def +(other)
        "add method"
      end
    end

    foo1 = Foo.new
    foo2 = Foo.new
    foo1 + foo2  # "add method"
  - |
    class Foo {
      def +(other: Foo): String = "add method"
    }

    val foo1 = new Foo
    val foo2 = new Foo
    foo1 + foo2  // "add method"
```

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

### メソッドの引数

```ymltbl
-
  - 種類
  - Ruby
  - Scala
  - 備考
-
  - 引数のデフォルト値
  - |
    class Foo
      def bar(baz = 1)
        baz
      end
    end

    foo = Foo.new
    foo.bar()  # => 1
    foo.bar(2)  # => 2
  - |
    class Foo {
      def bar(baz: Int = 1): Int = {
        baz
      }
    }

    val foo = new Foo()
    foo.bar()  // => 1
    foo.bar(2)  // => 2
  - ''
-
  - '可変長引数'
  - |
    class Foo
      def bar(baz, *hoge)
        # 2つめ以降の引数はhogeに配列として入る
      end
    end

    foo = Foo.new
    foo.bar(1, "foo", "bar")
    baz = 1
    hoge = ["foo", "bar"]
    foo.bar(baz, *hoge)
  - |
    class Foo {
      def bar(baz: Int, bar: String*): Unit = {
        // 2つめ以降の引数は bar にSeqとして入る
      }
    }

    val foo = new Foo
    foo.bar(1, "foo", "bar")
    val baz = 1
    val hoge = Seq("foo", "bar")
    foo.bar(baz, hoge:_*)
  - |
    Rubyでは定義するときも呼び出すときも `*` という記号を前につける。
    Scalaでは定義するときは `*` を後ろにつけ、呼び出すときは `:_*` という記号を後ろにつける。
-
  - 'キーワード引数'
  - |
    def foo(bar:, baz: 1)
    end

    foo(bar: "hello", baz: 12)
    foo(bar: "hello")
  - |
    def foo(bar: String, baz: Int = 1): Unit = {
    }

    foo(bar = "hello", baz = 12)
    foo(bar = "hello")
  - 'Scalaでは普通に定義したメソッドに名前付き引数を渡して呼び出すことができる。'
```

### クラスメソッド

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    class Foo
      class << self
        def bar(baz)
      end
    end
  - |
    class Foo {
    }
    object Foo {
      def bar(baz: Int): Unit = {
      }
    }
```
クラスと同名のシングルトン（コンパニオンオブジェクト）を定義し、その中にメソッドを記述する。

### 可視性と呼び出し制限

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    class Foo
      protected
      def bar()
      end

      private
      def baz()
      end
    end
  - |
    class Foo {
      def private bar(): Unit = {
      }
      def private[this] baz(): Unit = {
      }
    }
```

RubyとScalaの可視性に関する機能は厳密には一致しない。
たとえばScalaの`private`はRubyの`protected`と違ってサブクラスからはアクセスできない。

モジュール {#modules}
----

Scalaではトレイトを継承することでmixinを行う。
barというメソッドを持つトレイトFooを定義し、Bazで継承する。

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    module Foo
      def bar
      end
    end

    class Baz
      include Foo
    end
  - |
    trait Foo {
      def bar: Unit = {
      }
    }

    class Baz extends Foo {
    }
```

ひとつのクラスが複数のtraitをmixinする場合、二つ目以降は with というキーワードを使う。

```scala
class Foo extends Bar with Baz with Hoge {
}
```

### 名前空間

Rubyではモジュールを名前空間として使うことができる。
Scalaではパッケージのほか、シングルトンオブジェクトも名前空間として使うことができる。

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    module Foo
      module Bar
        class Baz
        end
      end
    end

    baz = Foo::Bar::Baz.new
  - |
    package foo
    object Bar {
      class Baz {
      }
    }

    val baz = new foo.Bar.Baz()
```

TODO: `import` について書く

オープンクラス {#openclass}
----

既存のクラスにメソッドを追加する場合、`implicit class`という仕組みを使う。
パッケージのスコープを使って、拡張の影響範囲をコントロールすることができる。
RubyのRefinementsに相当する。

```ymltbl
-
  - Ruby
  - Scala
-
  - |
    module CoreExtentions
      module IntExtention
        refine Integer do
          def plus(other)
            self + other
          end
        end
      end
    end

    # 違うファイルから使用する
    require 'core_extentions/int_extention'
    using CoreExtentions::IntExtention
    1.plus(2)  # => 3
  - |
    package coreExtentions
    implicit class IntExtention(self: Int) {
      def plus(other: Int): Int = self + other
    }

    // 違う名前空間からインポートして有効化する
    import coreExtentions.IntExtention
    1.plus(2)  // => 3
```

下記のような既存のメソッドの挙動を修正する「モンキーパッチ」は行うことができない。
* クラスを再オープンしてメソッドを上書きすること
* alias_method_chain
* Module#prepend
