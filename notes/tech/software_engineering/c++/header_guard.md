# Header Guard

Here is an example of header guard:

```cpp
// A.h
#ifndef A_H
#define A_H

// Declaration of a function defined in A.cpp
void functionInA();

#endif // A_H
```

The `#ifndef`, `#define`, `#endif` are the header guard.
It prevents the content in the header file being declared multiple times during
the C++ build process.

Note that header guard would not guard across mutiple translation units.
The code inside the guard will be preprocessed and compiled in each translation unit.
