# Declaration and Definition

Declaration mark the existence of an entity (variable, function, struct, or class).

Definition is the complete implementation of a function/struct/class, or memory allocation for a variable.

An entity can be declared multiple times in multiple places but can only have one definition.
This is called the **One Definition Rule (ODR)**.

We can even declare the same function in the same file multiple times.

We often put only declarations in `.h` files and definitions in `.cpp` files.
So, each `.cpp` file can include a lot of `.h` file without violating ODR since
it only includes the declaration without definition.

## Class and struct

One exception is struct/class definition.
The full class definition (including all member declarations) is typically
placed in a header file because the compiler needs to know the full layout and
members of the class whenever an object of that class is created or its members
are accessed.

Here is an example of class declaration vs definition.

```cpp
// declaration
class MyClass;

// definition
class MyClass {
public:
    void memberFunction();
private:
    int data;
};
```

This is why we need the header guards to ensure they are not declared multiple times.


## Variable

It is tricky to declara variables since their definition looks as simple as a declaration.
So we have to use `extern` to mark it as a declaration refering to an external entity.

Here is an example:

```cpp
// declaration
extern int globalCounter;
// definition
int globalCounter = 0;
```
