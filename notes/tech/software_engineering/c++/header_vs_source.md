# Header vs Source

In general only [declarations](./declaration_and_definition.md) should be put into the header files (`.h` files),
the definitions should all go into source files (`.cpp` files).
This is to obey the ODR.
We want each [translation unit](./translation_unit.md) to be aware of everything declared but not keep a
separate copy of the object in memory. Then, they link to the same object.

There are a few exceptions.

## Inline functions

They are not compiled as separate functions at compile time.
They are just copied and pasted into the functions calling them.
So, they have no declaration or definition. It is OK to have them in the header files.

```cpp
// MyMath.h
#pragma once

inline int add(int a, int b) { // Defined directly in the header
    return a + b;
}
```

Some trivial member functions would also be implicitly converted to inline
functions.

```cpp
// Person.h
#pragma once
#include <string>

class Person {
private:
    std::string name;
public:
    Person(const std::string& n) : name(n) {}
    const std::string& getName() const { // Small function defined in header (implicitly inline)
        return name;
    }
};
```

## Class/Templates

classes and templates are type definitions. They are typically kept in the headers.
They have no linkage.

Classes are typically defined in header files because at compile time, the
compiler needs to know the member functions and variables to compile their
usages in code.

```cpp
#pragma once // Prevents multiple inclusions of the same header

class MyClass {
public:
    int value; // Member variable declared

    MyClass(int val); // Constructor declaration
    void printValue(); // Member function declaration
    void inlineFunc() { // Inline function defined directly in header
        // Body here
        value++;
    }
};
```

So, if you use `MyClass my_class; my_class.printValue();`, the compiler would
have to know the `printValue()` function.  So, the header file has to have the
definition instead of just a declaration of the class name.

For templates, the compiler needs the entire definition of the class or the
function to generate the code for that type when instantiated.

See [template](./template.md) for more details on how a template is compiled.

```cpp
// MyContainer.h
#pragma once

template <typename T>
class MyContainer {
public:
    T value;
    MyContainer(T val) : value(val) {}
    void printValue() { // Template member function defined in header
        // Implementation detail needs to be visible
        std::cout << "Value: " << value << std::endl;
    }
};

template <typename T>
T getMax(T a, T b) { // Template function defined in header
    return (a > b) ? a : b;
}
```

## Constants/Enum

`const` variables with external linkage. If you have a const global variable
that you want to be visible across multiple translation units, it's typically
declared in a header. However, if it's not constexpr and not an integral type,
it still needs a single definition in a .cpp file. But for simple integral
consts, they can often be defined in the header.

```cpp
// Config.h
#pragma once

class Config {
public:
    static const int MAX_USERS = 100; // Can be defined in header
    enum Status { ACTIVE, INACTIVE };
    static const Status DEFAULT_STATUS = ACTIVE; // Can be defined in header
};
```

## `constexpr`

[`constexpr`](./constexpr.md) functions are functions that can be evaluated at compile time if
their arguments are known at compile time.

```cpp
// Constants.h
#pragma once

constexpr int multiply(int x, int y) { // Defined in header for compile-time evaluation
    return x * y;
}
```
