# Compiler

* AST is short for abstract syntax tree.
* IR is short for intermediate representation.
* The compiler can optimize the code execution because assembly language have more control over the hardware.
* LLVM can do both JIT (just-in-time) compiling and AOT (ahead-of-time) compiling.

## Deep Learning Compiler

* If running on GPUs, the output of a deep learning compiler is PTX, something like assembly code for GPUs.
* Deep learning compilers have both JIT and AOT kind.

### How does a driver work?
A driver is a program usually loaded by the operating system at start.  It
creates an abstraction of the hardware it manages.  A program running on the
CPU may call this driver through the bus, and the driver will operate the
hardware and writeback the results.

The GPU has a Nvidia driver, which contains a CUDA driver.
They operate the GPUs.

### How does a CUDA C++ code compile?

It is compiled with Nvidia CUDA Compiler (NVCC) instead of gcc or g++ or clang.
The NVCC is implemented based on LLVM.
It would analysis the C++ code and extract out the code to run on CPU (the host code) and the code to run on GPU (the device code).
Put them into an executable binary file, named CUDA Binary (cubin) file.
The executable runs on the host machine, but also contains the parts to run on GPU, like the PTX.
When runs it will call the CUDA runtime to run on GPU.

### XLA

XLA is the deep learning compiler for TensorFlow.
XLA is a JIT compiler.
It starts from High level IR.
It outputs the LLVM IR to run on GPU.

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

