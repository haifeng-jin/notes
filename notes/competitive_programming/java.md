# Java Grammar

* java输出可以使用`System.out.format();`这个的使用方法与`printf();`相同。
* 使用文件输入要抛出异常。

```java
public static void main(String args[]) throws FileNotFoundException
Scanner cin =new Scanner (new FileInputStream("t.txt"));
```

* 用java,高精度。读入高精度数可以直接用`cin.nextBigInteger();`
* 使用BigDecimal能处理输入的数字前端有＋号的情况
* java中StringBuffer类似于C++中的String，append函数可以在其后面添加字符，reverse可以反转。
* java中BigInteger的intValue方法可以将其转为int。

