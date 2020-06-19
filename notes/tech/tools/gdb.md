# Debugging with GDB | BetterExplained
#tech/tool
gdb primary tutorial

- - - -

A debugger lets you pause a program, examine and change variables, and step through code. Spend a few hours to learn one so you can avoid dozens of hours of frustration in the future. This is a quick guide, more information here:

* [Official Page](http://www.gnu.org/software/gdb/) – [Documentation](http://sources.redhat.com/gdb/current/onlinedocs/gdb_toc.html)
* [Sample session](http://sources.redhat.com/gdb/current/onlinedocs/gdb_2.html#SEC5) – [Short Tutorial](http://www.cs.princeton.edu/~benjasik/gdb/gdbtut.html) – [Long Tutorial](http://heather.cs.ucdavis.edu/~matloff/UnixAndC/CLanguage/Debug.html)
## Getting Started: Starting and Stopping

* `gcc -g myprogram.c`

	* Compiles myprogram.c with the debugging option (-g). You still get an a.out, but it contains debugging information that lets you use variables and function names inside GDB, rather than raw memory locations (not fun).

* `gdb a.out`

	* Opens GDB with file a.out, but does not run the program. You’ll see a prompt `(gdb)` – all examples are from this prompt.

* `r`
* `r arg1 arg2`
* `r < file1`

	* Three ways to run “a.out”, loaded previously. You can run it directly (r), pass arguments (r arg1 arg2), or feed in a file. You will usually set breakpoints before running.

* `help`
* `h breakpoints`

	* List help topics (help) or get help on a specific topic (h breakpoints). GDB is well-documented.

* `q` – Quit GDB
## Stepping Through Code

Stepping lets you trace the path of your program, and zero in on the code that is crashing or returning invalid input.

* `l`
* `l 50`
* `l myfunction`

	* List 10 lines of source code for current line (l), a specific line (l 50), or for a function (l myfunction).

* `next`

	* Run program until next line, then pause. If the current line is a function, execute the entire function, then pause. Next is good for walking through your code quickly.

* `step`

	* Run the next instruction, not line. If the current instructions is setting a variable, it is the same as `next`. If it’s a function, it will jump into the function, execute the first statement, then pause. Step is good for diving into the details of your code.

* `finish`

	* Finish executing the current function, then pause (also called step out). Useful if you accidentally stepped into a function.

## Breakpoints and Watchpoints

Breakpoints are one of the keys to debugging. They pause (break) a program when it reaches a certain location. You can examine and change variables, then resume execution. This is helpful when seeing why certain inputs fail, or testing inputs.

* `break 45`
* `break myfunction`

	* Set a breakpoint at line 45, or at myfunction. The program will pause when it reaches the breakpoint.

* `watch x == 3`

	* Set a watchpoint, which pauses the program when a condition changes (when x == 3 changes). Watchpoints are great for certain inputs (myPtr != NULL) without having to break on _every_ function call.

* `continue`

	* Resume execution after being paused by a breakpoint_watchpoint. The program will continue until it hits the next breakpoint_watchpoint.

* `delete N`

	* Delete breakpoint N (breakpoints are numbered when created).

## Setting Variables and Calling Functions

Viewing and changing variables at run-time is a huge part of debugging. Try giving functions invalid inputs or running other test cases to find the root of problems. Typically, you will view/set variables when the program is paused.

* `print x`

	* Print current value of variable x. Being able to use the original variable names is why the (-g) flag is needed; programs compiled regularly have this information removed.

* `set x = 3`
* `set x = y`

	* Set x to a set value (3) or to another variable (y)

* `call myfunction()`
* `call myotherfunction(x)`
* `call strlen(mystring)`

	* Call user-defined or system functions. This is extremely useful, but beware calling buggy functions.

* `display x`
* `undisplay x`

	* Constantly display value of variable x, which is shown after every step or pause. Useful if you are constantly checking for a certain value. Use undisplay to remove the constant display.

## Backtrace and Changing Frames

The _stack_ is a list of the current function calls – it shows you where you are in the program. A _frame_ stores the details of a single function call, such as the arguments.

* `bt`

	* Backtrace, aka print the current function stack to show where you are in the current program. If `main` calls function `a()`, which calls `b()`, which calls `c()`, the backtrace is

```
c <= current location
b
a
main
```

* `up`
* `down`

	* Move to the next frame up or down in the function stack. If you are in `c`, you can move to `b` or `a` to examine local variables.

* `return`

	* Return from current function.

## Crashes and Core Dumps

A “core dump” is a snapshot of memory at the instant the program crashed, typically saved in a file called “core”. GDB can read the core dump and give you the line number of the crash, the arguments that were passed, and more. This is very helpful, but remember to compile with (-g) or the core dump will be difficult to debug.

* `gdb myprogram core`

	* Debug myprogram with “core” as the core dump file.

* `bt`

	* Print the backtrace (function stack) at the point of the crash. Examine variables using the techniques above.

## Handling Signals

Signals are messages thrown after certain events, such as a timer or error. GDB may pause when it encounters a signal; you may wish to ignore them instead.

* `handle [signalname] [action]`
* `handle SIGUSR1 nostop`
* `handle SIGUSR1 noprint`
* `handle SIGUSR1 ignore`

	* Tell GDB to ignore a certain signal ( `SIGUSR1` ) when it occurs. There are varying levels of ignoring.

## Integration with Emacs

The Emacs text editor integrates well with GDB. Debugging directly inside the editor is great because you can see an entire screen of code at a time. Use `M-x gdb` to start a new window with GDB and [learn more here](http://sources.redhat.com/gdb/current/onlinedocs/gdb_24.html).

## Tips

* I often prefer watchpoints to breakpoints. Rather than breaking on every loop and checking a variable, set a watchpoint for when the variable gets to the value you need (i == 25, ptr != null, etc.).
* `printf` works well for tracing. But wrap `printf` in a `log` function for flexibility.
* Try passing a log level with your message (1 is most important, 3 is least). You can tweak your log function to send email on critical errors, log to a file, etc.
* Code speaks, so here it is. Use `#define LOG_LEVEL LOG_WARN` to display warnings and above. Use `#define LOG_LEVEL LOG_NONE` to turn off debugging.

```
#include <stdio.h>

#define LOG_NONE 0
#define LOG_ERROR 1
#define LOG_WARN 2
#define LOG_INFO 3
#define LOG_LEVEL LOG_WARN

// shows msg if allowed by LOG_LEVEL
int log(char *msg, int level){
  if (LOG_LEVEL >= level){
    printf("LOG %d: %s\n", level, msg);
    // could also log to file
  }

  return 0;
}

int main(int argc, char** argv){
  printf("Hi there!\n");

  log("Really bad error!", LOG_ERROR);
  log("Warning, not so serious.", LOG_WARN);
  log("Just some info, not that important.", LOG_INFO);

  return 0;
}
```

* Spend the time to learn GDB (or another debugging tool)! I know, it’s like telling people to eat their vegetables, but it really is good for you – you’ll thank me later.

 Like

8
 

 [Tweet](https://twitter.com/intent/tweet?original_referer=http%3A%2F%2Fbetterexplained.com%2Farticles%2Fdebugging-with-gdb%2F&amp;text=Debugging%20with%20GDB%20&amp;tw_p=tweetbutton&amp;url=http%3A%2F%2Fbetterexplained.com%2Farticles%2Fdebugging-with-gdb%2F)
  [2](http://twitter.com/search?q=http%3A%2F%2Fbetterexplained.com%2Farticles%2Fdebugging-with-gdb%2F)

![](Debugging%20with%20GDB%20%7C%20BetterExplained/image_1.gif)

![](Debugging%20with%20GDB%20%7C%20BetterExplained/image_1%202.gif)
This page has been shared 2 times. View these Tweets.

   [5](http://betterexplained.com/articles/debugging-with-gdb/#)

# 8 gdb tricks you should know (Ksplice Blog)

**Source URL:** [https://blogs.oracle.com/ksplice/entry/8_gdb_tricks_you_should](https://blogs.oracle.com/ksplice/entry/8_gdb_tricks_you_should)

« [Coffee shop Internet...](https://blogs.oracle.com/ksplice/entry/coffee_shop_internet_access) | [Main](https://blogs.oracle.com/ksplice/) | [Happy Birthday Kspli...](https://blogs.oracle.com/ksplice/entry/happy_birthday_ksplice_uptrack) » 
### 8 gdb tricks you should know

#### By Ksplice Post Importer on [Jan 24, 2011](https://blogs.oracle.com/ksplice/entry/8_gdb_tricks_you_should#)

Despite its age, gdb remains an amazingly versatile and flexible tool, and mastering it can save you huge amounts of time when trying to debug problems in your code. In this post, I'll share 10 tips and tricks for using GDB to debug most efficiently.

I'll be using the Linux kernel for examples throughout this post, not because these examples are necessarily realistic, but because it's a large C codebase that I know and that anyone can download and take a look at. Don't worry if you aren't familiar with Linux's source in particular -- the details of the examples won't matter too much.

1. `break WHERE if COND`

1. If you've ever used gdb, you almost certainly know about the "breakpoint" command, which lets you break at some specified point in the debugged program.

1. But did you know that you can set conditional breakpoints? If you add `if CONDITION` to a breakpoint command, you can include an expression to be evaluated whenever the program reaches that point, and the program will only be stopped if the condition is fulfilled. Suppose I was debugging the Linux kernel and wanted to stop whenever init got scheduled. I could do:

```
(gdb) break context_switch if next == init_task
```

1. Note that the condition is evaluated by gdb, not by the debugged program, so you still pay the cost of the target stopping and switching to gdb every time the breakpoint is hit. As such, they still slow the target down in relation to to how often the target location is hit, not how often the condition is met.

2. `command`

2. In addition to conditional breakpoints, the `command` command lets you specify commands to be run every time you hit a breakpoint. This can be used for a number of things, but one of the most basic is to augment points in a program to include debug output, without having to recompile and restart the program. I could get a minimal log of every `mmap()` operation performed on a system using:

```
(gdb) b do_mmap_pgoff 
Breakpoint 1 at 0xffffffff8111a441: file mm/mmap.c, line 940.
(gdb) command 1
Type commands for when breakpoint 1 is hit, one per line.
End with a line saying just "end".
>print addr
>print len
>print prot
>end
(gdb)
```

3. `gdb --args`

3. This one is simple, but a huge timesaver if you didn't know it. If you just want to start a program under gdb, passing some arguments on the command line, you can just build your command-line like usual, and then put "gdb --args" in front to launch gdb with the target program and the argument list both set:

```
[~]$ gdb --args pizzamaker --deep-dish --toppings=pepperoni
...
(gdb) show args
Argument list to give program being debugged when it is started is
  " --deep-dish --toppings=pepperoni".
(gdb) b main
Breakpoint 1 at 0x45467c: file oven.c, line 123.
(gdb) run
...
```

3. I find this especially useful if I want to debug a project that has some arcane wrapper script that assembles lots of environment variables and possibly arguments before launching the actual binary (I'm looking at you, libtool). Instead of trying to replicate all that state and then launch gdb, simply make a copy of the wrapper, find the final "exec" call or similar, and add "gdb --args" in front.

4. Finding source files

4. I run Ubuntu, so I can download debug symbols for most of the packages on my system from [ddebs.ubuntu.com](http://ddebs.ubuntu.com/), and I can get source using `apt-get source`. But how do I tell gdb to put the two together? If the debug symbols include relative paths, I can use gdb's `directory` command to add the source directory to my source path:

```
[~/src]$ apt-get source coreutils
[~/src]$ sudo apt-get install coreutils-dbgsym
[~/src]$ gdb /bin/ls
GNU gdb (GDB) 7.1-ubuntu
(gdb) list main
1192    ls.c: No such file or directory.
    in ls.c
(gdb) directory ~/src/coreutils-7.4/src/
Source directories searched: /home/nelhage/src/coreutils-7.4:$cdir:$cwd
(gdb) list main
1192        }
1193    }
1194    
1195    int
1196    main (int argc, char **argv)
1197    {
1198      int i;
1199      struct pending *thispend;
1200      int n_files;
1201
```

4. Sometimes, however, debug symbols end up with absolute paths, such as the kernel's. In that case, I can use `set substitute-path` to tell gdb how to translate paths:

```
[~/src]$ apt-get source linux-image-2.6.32-25-generic
[~/src]$ sudo apt-get install linux-image-2.6.32-25-generic-dbgsym
[~/src]$ gdb /usr/lib/debug/boot/vmlinux-2.6.32-25-generic 
(gdb) list schedule
5519    /build/buildd/linux-2.6.32/kernel/sched.c: No such file or directory.
    in /build/buildd/linux-2.6.32/kernel/sched.c
(gdb) set substitute-path /build/buildd/linux-2.6.32 /home/nelhage/src/linux-2.6.32/
(gdb) list schedule
5519    
5520    static void put_prev_task(struct rq *rq, struct task_struct *p)
5521    {
5522        u64 runtime = p->se.sum_exec_runtime - p->se.prev_sum_exec_runtime;
5523    
5524        update_avg(&p->se.avg_running, runtime);
5525    
5526        if (p->state == TASK_RUNNING) {
5527            /*
5528             * In order to avoid avg_overlap growing stale when we are
```

5. Debugging macros

5. One of the standard reasons almost everyone will tell you to prefer inline functions over macros is that debuggers tend to be better at dealing with inline functions. And in fact, by default, gdb doesn't know anything at all about macros, even when your project was built with debug symbols:

```
(gdb) p GFP_ATOMIC
No symbol "GFP_ATOMIC" in current context.
(gdb) p task_is_stopped(&init_task)
No symbol "task_is_stopped" in current context.
```

5. However, if you're willing to tell GCC to generate debug symbols specifically optimized for gdb, using `-ggdb3`, it can preserve this information:

```
$ make KCFLAGS=-ggdb3
...
(gdb) break schedule
(gdb) continue
(gdb) p/x GFP_ATOMIC
$1 = 0x20
(gdb) p task_is_stopped_or_traced(init_task)
$2 = 0
```

5. You can also use the `macro` and `info macro` commands to work with macros from inside your gdb session:

```
(gdb) macro expand task_is_stopped_or_traced(init_task)
expands to: ((init_task->state & (4 | 8)) != 0)
(gdb) info macro task_is_stopped_or_traced
Defined at include/linux/sched.h:218
  included at include/linux/nmi.h:7
  included at kernel/sched.c:31
#define task_is_stopped_or_traced(task) ((task->state & (__TASK_STOPPED | __TASK_TRACED)) != 0)
```

5. Note that gdb actually knows which contexts macros are and aren't visible, so when you have the program stopped inside some function, you can only access macros visible at that point. (You can see that the "included at" lines above show you through exactly what path the macro is visible).

6. gdb variables

6. Whenever you `print` a variable in gdb, it prints this weird `$NN =` before it in the output:

```
(gdb) p 5+5
$1 = 10
```

6. This is actually a gdb variable, that you can use to reference that same variable any time later in your session:

```
(gdb) p $1
$2 = 10
```

6. You can also assign your own variables for convenience, using `set`:

```
(gdb) set $foo = 4
(gdb) p $foo
$3 = 4
```

6. This can be useful to grab a reference to some complex expression or similar that you'll be referencing many times, or, for example, for simplicity in writing a conditional breakpoint (see tip 1).

7. Register variables

7. In addition to the numeric variables, and any variables you define, gdb exposes your machine's registers as pseudo-variables, including some cross-architecture aliases for common ones, like `$sp` for the the stack pointer, or `$pc` for the program counter or instruction pointer.

7. These are most useful when debugging assembly code or code without debugging symbols. Combined with a knowledge of your machine's calling convention, for example, you can use these to inspect function parameters:

```
(gdb) break write if $rsi == 2
```

7. will break on all writes to stderr on amd64, where the `$rsi` register is used to pass the first parameter.

8. The `x` command

8. Most people who've used gdb know about the `print` or `p` command, because of its obvious name, but I've been surprised how many don't know about the power of the `x` command.

8. `x` (for "e **x** amine") is used to output regions of memory in various formats. It takes two arguments in a slightly unusual syntax:

```
x/FMT ADDRESS
```

8. `ADDRESS`, unsurprisingly, is the address to examine; It can be an arbitrary expression, like the argument to `print`.

8. `FMT` controls how the memory should be dumped, and consists of (up to) three components:

	* A numeric COUNT of how many elements to dump
	* A single-character FORMAT, indicating how to interpret and display each element
	* A single-character SIZE, indicating the size of each element to display.
`x` displays COUNT elements of length SIZE each, starting from ADDRESS, formatting them according to the FORMAT.

There are many valid "format" arguments; `help x` in gdb will give you the full list, so here's my favorites:

`x/x` displays elements in hex, `x/d` displays them as signed decimals, `x/c` displays characters, `x/i` disassembles memory as instructions, and `x/s` interprets memory as C strings.

The SIZE argument can be one of: `b`, `h`, `w`, and `g`, for one-, two-, four-, and eight-byte blocks, respectively.

If you have debug symbols so that GDB knows the types of everything you might want to inspect, `p` is usually a better choice, but if not, `x` is invaluable for taking a look at memory.

```
[~]$ grep saved_command /proc/kallsyms
ffffffff81946000 B saved_command_line

(gdb) x/s 0xffffffff81946000
ffffffff81946000 <>:     "root=/dev/sda1 quiet"
```

`x/i` is invaluable as a quick way to disassemble memory:

```
(gdb) x/5i schedule
   0xffffffff8154804a <schedule>:   push   %rbp
   0xffffffff8154804b <schedule+1>: mov    $0x11ac0,%rdx
   0xffffffff81548052 <schedule+8>: mov    %gs:0xb588,%rax
   0xffffffff8154805b <schedule+17>:    mov    %rsp,%rbp
   0xffffffff8154805e <schedule+20>:    push   %r15
```

If I'm stopped at a segfault in unknown code, one of the first things I try is something like `x/20i $ip-40`, to get a look at what the code I'm stopped at looks like.

A quick-and-dirty but surprisingly effective way to debug memory leaks is to let the leak grow until it consumes most of a program's memory, and then attach `gdb` and just `x` random pieces of memory. Since the leaked data is using up most of memory, you'll usually hit it pretty quickly, and can try to interpret what it must have come from.

~ [nelhage](https://twitter.com/nelhage)

- - - -

**Ksplice is hiring!**

Do you love tinkering with, exploring, and debugging Linux systems? Does writing Python clones of your favorite childhood computer games sound like a fun weekend project? Have you ever told a joke whose punch line was a git command?

Join Ksplice and work on technology that most people will tell you is impossible: updating the Linux kernel while it is running.

Help us develop the software and infrastructure to bring rebootless kernel updates to Linux, as well as new operating system kernels and other parts of the software stack. We're hiring backend, frontend, and kernel engineers. Say hello at [jobs@ksplice.com](mailto:jobs@ksplice.com)!

Category: programming :::

Tags: [c](https://blogs.oracle.com/ksplice/tags/c) [debugging](https://blogs.oracle.com/ksplice/tags/debugging) [gdb](https://blogs.oracle.com/ksplice/tags/gdb) [linux](https://blogs.oracle.com/ksplice/tags/linux) [tricks](https://blogs.oracle.com/ksplice/tags/tricks)  ::: 

[Permanent link to this entry](https://blogs.oracle.com/ksplice/entry/8_gdb_tricks_you_should)  ::: 

« [Coffee shop Internet...](https://blogs.oracle.com/ksplice/entry/coffee_shop_internet_access) | [Main](https://blogs.oracle.com/ksplice/) | [Happy Birthday Kspli...](https://blogs.oracle.com/ksplice/entry/happy_birthday_ksplice_uptrack) » 
   Comments:

   

One of my favourite GDB tricks: The @ symbol, used to view many elements of an array/STL vector in one go.

With C, it is easy to view the full array:

If the code is:
int a[ 10 ] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };

Then:
(gdb) p a
$1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

However this is not useful if the array has 1000 entries, and you want to view a handful of entries located somewhere in the middle. Also, this will not work with a C++ vector, because it will dump the vector object's data members.

Using the '@' symbol allows us to do both:

(gdb) p *&a[0]@10
$1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

This prints the first 10 elements in the vector. Looks ugly, but is not so complicated really: '&a[0]' gets the address of the first element. '*' dereferences the address back to the vector's data type. Finally '@10' pulls out 10 elements.

Of course, to view elements 550-553 in a long vector, all you do is 'p *&a[550]@4'.

Posted by **Niraj** on August 28, 2012 at 07:37 AM EDT [#](https://blogs.oracle.com/ksplice/entry/8_gdb_tricks_you_should#comment-1346153863111) 

Post a Comment:
   

* Name:
* E-Mail:
* URL:
* Notify me by email of new comments
* Remember Information?
* Your Comment:
* HTML Syntax: NOT allowed
* Please answer this simple math question

* 4 + 93 =

http://betterexplained.com/articles/debugging-with-gdb/