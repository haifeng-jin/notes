# C++ Grammar

* 调试的时候`#define D(x) x`不调试的时候`#define D(x)`，把调试的输出写成`D(printf(“%d\n”, a));`。
* `long long = int * int`的时候一个`int`要强制转换为`long long`。
* c语言中`struct`不能有构造函数，开数组不能使用`const`的值作为大小，而要用`define`.
* 代替`vector`的建图方法，数组模拟链表法，`map[i]`存第`i`个点的第一条边在`e`中的下标。`e`用来存边，`next`记录该点的下一条边的坐标。
* 使用`vector`的效率极低。
* 用c语言写的，`memset`不用包含头文件
* 四舍五入的方法是`(int)(x + 0.5)`
* `cmath`中的`exp(x)`函数是用来求e的`x`次幂。
* 对于`double`类型`scanf`时要用`%lf`，`printf`时要用`%f`。
* `next_permutation(f, f+n);`是将f看做一个排列，并求其下一个排列，所有求得的排列是不重复的，需要a`lgorithm`头文件。在遇到最后一个排列后会返回`false`，并跳转到第一种排列，否则会返回`true`.
* `putchar()`,`getchar()`比`scanf()`,`printf()`快。
* `strtok(char *st1, char *st2)`用`st2`分割`st1`，损坏原串，返回分割后的第一个串的指针，想获得被分割的第二个串则需要调用第二次，并且第一个参数给`NULL`
* `unget(ch, stdin);`可以把读到的字符ch放回到输入文件中去。相当于`getchar()`的逆程。
* `reverse(f, f+n)`可以反转f数组的前n位，这个函数要包含`algorithm`。
* `string::find(char *, pos);`还要注意replace的用法`string::replace(pos, length, char*);`
* `map`常用于查找某元素在数组中的位置。
* 求和函数`accumulate`需要包含头文件`numeric`，使用方法为`sum = accumulate(f, f + n, 0);`
* 求最大值函数`max_element`返回最大值指针，需要包含头文件`algorithm`，使用方法为`max_value=*max_element(f, f+n);`
* 用`sort`排序重载`<`的时候要注意等于的情况也要返回`false`。
* map如果要使用`char*`作为`key`，不能简单的直接使用，可以用`string`作为`map`的`key`，使用的时候将`char*`转换为`string`。转换的方法是使用`string`的`assign`函数。`string.assign(char*);`也可以直接用`string`的构造函数。也可以指定一个`cmp`函数`map<char*,int,cmp>`。
* `<ctime>`中`clock()/CLOCK_PER_SEC`可以查看程序运行时间。
* `strchr(char*, char)`查找`char`在`char*`中第一次出现的位置，如果没有，返回`NULL`。
* `strstr(char*,char*)`同`strchr`,只是查找对象是字符串。
* `isalpha()`,`isdigit()`,`isupper()`,`islower()`可以判断char的类型是字母、数字、大写字母、小写字母。在头文件`cctype`中。`toupper()`,`tolower()`可用于`char`大小写转换，如果参数不符合要求则返回原值。
* `fgets(s, sizeof(s), stdin)`等价于`gets(s)`等价于`cin.getline(s, s_size);`还可以对输入设置截止字符,`cin.getline(s, s_size, ‘\n’);`
* 在使用`printf`时，`%`后面跟`-`号表示左对齐，否则右对齐。`%`后跟0表示用0补齐，否则表示用空格补齐，`%`后跟数字表示对齐宽度。例如：`%-05s`，表示宽度为5右对齐输出`s`，左面空余区域用0补齐。
* 集坐标排序最好用`atan2`，注意`atan2(y,x)`的使用方法，`y`在前，`x`在后。返回X轴正方向到原点到（x，y）点的射线的到角。
* 注意`vector`用法，`erase`函数返回的是删除后的下一个元素的指针。迭代器的写法是：`vector<  >::iterator i;`。或者`typeof(v.begin()) i`。
* `priority_queue`如果想同时建立小根堆和大根堆需要这样写`priority_queue<Elem, vector<Elem> , greater<Elem> > pq3; //小根`, `priority_queue<Elem, vector<Elem> , less<Elem> > pq2;//大根`。并重载大于和小于号。。
* `search(f, f+n, g, g+m);`在`f`中查找`g`，返回第一个与`g`完全匹配的起始位置，若无法匹配则返回`f+m`。
* `copy(f,f+n,g);`将f中的`n`个元素拷贝到`g`中。
* 使用`map`,首先`#include <map>`，然后声明`map<A，B>`，`map`可以当`B`类型数组用，下标为`A`类型。成员函数`find()`可以查找数组下标是否存在，如果没找到返回值为成员函数`.end()`的值。找到了返回下标。
* `scanf`的用法，`%*[ ]`,表示越过`[ ]`中的字符，`%[a-z]`表示读入字符串，直到遇到不是`a-z`中的字符为止，也可以在中括号里输入多个字符用逗号隔开。`%[^a]`表示读入字符串直到遇到字符`a`为止，但`a`并没有被读入。
* `multiset`是一个可存储重复元素的`set`。查找某元素的指针可以用`a.lower_bound(target)`。插入用`insert`，删除用`erase`，两者效率都是logN。可以用于解决不断修改一个集合内元素的内容还不断询问最大最小值的问题。
* `deque`是一个双向队列也可以求解移动窗口问题。
* `stringstream`可以将字符串作为输入流，从中读入内容。用`stringstream sin(inputstring);` 之后读入方法与`cin`一样。需要包含`sstream`头文件。
* `char*`转化成string可以直接用等号赋值。
* 大数组不能开在函数中，要使用全局变量
* 全局变量与局部变量以及结构体中的变量最好不要使用相同的名字，否则当名字指代错误引起bug时，很难发现错误。

