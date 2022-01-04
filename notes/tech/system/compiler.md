# Compiler

* AST is short for abstract syntax tree.
* IR is short for intermediate representation.
* The compiler can optimize the code execution because assembly language have more control over the hardware.
* LLVM can do both JIT (just-in-time) compiling and AOT (ahead-of-time) compiling.

## Deep Learning Compiler

* If running on GPUs, the output of a deep learning compiler is PTX, something like assembly code for GPUs.
* Deep learning compilers have both JIT and AOT kind.

## Language Compiler

### C Compiling Process

It contains 4 steps in total: preprocessing, compile, assembly, and linking.

#### Preprocessing
`*.c -> *.i`

It just fetch all the `#include<>` sources and insert them into the code.

#### Compile
`*.i -> *.s`

It converts the C language into assembly language. It is still text file till now.

#### Assembly
`*.s -> *.o`

It converts the assembly language to an binary file with machine language instructions.

#### Linking
`*.o -> *`

There are some functions that are built-in in C language, which doesn't require an `include` before using,
for example `printf`.
They are precompiled and assembled to save the compiling time.
Linking is to fetch these binaries and pack them all together with the compiled program
so that the final executable file is self-contained.

### Java Compiling Process
### Python Interpreting Process

