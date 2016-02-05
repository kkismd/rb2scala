制御構造
====

if-then-else
----

Ruby
```ruby
if a = b
  "equal!"
else
  "not equal!"
end
```

Scala
```scala
if (a == b) {
  "equal!"
}
else {
  "not equal!"
}
```

Scalaでもifは式であり、値を返すことができる。
後置式はない。

unless
----

Ruby
```ruby
unless foo?
  "not foo"
else
  "foo"
end

```

Scala
```scala
if (!isFoo)
  "not foo"
else
  "foo"
```

Scalaにunlessはない。

case
----

Ruby
```ruby
case hoge
when 1
  "one"
when 2, 3
  "two or three"
end
```

Scala
```scala
hoge match {
  case 1 =>
    "foo"
  case 2|3 =>
    "two or three"
}
```

Rubyのcase式もScalaのmatch式もどちらも強力だがここでは最も基本的な形を挙げている。

繰り返し
----

### whileループ

Ruby
```ruby
while true
  puts("Hello")
end
```

Scala
```scala
while (true) {
  println("Hello")
}
```

### untilループ

Ruby
```ruby
until f.eof?
  print f.gets
end
```

Scala
```scala
while (!f.isEof) {
  println(f.getLine)
}
```

untilはない。

### forループ

Ruby
```ruby
for i in [1,2,3]
  print i * 2, "\n"
end
```

Scala
```scala
for (i <- Seq(1,2,3)) {
  println(i * 2)
}
```

Scalaのfor式はもっと多機能だがここでは基本的な形を挙げている。

### break

Ruby
```ruby
i = 0
while true
  puts i
  i += 1
  if i > 10
    break
  end
end
```

Scala
```scala
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
```

ループのブレイクが構文として用意されていないので、標準ライブラリの Breaks を使う必要がある。

### next, redo, retry

Ruby
```ruby
lines.each do |line|
  next if line.blank?
  puts line
end
```

Scala
```scala
lines.foreach { line =>
  if (!line.isEmpty) {
    println(line)
  }
}
```

next, redo, retryなどの構文はないのでifなどを使って実装する必要がある。

例外処理
----

### 例外の送出

Ruby
```ruby
raise StandardError.new("例外が起きました")
```

Scala
```scala
throw new RuntimeException("例外が起きました")
```

### 例外の捕捉

Ruby
```ruby
begin
  do_something
rescue ZeroDivisionError => e
  recover(e)
ensure
  must_to_do
end
```

Scala
```scala
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
```

return
----


Ruby
```ruby
return 1
```

Scala
```scala
return 1
```

returnはほぼ同じ。
関数やメソッド、ブロックの最後のretrunを省略すると、Rubyと同じように最後に評価された値を返す。
