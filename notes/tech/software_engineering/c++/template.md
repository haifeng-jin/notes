# Template

If the same code for different types looks duplicated, we can use templates to reduce them.

```cpp
void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void swap(double& a, double& b) {
    double temp = a;
    a = b;
    b = temp;
}
```

This can be changed to:

```cpp
template <typename T>
void swap(T& a, T& b) {
    T temp = a;
    a = b;
    b = temp;
}
```

Templates can be used with functions:

```cpp
template <typename T> // Declares a template with a type parameter T
T maximum(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    int i = maximum(5, 10);      // T becomes int
    double d = maximum(3.14, 2.71); // T becomes double
    char c = maximum('a', 'z');   // T becomes char
    return 0;
}
```

And classes:

```cpp
template <typename T1, typename T2> // Two type parameters
class Pair {
public:
    T1 first;
    T2 second;

    Pair(T1 f, T2 s) : first(f), second(s) {}

    void print() {
        std::cout << "First: " << first << ", Second: " << second << std::endl;
    }
};

int main() {
    Pair<int, double> p1(10, 20.5);      // T1 is int, T2 is double
    Pair<std::string, int> p2("Hello", 123); // T1 is std::string, T2 is int

    p1.print();
    p2.print();
    return 0;
}
```

And variables:

```cpp
template <typename T>
constexpr int DefaultBufferSize = 1024 / sizeof(T);

// Usage:
// char buffer_char[DefaultBufferSize<char>];   // buffer_char has size 1024
// int buffer_int[DefaultBufferSize<int>];     // buffer_int has size 256 (if int is 4 bytes)
```

## Type specific implementations

For certain types, you may want to have a specialized implementation instead of
the general template one.  You can use the explicit specialization here.

```cpp
template <typename T>
void print(T value) {
    std::cout << "Generic print: " << value << std::endl;
}

template <> // No new template parameters; we're specializing an existing one
void print<const char*>(const char* value) { // Specify the exact type
    std::cout << "Specialized for C-string: " << value << std::endl;
}

// Usage:
// print(123);           // Calls generic print<int>
// print("Hello");       // Calls specialized print<const char*>
// print(std::string("World")); // Calls generic print<std::string>
```

## Limit the types

To limit what types can be used with the template, you can simply use asserts.

```cpp
template <typename T>
T multiply(T a, T b) {
    // Assert that T is an arithmetic type (e.g., int, float, double)
    static_assert(std::is_arithmetic_v<T>, "Type must be an arithmetic type!");
    return a * b;
}
```

Or for C++20 and later, you can use `concepts`.

```cpp
// Define a concept that requires a type to be integral
template <typename T>
concept Integral = std::is_integral_v<T>;

// Use the concept to constrain the template function
template <Integral T>
T add(T a, T b) {
    return a + b;
}
```

## Compile

They should be defined in header files.
They need to be instantiated at compile time since the compiler needs to know
the function/class when it sees the usages.

The compiler only generate the code for the usages of the types it saw, not for
every type.  So the more types used with the template, the longer it compiles.
